#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    vector<int> a(n);
    for(int &x : a) cin >> x;

    int maxh = -1, minh = 101;
    int max_idx = 0, min_idx = 0;
    for(int i = 0; i < n; i++) {
        if (a[i] > maxh) {
            maxh = a[i];
            max_idx = i;
        }
        if (a[i] <= minh) {
            minh = a[i];
            min_idx = i;
        }
    }

    int moves = max_idx + (n - 1 - min_idx);
    if (max_idx > min_idx) moves--;
    cout << moves << "\n";
    return 0;
}
