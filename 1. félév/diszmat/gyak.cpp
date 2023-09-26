// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
int lnko(int a, int b) { // ez az euklédiszi algoritmus, amely a legnagyobb közös osztót keresi
    if(b == 0) {
        return a;
    } else {
        return lnko(b, a % b);
    }
}

int x, k= 0;

int main() {
    int c = 0;
    for(int i = 1; i<= 88200; i++){
        if(88200%i==0) {
            c++;
            x = lnko(i, 110);
            if(x == 1) k++;
        }
    }
    
    cout << c << ' ' << k;

    return 0;
}
