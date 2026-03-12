#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(){
    string words;
    getline(cin, words);

    stringstream ss(words);
    string word;
    string last; 

    while (ss >> word){
        last = word;
    }

    if (!last.empty()){
        cout << last << "slop" << endl;
    }

}
