#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    float x,y,z, min, max;
    char d;
    cin >> x >> d >>  y >> z;

    min = (x * 1) + z;
    max = (x * y) + z;

    float avg = (min + max) / 2;

    cout << avg << endl;
}