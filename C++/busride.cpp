#include <iostream>
#include<vector>
using namespace std;

int main(){
    int n, sum, target, counter;
    cin >> n;

    vector<int> arr(n);

    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }

    sum = 0;
    for (int i = 0; i < n; i++){
        sum += arr[i];
    }
    

    if (sum % 3 != 0){
        cout << -1 << endl;
        return 0;
    }


    target = sum / 3;
    counter = 0;
    vector<int>  bus; 

    for (int i = 0; i < n; i++){
        counter += arr[i];

        if (counter == target){
            bus.push_back(i + 1);
            counter = 0;
        }
        else if (counter > target){
            cout << -1 << endl;
            return 0;
        }
    }

    if (bus.size() == 3){
        cout << bus[0] << " " << bus[1] << endl;
    }
    else{
        cout << -1 << endl;
    }
}

