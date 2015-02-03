#include <vector>
#include<iostream>
using namespace std;

int main() {
    vector<int> v;
    for(int i = 0; i <= 1000; i++) {
        v.push_back(i);
    }
    cout<<v.size();
    return 0;
}
