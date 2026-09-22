#include <iostream>
#include<vector>
#include<string>

using namespace std;

struct union_find {
    vector<int> parent, sizes;
    union_find(int n) : parent(n+1), sizes(n+1,1){
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
            sizes[i] = 1;
        }
    }

    int find(int x) {
        if(parent[x] == x) return x;
        return parent[x] = find(parent[x]);
        }

    void unite(int x, int y) {
        int main_x = find(x);
        int main_y = find(y);

        if (main_x != main_y){
            if (main_x < main_y){
                parent[main_y] = main_x;
                sizes[main_x] += sizes[main_y];
            }

            else{
                parent[main_x] = main_y;
                sizes[main_y] += sizes[main_x];
            }
        }

    }
};

int main(){
    int n, q; 
    cin >> n >> q;

    union_find uf(n+1);

    for(int i = 0; i < q; i++){
        int a;
        cin >> a;
        if (a == 2){
            int b; 
            cin >> b; 
            cout << uf.sizes[uf.find(b)] - 1 << endl;    
        }
        else{
            int b,c;
            cin >> b >> c;
            uf.unite(b,c);
        }
    }
}