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
using namespace std;

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
        
    struct sockaddr_in srcaddr;
    char buffer[2048];
    int ret2;
    
    while (true) {
        socklen_t srcaddrlen = sizeof(srcaddr);
        ret2 = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&srcaddr, &srcaddrlen);
        if (ret2 < 0) {
            if (errno == EAGAIN || errno == EWOULDBLOCK) break;
            perror("recvfrom");
            break;
        }
        int port2 = ntohs(srcaddr.sin_port);
        if (ret2 == 5){
            
            uint8_t g_id = buffer[0]; // Getting group Id 
            uint32_t c_net; 
            memcpy(&c_net, buffer + 1, 4); 
            uint32_t challenge = ntohl(c_net); // turning Network byte order to local
            uint32_t sigil = challenge ^ secret_num; // XOR secret num with local 
            uint32_t sigil_net = htonl(sigil); // turning local to Network byte

            unsigned char msg_b[5]; // making the buffer msg 
            msg_b[0] = g_id; // sending back the group id 
            memcpy(msg_b + 1, &sigil_net, 4); // with the XOR sigil

            destaddr.sin_port = htons(port2);

            int ret = sendto(sockfd, msg_b, 5, 0, (struct sockaddr*)&destaddr, sizeof(destaddr));
            if (ret < 0) perror("Error sending Sigil");

            // Port 1 4054
        }   

        s = string(buffer, ret2);
        int port = ntohs(srcaddr.sin_port);

        cout << port << " Received " << s << endl;
    }
};



    