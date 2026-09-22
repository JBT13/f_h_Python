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
#include <netinet/ip6.h>
#include <netinet/udp.h>
#include <unistd.h>
using namespace std;

struct State{
    int secret_port = 0;
    int evil_port = 0;
    int guardian_port = 0;
    int dragon_port = 0;


    unsigned char msg_b[5];
    string guardian_spell;

    string secret_message;
    string evil_message;
    string guardian_message;
    string dragon_message;
};


set<int> udpscanner(const char *ipaddr, State state) {
    int lowport = 4000;
    int highport = 4100;
    
    
    int sockfd;
    string message = "Hello \n";

    //creating the timeout structure for setsockopt()
    struct timeval timeout;
    timeout.tv_sec = 2;
    timeout.tv_usec = 0;

    int ret;

    //creating the socket and checking for errors
    //creating the structure for destination address for the sendto function
    struct sockaddr_in destaddr;
    destaddr.sin_family = AF_INET;
    sockfd = socket(AF_INET, SOCK_DGRAM, 0); 
    if (sockfd < 0) {
        perror("Error creating socket");
        exit(1);
    }
    
    //converting the IP address from text format to network format
    //and checking for invalid address
    if (inet_pton(AF_INET, ipaddr, &destaddr.sin_addr) < 1) {
        std::cerr << "Invalid IP adress or address family: " << ipaddr << std::endl;
        exit(1);
    }


    //setting socket option to receive timeout
    if (setsockopt(sockfd, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof(timeout)) < 0) {
        perror("setsockopt");
        exit(1);
    }

    //creating the socket and checking for errors
    //creating the structure for destination address for the sendto function
    

    //iteraring through all the ports in the range
    for (int port = lowport; port <= highport; port++) {
        destaddr.sin_port = htons(port); //formatting the port number from host byte order to network byte order

         //second iteration sending 10 UDP packets to each 
        for (int i = 1; i <= 10; i++) { //second iteration sending 10 UDP packets to each 
            destaddr.sin_port = htons(port);
            ret = sendto(sockfd, message.c_str(), message.length(), 0, (struct sockaddr*)&destaddr, sizeof(destaddr));
            if (ret < 0) { //checking for errors while sending
            perror("Error sending"); 
            }      
        }
            
        usleep(10000); //evil port      
    }
    
    
    //creating structure for source address returned 
    struct sockaddr_in srcaddr;
    socklen_t srcaddrlen = sizeof(srcaddrlen);
    char buffer[2048];
    int ret2;



    set<int> ports = {};
    string s;
    // 2. Insertion

    //The while loop runs until the socket gets a timeout
    while (true) {
        socklen_t srcaddrlen = sizeof(srcaddr);
        ret2 = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&srcaddr, &srcaddrlen);
        if (ret2 < 0) {
            if (errno == EAGAIN || errno == EWOULDBLOCK) break;
            perror("recvfrom");
            break;
        }
       
        
            //formatting back from network byte order to host byte order to be able to print out the host that responded
        s = string(buffer, ret2);
        int port = ntohs(srcaddr.sin_port);

        ports.insert(port);

        if (s.find("Sacred Elder Cipher Relay for Enchanted Transmissions") < s.length()){
            state.secret_port = port;
            state.secret_message = string(buffer, ret2);
        }

        
        else if (s.find("evil") < s.length()){
            state.evil_port = port;
            state.evil_message = string(buffer, ret2);
        }
        
        
        else if (s.find("guardian") < s.length()){
            state.guardian_port = port;
            state.guardian_message = string(buffer, ret2);
        }
       
        else if (s.find("D.R.A.G.O.N") < s.length()){
            state.dragon_port = port;
            state.dragon_message = string(buffer, ret2);
        }
        
    }
    return ports;
}

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




void secret(const struct sockaddr_in& address, int sockfd, int port, State state){ //TODO: gera bool ekki void
    cout << "secret message: " << state.secret_message << endl;
    cout << "secret port: " << state.secret_port << endl;
    string secret_mes1;
    string secret_mes2;
    sockaddr_in destaddr = address;
    destaddr.sin_port = htons(port);
   
    struct sockaddr_in srcaddr;
    char buffer[2048];
    int ret2;
    socklen_t srcaddrlen = sizeof(srcaddr);
    string message = "Hello \n";
    
    for (int i = 0; i <= 5; i++){
        int ret1 = sendto(sockfd, message.c_str(), message.length(), 0, (struct sockaddr*)&destaddr, sizeof(destaddr));
            if (ret1 < 0) { //checking for errors while sending
            perror("Error sending"); 
            exit(1);
            }
        
        ret2 = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&srcaddr, &srcaddrlen);

        if (ret2 >= 0) {
            break;
        }
        if (errno == EAGAIN || errno == EWOULDBLOCK) continue;
        if (ret2 < 0) {
            perror("recvfrom");
            return;
        }
    }

    uint32_t secret_num = 130306;
    string secret = "S.E.C.R.E.T.:"; 
    string names = "jeremias25,sylviat24,thordish25";
    uint32_t secret_num_net = htonl(secret_num); // turning my secret number to network byte order
    
    char msg[256];
    size_t text_len = secret.length() + names.length(); 
    size_t total_len = text_len + sizeof(secret_num_net);
    memcpy(msg, secret.c_str(), secret.length());
    memcpy(msg + secret.length(), names.c_str(), names.length());
    memcpy(msg + text_len, &secret_num_net, sizeof(secret_num_net));

    
    int rett = sendto(sockfd, msg, total_len, 0, (const struct sockaddr*)&destaddr, sizeof(destaddr));
    if (rett < 0) {
        perror("Error sending");
        exit(1);
    }

    
    ret2 = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&srcaddr, &srcaddrlen);

    if (ret2 < 0) {
        perror("recvfrom");
        return;
    }
    secret_mes1 = string(buffer, ret2);
   
    //TODO: hafa ntohs(srcaddr.sin_port) í öllu


    state.msg_b[0] = buffer[0]; // Getting group Id 
    uint32_t c_net; 
    memcpy(&c_net, buffer + 1, 4); 
    uint32_t challenge = ntohl(c_net); // turning Network byte order to local
    uint32_t sigil = challenge ^ secret_num; // XOR secret num with local 
    uint32_t sigil_net = htonl(sigil); // turning local to Network byte

    memcpy(state.msg_b + 1, &sigil_net, 4); // with the XOR sigil
    int ret = sendto(sockfd, state.msg_b, 5, 0, (const struct sockaddr*)&destaddr, sizeof(destaddr));
    if (ret < 0) {
        perror("Error sending");
        exit(1);
    }
    int ret3 = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&srcaddr, &srcaddrlen);

    if (ret3 < 0) {
        perror("recvfrom");
        return;
    }
    secret_mes2 = string(buffer, ret3);
    cout << port << " Received " << secret_mes1 << endl;
    cout << port << " Received " << secret_mes2 << endl;
    return;
   
}

void evil(const char *ipaddr, int sockfd, int port, int source_port, State state) {
    cout << "evil message: " << state.evil_message << endl;
    cout << "evil port" << state.evil_port << endl;

    string evil_mes1;
    sockaddr_in destaddr ;
    destaddr.sin_port = htons(port);
   
    struct sockaddr_in srcaddr;
    char buffer[2048];
    int ret2;
    socklen_t srcaddrlen = sizeof(srcaddr);

    struct ip ip_header;
    struct udphdr udp_header;

    
    
    memset(&ip_header, 0, sizeof(ip_header));
    memset(&udp_header, 0, sizeof(udp_header));

    ip_header.ip_v = 4;
    ip_header.ip_hl = 5;
    ip_header.ip_tos = 0;
    ip_header.ip_len = sizeof(struct ip) + sizeof(struct udphdr) + sizeof(state.msg_b);
    ip_header.ip_id = 0;
    ip_header.ip_off = IP_RF; //evil bit
    ip_header.ip_ttl = 64;
    ip_header.ip_p = IPPROTO_UDP;
    

    
    inet_pton(AF_INET, ipaddr, &ip_header.ip_dst);

    ip_header.ip_sum = 0;
    ip_header.ip_sum = calculate_ip_checksum((uint16_t*)&ip_header, sizeof(struct ip));

    udp_header.uh_sport = htons(source_port);
    udp_header.uh_dport = htons(port);
    udp_header.uh_ulen = htons(sizeof(struct udphdr) + sizeof(state.msg_b));
    udp_header.uh_sum = 0;

    char packet[1024];

    memcpy(packet, &ip_header, sizeof(struct ip));
    memcpy(packet + sizeof(struct ip), &udp_header, sizeof(struct udphdr));
    memcpy(packet + sizeof(struct ip) + sizeof(struct udphdr), state.msg_b, sizeof(state.msg_b));

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

    destaddr.sin_family = AF_INET;
    destaddr.sin_port = htons(port);

    if (inet_pton(AF_INET, ipaddr, &destaddr.sin_addr) < 1) {
        std::cerr << "Invalid IP adress or address family: " << ipaddr << std::endl;
        exit(1);
    }

    size_t total_len = sizeof(struct ip) + sizeof(struct udphdr) + sizeof(state.msg_b);
    int ret = sendto(rawsocket, packet, total_len, 0, (struct sockaddr *)&destaddr, sizeof(destaddr));
    if (ret < 0) {
        perror("Error sending");
        exit(1);
    }


    ret2 = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&srcaddr, &srcaddrlen);

    if (ret2 < 0) {
        perror("recvfrom");
        return;
    }
    cout << port << " Received " << string(buffer, ret2) << endl;
    return;
};
void guardian(int sockfd, const char *buffer, const struct sockaddr_in& address, int port, int ret2, State state) {
    cout << "guardian message: " << state.guardian_message << endl;
    cout << "guardian port" << state.guardian_port << endl;
    struct sockaddr_in srcaddr;
    socklen_t srcaddrlen = sizeof(srcaddr);
    char guardian_mes[2048];

    struct ip6_hdr guardian_ip6;
    struct udphdr guardian_udp;

    memcpy(&guardian_ip6, buffer, sizeof(struct ip6_hdr));
    memcpy(&guardian_udp, buffer + sizeof(struct ip6_hdr), sizeof(struct udphdr));

    struct ip6_hdr ip6_header;
    struct udphdr udp_header;

    memset(&ip6_header, 0, sizeof(ip6_header));
    memset(&udp_header, 0, sizeof(udp_header));

    ip6_header.ip6_flow = guardian_ip6.ip6_flow; //útaf error
    ip6_header.ip6_src = guardian_ip6.ip6_dst;
    ip6_header.ip6_dst = guardian_ip6.ip6_src;
    ip6_header.ip6_vfc = IPV6_VERSION;
    ip6_header.ip6_plen = htons(sizeof(struct udphdr) + sizeof(state.msg_b));
    ip6_header.ip6_nxt = IPPROTO_UDP;
    ip6_header.ip6_hlim = 64;



    udp_header.uh_sport = guardian_udp.uh_dport;
    udp_header.uh_dport = guardian_udp.uh_sport;
    udp_header.uh_ulen = htons(sizeof(struct udphdr) + sizeof(state.msg_b));
    udp_header.uh_sum = 0;


    char checksum_buffer[100];
    int offset = 0;

    memcpy(checksum_buffer + offset, &ip6_header.ip6_src, sizeof(ip6_header.ip6_src));
    offset += sizeof(ip6_header.ip6_src);

    memcpy(checksum_buffer + offset, &ip6_header.ip6_dst, sizeof(ip6_header.ip6_dst));
    offset += sizeof(ip6_header.ip6_dst);

    uint32_t udp_len = htonl(sizeof(struct udphdr) + sizeof(state.msg_b));
    memcpy(checksum_buffer + offset, &udp_len, sizeof(udp_len));
    offset += sizeof(udp_len);

    checksum_buffer[offset++] = 0;
    checksum_buffer[offset++] = 0;
    checksum_buffer[offset++] = 0;
    checksum_buffer[offset++] = IPPROTO_UDP;

    memcpy(checksum_buffer + offset, &udp_header, sizeof(struct udphdr));
    offset += sizeof(struct udphdr);
    
    memcpy(checksum_buffer + offset, state.msg_b, sizeof(state.msg_b));
    offset += sizeof(state.msg_b);

    udp_header.uh_sum = calculate_ip_checksum((uint16_t*)checksum_buffer, offset);

    char packet[sizeof(struct ip6_hdr) + sizeof(struct udphdr) + sizeof(state.msg_b)];
    memcpy(packet, &ip6_header, sizeof(struct ip6_hdr));
    memcpy(packet + sizeof(struct ip6_hdr), &udp_header, sizeof(struct udphdr));
    memcpy(packet + sizeof(struct ip6_hdr) + sizeof(struct udphdr), state.msg_b, sizeof(state.msg_b));

    int ret = sendto(sockfd, packet, sizeof(packet), 0, (struct sockaddr*)&address, sizeof(address));

    if (ret < 0) {
        perror("Error sending");
        exit(1);
    }

    ret2 = recvfrom(sockfd, guardian_mes, sizeof(guardian_mes), 0, (struct sockaddr*)&srcaddr, &srcaddrlen);

    if (ret2 < 0) {
        perror("recvfrom");
        return;
    }
    cout << port << " Received " << string(guardian_mes, ret2) << endl; //evil er að prentast hérna


}

/*
void dragon(int sockfd, const struct sockaddr_in& address){

    string ports = "4054,4093"; //get ekki harðkóðað þetta breytist I think

    int ret = sendto(sockfd, ports.c_str(), ports.size(), 0, (struct sockaddr*)&address, sizeof(address));

    if (ret < 0) {
        perror("Error sending");
        exit(1);
    }


}
    
*/
/*
void dragon2(int sockfd, const struct sockaddr_in& address){
    int knock[] = {4093, 4054, 4054, 4054, 4093, 4093}; // ekki harðkóða

    for (int i = 0; i < 6; i++) {
        struct sockaddr_in knock_addr = address;
        knock_addr.sin_port = htons(knock[i]);

        char packet[1024];
        int offset = 0;

        memcpy(packet + offset, msg_b, sizeof(msg_b));
        offset += sizeof(msg_b);

        memcpy(packet + offset, guardian_spell.c_str(), guardian_spell.length());
        offset += guardian_spell.length();

        int ret = sendto(sockfd, packet, sizeof(packet), 0, (struct sockaddr*)&knock_addr, sizeof(knock_addr));

        if (ret < 0) {
            perror("Error sending");
            exit(1);
        }
    }
}

*/

int main(int argc, const char* argv[]) {
    const char *ipaddr = argv[1];
    int firstport = stoi(argv[2]);
    int secondport = stoi(argv[3]);
    int thirdport = stoi(argv[4]);
    int fourthport = stoi(argv[5]);

    set <int> arg_ports = {firstport, secondport, thirdport, fourthport};
    set <int> udp_result;
    int sort_port[] = {firstport, secondport, thirdport, fourthport};
    

    struct timeval timeout;
    timeout.tv_sec = 15;
    timeout.tv_usec = 0;

    struct State state;
    

    int sockfd;
    string s;

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



    
    
   

    //creating the timeout structure for setsockopt()
    
    
    int ret;

    //creating the socket and checking for errors
    //creating the structure for destination address for the sendto function
    

    //iteraring through all the ports in the range
    
    
   udp_result = udpscanner(ipaddr, state);


    if (arg_ports != udp_result){
        for (int port: udp_result) {
            cout << "Open ports: " << port << " ";
        }
        cout << endl;
        exit(1);
    }
    string message = "Hello \n";
    
    
    
    

    secret(destaddr, sockfd, state.secret_port, state);

    destaddr.sin_port = htons(state.evil_port);
    ret = sendto(sockfd, message.c_str(), message.length(), 0, (struct sockaddr*)&destaddr, sizeof(destaddr));
    if (ret < 0) { //checking for errors while sending
        perror("Error sending");
        exit(1); 
        }
    //fyrir evil
    struct sockaddr_in srcaddr;
    char buffer[2048];
    int ret2;
    socklen_t srcaddrlen = sizeof(srcaddr);

    ret2 = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&srcaddr, &srcaddrlen);

    if (ret2 < 0) {
        perror("recvfrom");
        exit(1);
    }
    struct sockaddr_in localaddr;
    socklen_t localaddrlen = sizeof(localaddr);

    if (getsockname(sockfd, (struct sockaddr *)&localaddr, &localaddrlen) < 0) {
        perror("getsocknane");
        exit(1);
    }
    
    int source_port = ntohs(localaddr.sin_port);

    evil(ipaddr, sockfd, state.evil_port, source_port, state);

    destaddr.sin_port = htons(state.guardian_port);
    for (int i = 0; i <= 5; i++){
        int ret1 = sendto(sockfd, message.c_str(), message.length(), 0, (struct sockaddr*)&destaddr, sizeof(destaddr));
            if (ret1 < 0) { //checking for errors while sending
            perror("Error sending"); 
            exit(1);
            }
        
        ret2 = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&srcaddr, &srcaddrlen);

        if (ret2 >= 0) {
            break;
        }
        if (errno == EAGAIN || errno == EWOULDBLOCK) continue;
        if (ret2 < 0) {
            perror("recvfrom");
            exit(1);
        }
    }
           
    guardian(sockfd, buffer, destaddr, state.guardian_port, ret2, state);

}

        //dragon(sockfd, srcaddr);


        //dragon2(sockfd, srcaddr);
    


       
        