#include <iostream>
using namespace std;

void f() {
    f();
}

void f2(int i) {
    if(i == 0) return;
    cout << i << " ";
    f2(--i);
}

int osszead(int x, int* c) {
    if(x == 0) return *c;
    cin >> x;
    *c = *c + x;
    return osszead(x, c);
}

void ossezadv(int x, int* c) {
    if(x == 0) return;
    cin >> x;
    *c = *c + x;
    osszead(x, c);
}

int fact(int n) {
    if(n == 0) return 1;
    return n * fact(n - 1);
}

int main() {
    /*
        literáció = ciklus
        C alapú prog. nyelvekben 3 ciklus szervező utasítás van:
        - for (előírt lépésszámú ciklus)
        - while (elől tesztelő ciklus)
        - do-while (hátul tesztelő ciklus)
        
        üres ciklus: olyan ciklus, aminek a törzse sose fut le
        hátúl tesztelővel nem lehet üres ciklust írni, mivel egyszer garantáltan lefut
        végtelen ciklus: a teszt mindig igaz, ezért mindig meghívódik a törzs
    */
    // végtelen ciklus:

    // while(true) {}
    // for(;true;) {}
    // do {} while(true);

    // feladat: addig add össze számokat, amíg a szám nem 0
    // int c = 0;
    // int x;

    // do {
    //     cin >> x;
    //     c += x;
    // } while(x != 0);

    // cout << c;

    /*
        a rekurzió és a ciklus egyenértékű programozói eszközök
        amit meg lehet oldani ciklussal, azt rekurzióval is
        egy fv-t rekurzív fv-nek nevezek ha önmagát hívja
        tipikus eset: kocsmára nyílik a kocsma ajtó ?? nem utcára??
        nagyon könnyű végtelen rekurziót írni ugyan akkor, nem fut végtelen ideig, mert betelik a stack
        minden hívás előtt a rendszer lementi az összes lokális változót és regiszterek méretet
        végtelen rekurziót lehet írni, de végtelen sokáig futót nem
        ahhoz h a rekurzió ne legyen végtelen, kell egy ú.n bázis feltétel
        a bázis feltétel egyik ága rekurzív, másik ága nem
        i-- jelentése: először használd fel az értékét, utána csökkentsd
    */

    // f2(10);

    // feladat: olvass be számokat amíg 0-t nem kapsz, add össze a számokat
    // int-el:
    // int x;
    // cin >> x;
    // int c = x;
    // cout << osszead(x, &c);
    // void-al:
    // int x;
    // cin >> x;
    // int c = x;
    // osszead(x, &c);
    // cout << c;

    /*
        rekurzió akkumulátorral
        az akkumulátor olyan paraméten, ahol az utolsó részeredmény az eredmény
    */

    cout << fact(5);
    return 0;
}
