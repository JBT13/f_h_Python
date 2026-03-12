#include <iostream>
using namespace std;

string func1(int n){
    string text;  

    for (int i = 0; i < n; i++){
        text.append("-");
    }

    return string("+") + text + string("+");
}

string func2(int n){
    string text; 

    for (int i = 0; i < n; i++){
        text.append(" ");
    }

    return "|" + text + "|";
}

int main(){
    int n;
    cin >> n;

    if (n == 0){
        cout << "++" << endl;
        cout << "++" << endl;
    }

    else {
        cout << func1(n) << endl;
        for (int i = 0; i < n; i++){
            cout << func2(n) << endl;
        }
        cout << func1(n) << endl;
    }
}

