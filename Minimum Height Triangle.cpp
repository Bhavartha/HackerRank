#include <bits/stdc++.h>

using namespace std;

int lowestTriangle(int base, int area){
    int ans = 2*area%base==0?0:1;
    return  ans+ 2*area/base;
}

int main() {
    int base;
    int area;
    cin >> base >> area;
    int height = lowestTriangle(base, area);
    cout << height << endl;
    return 0;
}
