#include <sys/socket.h>
#include <stdio.h>
#include <iostream>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <cstdlib>
#include <string>
#include <set>
#include <errno.h>
using namespace std;

// Array of char pointer and integer for how many arguments
int main(int argc, const char* argv[]) {
    const char *ipaddr = argv[1];
    int lowport = stoi(argv[2]);
    int highport = stoi(argv[3]);



    int sockfd;
    string s = "Hello \n";

    //creating the timeout structure for setsockopt()
    struct timeval timeout;
    timeout.tv_sec = 15;
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
    // if (inet_pint port2 = ntohs(srcaddr.sin_port);
    //     if (ret2 == 5){
            
    //         uint8_t g_id = buffer[0]; // Getting group Id 
    //         uint32_t c_net; 
    //         memcpy(&c_net, buffer + 1, 4); 
    //         uint32_t challenge = ntohl(c_net); // turning Network byte order to local
    //         uint32_t sigil = challenge ^ secret_num; // XOR secret num with local 
    //         uint32_t sigil_net = htonl(sigil); // turning local to Network byte

    //         unsigned char msg_b[5]; // making the buffer msg 
    //         msg_b[0] = g_id; // sending back the group id 
    //         memcpy(msg_b + 1, &sigil_net, 4); // with the XOR sigil

    //         destaddr.sin_port = htons(port2);

    //         int ret = sendto(sockfd, msg_b, 5, 0, (struct sockaddr*)&destaddr, sizeof(destaddr));
    //         if (ret < 0) perror("Error sending Sigil");

    //         // Port 1 4054
    //     }   ton(AF_INET, ipaddr, &destaddr.sin_addr) < 1) {
    //     std::cerr << "Invalid IP adress or address family: " << ipaddr << std::endl;
    //     exit(1);
    // }


    //setting socket option to receive timeout
    if (setsockopt(sockfd, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof(timeout)) < 0) {
        perror("setsockopt");
        exit(1);
    }

    //iteraring through all the ports in the range
    for (int port = lowport; port <= highport; port++) {
        destaddr.sin_port = htons(port); //formatting the port number from host byte order to network byte order

        for (int i = 1; i <= 10; i++) { //second iteration sending 10 UDP packets to each 
            ret = sendto(sockfd, s.c_str(), s.length(), 0, (struct sockaddr*)&destaddr, sizeof(destaddr));
            if (ret < 0) { //checking for errors while sending
            perror("Error sending"); 
            }      
        }
    }
    
    //creating structure for source address returned 
    struct sockaddr_in srcaddr;
    char buffer[2048];
    int ret2;



    //set<int> ports = {};
    
    // 2. Insertion

    //The while loop runs until the socket gets a timeout
    while (EAGAIN != errno && EWOULDBLOCK != errno){
        socklen_t srcaddrlen = sizeof(srcaddr);
        //checking for respond from the port and errors 
        ret2 = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&srcaddr, &srcaddrlen);
        if (ret2 == -1){
            perror("Error recieving");
        }


        else{
            //formatting back from network byte order to host byte order to be able to print out the host that responded
            int port = ntohs(srcaddr.sin_port);
            s = string(buffer, ret2);


            //if (ports.insert(port).second){
            cout << "Port " << port << s <<endl;
            //}
        }
    }
}




    