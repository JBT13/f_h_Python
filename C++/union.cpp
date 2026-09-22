#include <iostream>
#include<vector>

using namespace std;

struct union_find {
    vector<int> parent, sizes;
    union_find(int n) : parent(n), sizes(n,1) {
        for (int i = 0; i < n; i++) {
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

int main() {
    int n, m, a, b;
    cin >> n >> m;
    union_find uf(n);
    
    for (int i = 0; i < m; i++){
        cin >> a >> b;
        uf.unite(a,b);    
    }

    for (int i = 0; i < n; i++){
        cout << uf.find(i) << " "; // þetta er fyrir the freaking set LEADER 
        // cout << uf.parent[i] << " "; 
        // þetta er bara fyrir the parent þannig eg myndi ekki fa rett svar
    }
    cout << endl;

    return 0;
}