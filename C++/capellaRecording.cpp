#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n,d,record,value,count; 
    cin >> n >> d; 

    vector<int> arr(n);


    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());
    value = arr[0];

    // cout << value << endl;
    count = 0;
    for (int i = 0; i < n; i++){
        if (arr[i]- value <= d){
            continue;
        }
        else{
            value = arr[i];
            count += 1;
        }
    }
    cout << count + 1 << endl;
}


 