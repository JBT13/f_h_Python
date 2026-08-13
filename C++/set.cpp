#include <iostream>
#include <set>
using namespace std;

int main(){
    set<int> s;
    s.emplace(1);
    s.emplace(2);

    for (int i : s) {
        cout << i << endl;
    }

    // O(log n) IN C++ 
    s.erase(1);

    for (int i : s){
        cout << i << endl;
    }
}