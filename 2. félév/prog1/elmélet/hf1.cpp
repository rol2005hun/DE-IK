#include <iostream>
using namespace std;

int fullProcessor(int a, int b) {
    int c = a * b;
    int d = c * c;
    return fullProcessor(c, d);
}

int main() {
    fullProcessor(2, 3);
    return 0;
}