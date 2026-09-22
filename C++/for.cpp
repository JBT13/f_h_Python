#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main(){
    int n, count;

    count = 0;
    cin >> n;
    for (int i = n; i > 0; i /= 2){
        count++;         
    }
    cout << count << endl;

}