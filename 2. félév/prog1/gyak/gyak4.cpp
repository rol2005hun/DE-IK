#include <iostream>
using namespace std;

int main()
{
    int *t = new int[10];
    int x;
    cin >> x;
    for (int i = 0; i < 10; i++) {
        cin >> t[i];
    }
    bool talalt = false;
    for (int i = 0; i < 10; i++) {
        if (t[i] == x) {
            talalt = true;
            break;
        }
    }
    if (talalt) cout << "talaltam";
    else cout << "nem";
    free(t);
}
