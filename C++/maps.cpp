#include <iostream>
#include <map>

using namespace std;

int main(){
    // map = dict

    map<string, int> a;

    a.emplace("abc", 10); //key value
    a["b"] = 10;

    for (pair<string, int> i : a){
        cout << i.first << " " << i.second << endl;
    }

    cout << a["abc"] << endl;

    // cout << a.contains("b") << endl; // returns true if its 

    // -std=c++20 to compile if it dont recognise
}