#include <iostream>
#include<vector>
#include<string>

using namespace std;

struct union_find {
    vector<int> parent, sizes;
    int count = 0;
    union_find(int n) : parent(n), sizes(n,1){
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
                count;
            }

            else{
                parent[main_x] = main_y;
                sizes[main_y] += sizes[main_x];
            }
        }

    }
};

int main(){
    int n, m, a, b;
    string t;

    cin >> n >> m; 

    union_find uf(n);

    for(int i = 0; i < m ; i++){
        cin >> t;
        if (t == "LEGAL"){
            cin >> a;
            cout << uf.find(a) << endl;
        }

        else{
            cin >> a >> b;
            uf.unite(a,b);
        }
    }
}