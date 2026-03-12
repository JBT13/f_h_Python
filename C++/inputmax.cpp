#include <iostream>
using namespace std;

int main(){
    
    int n;
    cin >> n;
    int max;
    max = 0;

    for(int i = 0; i < n; i++){
        int a;
        cin >> a; 
        if (a > max){
            max = a;
        }
    }

    if (n > max){
        cout << n << endl;
    }
    else{
        cout << max <<endl;
    }
}