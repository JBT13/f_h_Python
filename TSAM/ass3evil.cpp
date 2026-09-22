#include <sys/socket.h>
#include <stdio.h>
#include <iostream>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <cstdlib>
#include <string>
#include <cstring>
#include <set>
#include <errno.h>
#include <netinet/ip.h>
#include <netinet/udp.h>
#include <netinet/ip6.h>
using namespace std;

unsigned char msg_b[5];

uint16_t calculate_ip_checksum(uint16_t *addr, int len) {
    uint32_t sum = 0;

    // Sum 16-bit words
    while (len > 1) {
        sum += *addr++;
        len -= 2;
    }

    // Add left-over byte, if any
    if (len > 0) {
        sum += *(uint8_t*)addr;
    }

    // Fold 32-bit sum to 16 bits (carry propagation)
    while (sum >> 16) {
        sum = (sum & 0xFFFF) + (sum >> 16);
    }

    // One's complement
    return (uint16_t)(~sum);
}

uint16_t calculate_ipv6_udp_checksum(struct ip6_hdr *ip6, struct udphdr *udp, const unsigned char *payload, int payload_len) {
    uint32_t sum = 0;
    uint16_t *ptr;

    // 1. IPv6 Pseudo-Header: Source and Destination IPs
    ptr = (uint16_t *)&ip6->ip6_src;
    for (int i = 0; i < 16; i++) sum += *ptr++; // 16 words = 32 bytes

    // 2. IPv6 Pseudo-Header: UDP Length & Protocol (17)
    sum += udp->len; // udp->len is already in Network Byte Order
    sum += htons(IPPROTO_UDP); 

    // 3. UDP Header
    ptr = (uint16_t *)udp;
    for (int i = 0; i < 4; i++) sum += *ptr++;

    // 4. Payload
    ptr = (uint16_t *)payload;
    for (int i = 0; i < payload_len / 2; i++) {
        sum += *ptr++;
    }
    // Handle odd-length payloads (like your 5-byte message)
    if (payload_len % 2 != 0) {
        uint16_t last = 0;
        *((uint8_t*)&last) = payload[payload_len - 1]; // Pad with trailing zero
        sum += last;
    }

    // Fold 32-bit sum into 16 bits
    while (sum >> 16) {
        sum = (sum & 0xFFFF) + (sum >> 16);
    }

    uint16_t final_sum = ~sum;
    // In UDP, a calculated checksum of 0 is transmitted as all ones (0xFFFF)
    return (final_sum == 0) ? 0xFFFF : final_sum; 
}

void GUARDIAN(int sockfd, const char *buffer, int recv_len, const struct sockaddr_in& address) {
    if (recv_len < sizeof(struct ip6_hdr) + sizeof(struct udphdr)) return;

    struct ip6_hdr *rx_ip6 = (struct ip6_hdr *)buffer;
    struct udphdr *rx_udp = (struct udphdr *)(buffer + sizeof(struct ip6_hdr));

    struct ip6_hdr tx_ip6;
    struct udphdr tx_udp;

    memset(&tx_ip6, 0, sizeof(tx_ip6));
    memset(&tx_udp, 0, sizeof(tx_udp));

    // FIX: Copy the flow label and version directly from rx_ip6
    tx_ip6.ip6_flow = rx_ip6->ip6_flow; 
    tx_ip6.ip6_plen = htons(sizeof(struct udphdr) + 5); 
    tx_ip6.ip6_nxt = IPPROTO_UDP;
    tx_ip6.ip6_hops = 64;
    
    // Swap source and destination IPv6 addresses
    tx_ip6.ip6_src = rx_ip6->ip6_dst;
    tx_ip6.ip6_dst = rx_ip6->ip6_src;

    // Swap UDP ports
    tx_udp.source = rx_udp->dest;   
    tx_udp.dest = rx_udp->source;
    tx_udp.len = htons(sizeof(struct udphdr) + 5);
    tx_udp.check = 0; 

    // Calculate checksum
    tx_udp.check = calculate_ipv6_udp_checksum(&tx_ip6, &tx_udp, msg_b, 5);

    // Assemble outer packet
    char packet[1024];
    memcpy(packet, &tx_ip6, sizeof(struct ip6_hdr));
    memcpy(packet + sizeof(struct ip6_hdr), &tx_udp, sizeof(struct udphdr));
    memcpy(packet + sizeof(struct ip6_hdr) + sizeof(struct udphdr), msg_b, 5);

    size_t total_len = sizeof(struct ip6_hdr) + sizeof(struct udphdr) + 5;

    int ret = sendto(sockfd, packet, total_len, 0, (const struct sockaddr*)&address, sizeof(address));
    if (ret < 0) {
        perror("Error sending GUARDIAN response");
    } else {
        cout << "Sent Guardian encapsulated response!" << endl;
    }
}


void SECRET(int sockfd, const char *buffer, uint32_t secret_num, const struct sockaddr_in& address) {
    
    msg_b[0] = buffer[0]; // Getting group Id 
    uint32_t c_net; 
    memcpy(&c_net, buffer + 1, 4); 
    uint32_t challenge = ntohl(c_net); // turning Network byte order to local
    uint32_t sigil = challenge ^ secret_num; // XOR secret num with local 
    uint32_t sigil_net = htonl(sigil); // turning local to Network byte

    memcpy(msg_b + 1, &sigil_net, 4); // with the XOR sigil

    int ret = sendto(sockfd, msg_b, 5, 0, (const struct sockaddr*)&address, sizeof(address));
    if (ret < 0) perror("Error sending Sigil");
}

void evil(const char *ipaddr, int port, int source_port) {
    struct ip ip_header;
    struct udphdr udp_header;

    memset(&ip_header, 0, sizeof(ip_header));
    memset(&udp_header, 0, sizeof(udp_header));

    // IP Header Setup
    ip_header.ip_v = 4;
    ip_header.ip_hl = 5;
    ip_header.ip_tos = 0;
    // LINUX FIX: Use htons() for IP length
    ip_header.ip_len = htons(sizeof(struct ip) + sizeof(struct udphdr) + sizeof(msg_b));
    ip_header.ip_id = 0;
    // LINUX FIX: Use htons() for the offset (evil bit)
    ip_header.ip_off = htons(IP_RF); 
    ip_header.ip_ttl = 64;
    ip_header.ip_p = IPPROTO_UDP;
    
    // LINUX FIX: Assign a source IP (INADDR_ANY lets the kernel choose the interface IP)
    ip_header.ip_src.s_addr = INADDR_ANY;
    inet_pton(AF_INET, ipaddr, &ip_header.ip_dst);

    ip_header.ip_sum = 0;
    ip_header.ip_sum = calculate_ip_checksum((uint16_t*)&ip_header, sizeof(struct ip));

    // LINUX FIX: Use Linux struct member names (source, dest, len, check)
    udp_header.source = htons(source_port);
    udp_header.dest = htons(port);
    udp_header.len = htons(sizeof(struct udphdr) + sizeof(msg_b));
    udp_header.check = 0;

    char packet[1024];

    memcpy(packet, &ip_header, sizeof(struct ip));
    memcpy(packet + sizeof(struct ip), &udp_header, sizeof(struct udphdr));
    memcpy(packet + sizeof(struct ip) + sizeof(struct udphdr), msg_b, sizeof(msg_b));

    int rawsocket = socket(AF_INET, SOCK_RAW, IPPROTO_UDP);
    if (rawsocket < 0) {
        perror("socket");
        exit(1);
    }

    int on = 1;
    if (setsockopt(rawsocket, IPPROTO_IP, IP_HDRINCL, &on, sizeof(on)) < 0) {
        perror("setsockopt");
        exit(1);
    }
    
    struct sockaddr_in destaddr;
    destaddr.sin_family = AF_INET;
    destaddr.sin_port = htons(port);

    if (inet_pton(AF_INET, ipaddr, &destaddr.sin_addr) < 1) {
        std::cerr << "Invalid IP adress or address family: " << ipaddr << std::endl;
        exit(1);
    }

    size_t total_len = sizeof(struct ip) + sizeof(struct udphdr) + sizeof(msg_b);
    int ret = sendto(rawsocket, packet, total_len, 0, (struct sockaddr *)&destaddr, sizeof(destaddr));

    if (ret < 0) {
        perror("Error sending");
        exit(1);
    }
}

int main(int argc, const char* argv[]) {
    if (argc < 4) {
        std::cerr << "Usage: " << argv[0] << " <IP> <lowport> <highport>" << std::endl;
        return 1;
    }

    const char *ipaddr = argv[1];
    int lowport = stoi(argv[2]);
    int highport = stoi(argv[3]);

    int sockfd;
    string s;
    uint32_t secret_num = 130306;
    string secret = "S.E.C.R.E.T.:"; 
    string names = "jeremias25,sylviat24,thordish25";
    uint32_t secret_num_net = htonl(secret_num); // turning my secret number to network byte order

    char msg[256];
    size_t text_len = secret.length() + names.length(); 

    memcpy(msg, secret.c_str(), secret.length());
    memcpy(msg + secret.length(), names.c_str(), names.length());
    memcpy(msg + text_len, &secret_num_net, sizeof(secret_num_net));

    size_t total_len = text_len + sizeof(secret_num_net);

    struct timeval timeout;
    timeout.tv_sec = 30;
    timeout.tv_usec = 0;
    
    int ret;

    struct sockaddr_in destaddr;
    destaddr.sin_family = AF_INET;

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        perror("Error creating socket");
        exit(1);
    }
        
    if (inet_pton(AF_INET, ipaddr, &destaddr.sin_addr) < 1) {
        std::cerr << "Invalid IP adress or address family: " << ipaddr << std::endl;
        exit(1);
    }

    if (setsockopt(sockfd, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof(timeout)) < 0) {
        perror("setsockopt");
        exit(1);
    }

    // Send initial packets
    for (int port = lowport; port <= highport; port++) {
        destaddr.sin_port = htons(port);
        for (int i = 1; i <= 10; i++) {
            ret = sendto(sockfd, msg, total_len, 0, (struct sockaddr*)&destaddr, sizeof(destaddr));
            if (ret < 0) {
                perror("Error sending");    
            }
        }
    }

    // Get the local port the OS assigned to our socket
    struct sockaddr_in localaddr;
    socklen_t localaddrlen = sizeof(localaddr);

    if (getsockname(sockfd, (struct sockaddr *)&localaddr, &localaddrlen) < 0) {
        perror("getsockname");
        exit(1);
    }
    int source_port = ntohs(localaddr.sin_port);
        
    struct sockaddr_in srcaddr;
    char buffer[2048];
    int ret2;

    bool sigil_ready = false;
    bool guardian_answer = false;
    bool answer = false;
    
    while (true) {
        socklen_t srcaddrlen = sizeof(srcaddr);
        ret2 = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&srcaddr, &srcaddrlen);
        
        if (ret2 < 0) {
            if (errno == EAGAIN || errno == EWOULDBLOCK) break;
            perror("recvfrom");
            break;
        }
        
        int port = ntohs(srcaddr.sin_port);
        s = string(buffer, ret2);
     
        cout << port << " Received " << s << endl;

        if (port == 4048 && ret2 == 5){
            SECRET(sockfd, buffer, secret_num, srcaddr);
            sigil_ready = true;
        }   

        if (port == 4026 && sigil_ready && !guardian_answer){
            GUARDIAN(sockfd, buffer, ret2, srcaddr);
            guardian_answer = true;
        }

        if (port == 4017 && !answer){
            evil(ipaddr, port, source_port);
            answer = true;
        }
    }
    
    return 0;
}