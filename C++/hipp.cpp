#include <iostream>
using namespace std;

int main(){
    string text;
    int n;
    cin >> text;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cout << "Hipp hipp hurra, " << text << "!" << endl;
    }
}