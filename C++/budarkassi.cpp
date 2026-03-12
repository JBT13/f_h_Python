#include <iostream>
using namespace std;

int main(){
    int n, total;
    total = 0;
    cin >> n;
    
    for (int i = 0; i < n; i++ ){
        int s;
        cin >> s;
        total = total + s;
    }
    
    cout << total << endl;
}