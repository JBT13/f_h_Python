#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    //upper_bound = (g) -> g < v[g] 
    //lower_bound = (g) -> g <= v[g]

    vector<int> t{1,2,3,4,5,6,7,18,19};

    int v = *upper_bound(t.begin(),t.end(), 7);

    cout << v << endl;
}   