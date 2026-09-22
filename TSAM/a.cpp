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

int main(){
    string s;
    uint32_t secret_num = 130306;
    string names = "jeremias25,sylviat24,thordish25";
    string secret = "S.E.C.R.E.T.:";
    char msg[256] = {0}; 

    // msg[0] = 'S';
    // msg[1] = (secret >> 24) & 0xFF;
    // msg[2] = (secret >> 16) & 0xFF;
    // msg[3] = (secret >> 8) & 0xFF;
    // msg[4] = secret & 0xFF;

    string final = secret + names;

    // memcpy(msg, "S.E.C.R.E.T.:", 13);
    // memcpy(msg+13, &names, sizeof(names));
    memcpy(msg, &secret_num, sizeof(secret_num));

    final.append(msg, 4);

    cout << final.size() << endl;

}