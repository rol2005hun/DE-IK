#include <iostream>
using namespace std;

/*
    A(0)=5
    A(n)=A(n-1)*2, ha n > 0
    Feladat: készíts olyan rekurzív fv-t, ami ennek a sorozatnak, az n-edik elemét számolja ki
*/

int elso(int n) {
    if(n == 0) return 5;
    return elso(n - 1) * 2;
}

int main() {
    cout << elso(5);
    return 0;
}
