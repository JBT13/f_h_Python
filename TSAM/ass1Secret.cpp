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

/*
1. Generate a 32 bit secret number (and remember it for later)
2. Send me a message where the first byte is the letter 'S' followed by 4 bytes containing your secret number (in network byte order),
    and the rest of the message is a comma-separated list of the RU usernames of all your group members.
3. I will reply with a 5-byte message, where the first byte is your group ID and the remaining 4 bytes are a 32 bit challenge number (in network byte order)
4. Combine this challenge using the XOR operation with the secret number you generated in step 1 to obtain a 4 byte signature.
5. Reply with a 5-byte message: the first byte is your group number, followed by the 4-byte signature (in network byte order).
6. If your signature is correct, I will respond with a secret port number. Good luck!
7. Remember to keep your group ID and signature for later, you will need them for other ports. (But do not hard-code them!)

*/



// Array of char pointer and integer for how many arguments
int main(int argc, const char* argv[]) {
    const char *ipaddr = argv[1];
    int lowport = stoi(argv[2]);
    int highport = stoi(argv[3]);

    int sockfd;
    string s;
    uint32_t secret = 130306;
    string names = "jeremias25,sylviat24";
    char msg[256]; 

    msg[0] = 'S';
    msg[1] = (secret >> 24) & 0xFF;
    msg[2] = (secret >> 16) & 0xFF;
    msg[3] = (secret >> 8) & 0xFF;
    msg[1] = secret & 0xFF;

    strcpy(&msg[5], names.c_str());

    int total = 5 + names.length();

    //creating the timeout structure for setsockopt()
    struct timeval timeout;
    timeout.tv_sec = 30;
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

    //iteraring through all the ports in the range
    for (int port = lowport; port <= highport; port++) {
        destaddr.sin_port = htons(port); //formatting the port number from host byte order to network byte order

        for (int i = 1; i <= 10; i++) { //second iteration sending 10 UDP packets to each 
            ret = sendto(sockfd, msg, total, 0, (struct sockaddr*)&destaddr, sizeof(destaddr));
            if (ret < 0) { //checking for errors while sending
            perror("Error sending"); 
            exit(1);    
            }
        
        }
    }
    
    //creating structure for source address returned 
    struct sockaddr_in srcaddr;
    socklen_t srcaddrlen = sizeof(srcaddrlen);
    char buffer[2048];
    int ret2;

    //The while loop runs until the socket gets a timeout
    while (EAGAIN != errno && EWOULDBLOCK != errno){
        socklen_t srcaddrlen = sizeof(srcaddr);
        //checking for respond from the port and errors 
        ret2 = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&srcaddr, &srcaddrlen);
        if (ret2 == -1){
            perror("Error recieving");
            exit(1);
        }

        else{
            s = string(buffer, ret2); //creating a value for the received respond

            //formatting back from network byte order to host byte order to be able to print out the host that responded
            int port = ntohs(srcaddr.sin_port); 
            cout << "Port " << port << " Received "<< s << endl;
        }
    }
}



    
