#include <iostream>
using namespace std;

void svap(int *a, int *b) {
    swap(a, b);
    cout << *a;
}

int main() {
    int* t = new int[3];
    int parosok = 0;
    int parosindex;
    srand(time(NULL));
    for(int i = 0; i <= sizeof(t); i++) {
        t[i]=rand() % 100;
        if(t[i] % 2 == 0) {
            parosok+=t[i];
            parosindex++;
        }
    }

    for(int i = 0; i <= sizeof(t); i++) {
        cout << t[i] << endl;
    }

    if(parosok == 0) {
        cout << "nincs atlag";
    } else cout << "atlag: " << parosok / parosindex << endl;
    free(t);
    int x = 10;
    int y = 12;
    svap(&x, &y);
    cout << x;

    // tipus kenyszerites, mas szoval kasztolas
    // szintaxis (tipus)valtozo
    // a valtozot atkenyszeriti a megadott tipusra
    // int* ez egy tipus, int-re muatato pointer tipus
    // *a jelentese: indirekt hivatkozas
    // a: amire mutat
}
