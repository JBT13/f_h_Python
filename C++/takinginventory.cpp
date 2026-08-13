#include <iostream>
#include <map>
#include <cmath>
using namespace std;

int main(){
    int n;
    cin >> n;

    map<string, int> items;

    // O(n * log(n))

    for (int i = 0; i < n; i++){
        string item; 
        int x; 
        cin >> item >> x; 
        
        items[item] += x;
    }

    // O(n * log(n))
    for (pair<string, int> i: items){
        int stack =  (i.second + 63) / 64; 
        cout << i.first << " " << stack << endl;
    }
}
