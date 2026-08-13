#include <iostream>
#include <cmath>
using namespace std;

int main(){
    double x,y,r1,r2,l_p,s_p,z;

    cin >> x;
    cin >> y;
    cin >> z;

    r1 = x / 2;
    r2 = y / 2;
    
    l_p = r1*r1;
    s_p = z*r2*r2;

    if (s_p >= l_p){
        cout << "Jebb" << endl;
    }

    else{
        cout << "Neibb" << endl;
    }

}