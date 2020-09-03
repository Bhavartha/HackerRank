#include <bits/stdc++.h>

using namespace std;

bool isSorted(vector<int> &arr){
    for(int i=1;i<arr.size();i++)
        if(arr[i]<arr[i-1]) return false;
    return true;
}

int main()
{
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i=0;i<n;i++)
        cin>>arr[i];
    if(isSorted(arr)){
        cout<<"yes";
        return 0;
    }
    int a,b;
    for(a=0;a<arr.size() && arr[a]<=arr[a+1];a++);
    for(b=arr.size()-1;a>=0 && arr[b]>=arr[b-1];b--);
    int aa=a+1,bb=b+1;
    swap(arr[a++],arr[b--]);
    if(isSorted(arr)){
        cout<<"yes\nswap "<<aa<<" "<<bb;
        return 0;
    }
    while(a<b) swap(arr[a++],arr[b--]);
    if(isSorted(arr)){
        cout<<"yes\nreverse "<<aa<<" "<<bb;
        return 0;
    }
    cout<<"no";
}
