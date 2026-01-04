#include <bits/stdc++.h>
using namespace std;

int arr[20000001];
int n;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    while(n--) {
        int t;
        cin >> t;
        arr[t + 10000000]++;
    }

    int k;
    cin >> k;
    while(k--) {
        int q;
        cin >> q;
        cout << arr[q + 10000000] << " ";
    }

    return 0;
}
