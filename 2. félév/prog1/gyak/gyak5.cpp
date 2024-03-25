#include <iostream>
using namespace std;

bool szerk(double a, double b, double c) {
    if(a+b+c == 180) return true;
    else return false;
}

int main()
{
    cout << szerk(60,60,60);
}
