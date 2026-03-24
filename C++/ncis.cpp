#include <iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;


int main(){
    int l;
    cin >> l;

    vector<string> words(l);
    
    for (int i= 0; i < l; i++){
        cin >> words[i];
        
    }

    struct
    {
        bool operator()(string a, string b) const { return towlower(a) < towlower(b)} 
    }
    customeless;
    

    sort(words.begin(), words.end());

    for (int i = 0; i < l; i++){
        cout << words[i] << endl;
    }

}