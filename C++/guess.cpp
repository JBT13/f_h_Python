#include <iostream>
using namespace std;

int main(){
    int l,h,m;
    l = 1;
    h = 1000;

    while (l <= h){
        m = (l + h) / 2;

        cout << m << endl;

        string answer;

        cin >> answer; 

        if (answer == "lower"){
            h = m - 1;
        }
        else if(answer == "higher"){
            l = m + 1;
        }
        else{
            return 0;
        }
    }
}
