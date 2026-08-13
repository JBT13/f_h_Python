#include <bits/stdc++.h>

using namespace std;

using int_t = int64_t;
const int_t INF = 1l << 62l; // 2**63

// root = 1
// left_child(n) = 2 * n
// right_child(n) = 2 * n + 1
struct SegTree {
    int n;
    vector<int_t> tree;

    // Takes in initial values
    SegTree(const vector<int_t> &a): n(a.size()), tree(4 * n) {
        build(1, 0, n-1, a);
    }

    void build(int node, int l, int r, const vector<int_t> &a) {
        if (l == r) {
            tree[node] = a[l];
            return;
        }

        int mid = (l + r) / 2;
        // build left child
        build(2*node, l, mid, a);
        // build right child
        build(2*node+1, mid + 1, r, a);
        tree[node] = min(tree[2*node], tree[2*node + 1]); // Operation
    }

    void update(int node, int l, int r, int i, int_t val) {
        if (l == r) {
            tree[node] = val;
            return;
        }

        int mid = (l + r) / 2;

        if (i <= mid) update(2 * node, l, mid, i, val);
        else update(2 * node + 1, mid + 1, r, i, val);
        tree[node] = min(tree[2 * node], tree[2 * node + 1]); // Operation
    }

    int_t query(int node, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return INF; // Identity
        if (ql <= l && qr >= r) return tree[node];

        int mid = (l + r) / 2;
        return min(query(2 * node, l, mid, ql, qr),
               query(2 * node + 1, mid + 1, r, ql, qr)); // Operation
    }

    void update(int i, int_t val) { update(1, 0, n-1, i, val); }
    int_t query(int ql, int qr) { return query(1, 0, n-1, ql, qr); }
};

int main() {
    SegTree listi(); 

}