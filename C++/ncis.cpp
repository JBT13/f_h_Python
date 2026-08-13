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

    auto customless = [](const string& a, const string& b) {
        return lexicographical_compare(
            a.begin(), a.end(),
            b.begin(), b.end(),
            [](unsigned char c1, unsigned char c2) {
                return tolower(c1) < tolower(c2);
            }
        );
    };
    

    sort(words.begin(), words.end(),customless);

    for (int i = 0; i < l; i++){
        cout << words[i] << endl;
    }
}