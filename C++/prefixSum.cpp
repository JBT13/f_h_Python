#include <iostream>
#include<vector>
using namespace std;

int main(){
    int n,q;
    cin >> n;

    vector<int> arr(n);

    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }

    vector<int> prefix(n+1);

    for (int i = 0; i < n; i++){
        prefix[i + 1] = prefix[i] + arr[i];
    }

    cin >> q;

    for (int i = 0; i < q; i++){
        int l,r;
        cin >> l >> r;

        cout << prefix[r+1] - prefix[l] << endl;
    }
}