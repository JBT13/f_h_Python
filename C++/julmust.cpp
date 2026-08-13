#include <iostream>
#include <string>
using namespace std;

int main() {

    int r, mid;
    string text;
    cin >> r;
    mid = r / 2;

    cout << mid << endl;

    for (int i = 1; i < 86; i++) {
        cin >> text;

        if (text == "less") {
            cout << mid-1 << endl;
            r = mid-1 * i;
        }

        else if (text == "less") {
            cout << mid+1 << endl;
            mid = mid+1 * i;
        } 

        else if (text == "exact"){
            return 0;
        }
    }
}