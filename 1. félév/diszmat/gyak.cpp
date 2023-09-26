#include <iostream>
using namespace std;
int main() {
    int c = 0;
    for(int i = 1; i<= 88200; i++){
        if(88200%i==0) {
            c++;
        }
    }
    
    cout << c;

    return 0;
}
