#include <iostream>
#include <string> 
using namespace std;

string top(int n){
    string bars(n, '-');

    return "+" + bars + "+" ;
}

int main(){
    int n;    
    cin >> n;
    if (n > 0){
        string empt(n, ' '); 
        cout << top(n) << endl;
        for (int i = 0; i < n; i++){
            cout << "|" << empt << "|" << endl;
        }
        cout << top(n) << endl;
    }
    else{
        cout << "++" << endl;
        cout << "++" << endl;
    }
    
}