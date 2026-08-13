#include <iostream>
#include<vector>
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

int main(){
    map<string, int> dic;
    vector<int> ls;
    int n, k,num,num2;
    string s, s2;
    cin >> n;

    for(int i = 0; i < n; i++){
        cin >> s >> num;
        dic.emplace(s,num);
    }
    
    cin >> k;

    for(int i = 0; i < k; i++){
        cin >> s2 >> num2;
        if (dic[s2])

    }

}