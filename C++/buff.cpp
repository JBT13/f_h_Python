#include <iostream>
using namespace std;

int main(){
    long l,h,n,m;

    for (long i = 2; i != 0; i *= 2) {
                cout << "buf[" << i << "]" << endl;


        cin >> n;
        
        // if (c % 10 == 0) {
        //     cout << c << endl;
        // }
        if (n) {
            continue;
        }

        h = i;
        l = i / 2;
            //cout << "strlen(buf) = " << i << endl;
        break;
    }

    while (abs(h - l) != 1 ){
        m = (h - l) / 2 + l;

        cout << "buf[" << m << "]" << endl;
        cin >> n;

        if (n) {
            l = m;
        }
        else {
            h = m; 
        }
    }

    cout << "strlen(buf) = " << h << endl;
}
