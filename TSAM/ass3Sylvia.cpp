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

void SECRET(int sockfd, const char *buffer, u_int32_t secret_num, const struct sockaddr_in& address) {
    
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

    ip_header.ip_v = 4;
    ip_header.ip_hl = 5;
    ip_header.ip_tos = 0;
    ip_header.ip_len = sizeof(struct ip) + sizeof(struct udphdr) + sizeof(msg_b);
    ip_header.ip_id = 0;
    ip_header.ip_off = IP_RF; //evil bit
    ip_header.ip_ttl = 64;
    ip_header.ip_p = IPPROTO_UDP;
    

    
    inet_pton(AF_INET, ipaddr, &ip_header.ip_dst);

    ip_header.ip_sum = 0;
    ip_header.ip_sum = calculate_ip_checksum((uint16_t*)&ip_header, sizeof(struct ip));


    udp_header.uh_sport = htons(source_port);
    udp_header.uh_dport = htons(port);
    udp_header.uh_ulen = htons(sizeof(struct udphdr) + sizeof(msg_b));
    udp_header.uh_sum = 0;

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

};

int main(int argc, const char* argv[]) {
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

    for (int port = lowport; port <= highport; port++) {
        destaddr.sin_port = htons(port);
        for (int i = 1; i <= 10; i++) {
            ret = sendto(sockfd, msg, total_len, 0, (struct sockaddr*)&destaddr, sizeof(destaddr));
            if (ret < 0) {
            perror("Error sending");    
            }
        
        }
    }

    struct sockaddr_in localaddr;
    socklen_t localaddrlen = sizeof(localaddr);

    if (getsockname(sockfd, (struct sockaddr *)&localaddr, &localaddrlen) < 0) {
        perror("getsocknane");
        exit(1);
    }
    int source_port = ntohs(localaddr.sin_port);

        
    struct sockaddr_in srcaddr;
    char buffer[2048];
    int ret2;

    bool answer = false;
    
    while (true) {
        socklen_t srcaddrlen = sizeof(srcaddr);
        ret2 = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&srcaddr, &srcaddrlen);
        int port = ntohs(srcaddr.sin_port);
        if (ret2 < 0) {
            if (errno == EAGAIN || errno == EWOULDBLOCK) break;
            perror("recvfrom");
            break;
        }
            
        s = string(buffer, ret2);
     
        cout << port << " Received " << s << endl;

        if (port == 4048 && ret2 == 5){
            SECRET(sockfd, buffer, secret_num, srcaddr);
        }   

        if (port == 4017 && !answer){
            evil(ipaddr, port, source_port);
            answer = true;
    }
}

};



    