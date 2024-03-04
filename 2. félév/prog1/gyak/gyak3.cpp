#include <iostream>
using namespace std;

int main()
{
    // ciklus:
    // -előltesztelő: ezen belül előírt lépésszámú: for
    // -hátulteszteő
    // for ciklus szintaxisa:
    // for(init; teszt; léptetés) { ciklus mag }
    // init: utasítás, de gyakran változó deklarálás
    // teszt: igaz/hamis kifejezés
    // léptetés: utasítás, de gyakran a ciklus változó léptetése
    // for ciklus szemantikája:
    // 1. init
    // 2. teszt
    // 3. ciklus mag
    // 4. léptetés
    // 5. ugrás a tesztre
    // addig fut a ciklus mag, amíg a teszt igaz, ha hamis akkor
    // a for utáni első utasítás következik
    // i++ ugyan az, mintha ezt írnám

   /* for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5 - i; j++) {
            cout << " ";
        }

        for (int j = 0; j < i * 2 - 1; j++) {
            cout << "*";
        }

        cout << endl;
    }*/

    /*for (int i = 0; i < 6; i++) {
        if (i <= 3) {
            for (int j = 0; j < 5 - i; j++) {
                cout << " ";
            }

            for (int j = 0; j < i * 2 - 1; j++) {
                cout << "*";
            }
        }
        else {
            for (int j = 0; j < i - 1; j++) {
                cout << " ";
            }

            for (int j = 0; j < i - j * 2; j++) {
                cout << "*";
            }
        }

        cout << endl;
    }*/

    // tömb szintaxisa
    // tömb_típusa tömb_neve[] = tömb kezdő értéke
    // a tömb homogén adatszerkezet
    // a C alapú nyelvekben a tömb 0-tól indexelődik

    /*int t[3] = { 0, 2, 4 };
    for (int i = 0; i < size(t); i++) {
        cout << t[i] << endl;
    }
    string nevek[] = { "a", "b", "c" };
    for (int i = 1; i < size(nevek) - 1; i++) {
        cout << nevek[i-1] << endl;
        cout << nevek[i] << endl;
        cout << nevek[i + 1] << endl;
    }*/

    int t[] = { 1, 2, 3 };

    // a tömb neve az egy pointer, méghozzá a tömb 0. elemére mutat
    // p - pointer
    // *p - a p által mutatott memória helyen lévő érték
    // pointer aritmetika, a pointereket lehet léptetni
    *t = 5;
    int* p = t + 1;
    int x = 15;
    int* px = &x;
    // a memória két részből áll: stack(verem) és heap(halom)
    // stack - lokális változók helye
    // heap - a dinamikus változók helye
    int* pointer = NULL;
    // ha létrehozok egy pointert, annak a kezdőértéke NULL
    /*cout << *px;*/
    /*pointer = (int*)malloc(5 * sizeof(int));*/
    /*pointer = new int[5];
    pointer[0] = 1;
    pointer[1] = 1;
    pointer[2] = 1;
    pointer[3] = 1;
    pointer[4] = 1;
    free(pointer);*/
    int *tomb = new int[5];
    for (int i = 0; i < 5; i++) {
        tomb[i] = rand();
    }
    for (int i = 0; i < 5; i++) {
        cout << tomb[i]<<endl;
    }
    free(tomb);
}
