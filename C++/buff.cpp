// #include <iostream>
// using namespace std;

// int main(){
//     int low,high,n;

//     low = 0;
//     high = 0;
//     for (int i = 1; i != 0; i *= 2){
//         cout << "buf[" << i << "]" << endl;
//         cin >> n;
//         if (n > 0 && n <= 255){
//             continue;
//         }
//         else if (n == 0){
//             high = i; 
//             low -= i;
//             break;
//         }
//     }
//     for (int i = high-1; i > low; i--){
//         cout << "buf[" << i << "]" << endl;
//         cin >> n;
//         if (n > 0 && n <= 255){ 
//             cout << "strlen(buf) = " << high << endl;
//             break;
//         }
//     }
// } 


#include <iostream>
using namespace std;


int main(){
    int l,h,n;

    for (int i = 1; i != 0; i *= 2) {

        cout << "buf[" << i << "]" << endl;
        cin >> n;

        if (n > 0 && n <= 255){
            continue;
        }

        else if (n == 0){
            h = i-1;
            l = i / 2;
            //cout << "strlen(buf) = " << i << endl;
            break;
        }
    }

    

    
}

