#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

int main(){
    int n, num, a;
    cin >> n;
    string name, final_name; 
    unordered_map<string, int> cribs;

    for(int i = 0; i < n; i++){
        cin >> name >> num;
        cribs[name] = num;
    }

    a = 0;
    for(const auto&[key, value] : cribs){
        if (value >= a){
            a = value;
            final_name = key;
        }
    }
    cout << final_name << endl;
}