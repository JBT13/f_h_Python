# Assignment 1 TSAM UDP Port Scanner

## Overview

The code sends multiples UDP packets to each port within a specific range from lowport ot highport then listen for responds and saves the unique ports numbers that got respond from

## Prerequisites 

To compile and run this project you need:
+ A C++ compiler (g++ or clang++)

Compile the source file "g++":
g++ name_file -o main
And run it:
./main IP LowPort Highport

# HOW IT WORKS

Socket initialization: Creates a UDP socket and configures a receive timeout
Packet transmission: Iterates through the specified port range and sends 10 UDP packets to each target port
Listening: listens for response via recvfrom(), converts port numbers from network byte order to host byte order and stores unique active ports using a set

# POSTDATA
When you are creating the socket depending if you are on linux or mac you have to change the internet domain in my case is AF_INET for IPv4 Internet Protocol in Mac its PF_INET