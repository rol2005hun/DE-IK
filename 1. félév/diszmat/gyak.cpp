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
//
// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;


int main() {
    for(int i = 1; i<= 9; i++) {
        if( (100000*i+60717) % 3 == 0) {
            cout << i << endl;
        }
    }

    return 0;
}
//
// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;


int main() {
    for(int j = 0; j<=9; j++) {
        for(int i = 0; i<= 9; i++) {
            if((440000+i*1000+830+j) % 88 == 0) {
                cout << i << endl;
                cout << j << endl;
            }
        }
    }

    return 0;
}
//
// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;


int main() {
    int t[11] = {-117,-134, 64,46,-107,-28, -60, 149, 106, 136};
    
    for(int i = 0; i<=9; i++) {
        if((t[i]-1)%15) cout << t[i] <<endl;
    }

    return 0;
}
