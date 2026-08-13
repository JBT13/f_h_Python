#include <iostream>
#include <set>
#include <string>
using namespace std;

int main(){
    int c;
    set<string> bok;

    cin >> c;

    for (int i = 0; i < c; i++){
        char op;
        string name;
        cin >> op >> name; 

        if (op == '+'){
            bok.emplace(name);
        }

        else if (op == '-'){
            bok.erase(name);
        }

        else if (op == '?'){
            if (bok.contains(name)){
                cout << "Jebb" << endl;
            }
            else{
                cout << "Neibb" << endl;
            }
        }
    }


}