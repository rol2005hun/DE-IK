#include <iostream>
using namespace std;

/*
    egyirányban láncolt lista
    egy egyirányban láncolt lista láncszemekből áll
    egy láncszem tartalmaz
    - értékes adatot
    - a következő láncszemre mutató pointert
    egy láncszem az gy rekord, rekordot a struct kulcsszóval lehet létrehozni
*/

struct mynode {
    int szam;
    mynode* next; // a mext mutat a következő láncszemre
};

/*
    az egy irányba láncol listának van feje
    a fej a láncszemre mutat
    az üres listában nincs egy láncszem se, iyenkor a fej NULL
*/

// beszúrás a láncolt lista végén
mynode* beszur(mynode* fej, int adat) {
    mynode* uj = (mynode*)malloc(sizeof(mynode));
    uj -> szam = adat;
    uj -> next = NULL;

    // elgyaloglok a végére és a végére láncolom be
    // ha a lista üres, azaz a fej NULL
    if(fej == NULL) {
        fej = uj;
        return fej;
    }
    mynode* temp = fej;
    while(temp -> next != NULL) {
        temp = temp -> next;
    }
    temp -> next = uj;
    return fej;
}

mynode* beszure(mynode* fej, int adat) {
    // létrehozom az újat
    // szépen beállítom a szám és a next részét
    // úgy kell beláncolni, lásd tábla

    mynode* uj = (mynode*)malloc(sizeof(mynode));
    uj -> szam = adat;
    uj -> next = fej;
    fej = uj;
    return fej;
}

int main() {
    mynode* fej = NULL; // a legelső láncszemre mutat

    fej = beszure(fej, 5);
    fej = beszure(fej, 8);
    fej = beszure(fej, 3);
    fej = beszure(fej, 12);

    // mynode* uj = (mynode*)malloc(sizeof(mynode));
    // uj -> szam = 5; // pointeren keresztül mező hivatkozás
    //                 // minősítő jel: ->
    //                 // pointerneve -> mezőneve
    // uj -> next = NULL;
    // fej = uj;

    // uj = (mynode*)malloc(sizeof(mynode));
    // uj -> szam = 8;
    // uj -> next = NULL;
    // fej -> next = uj;

    // uj = (mynode*)malloc(sizeof(mynode));
    // uj -> szam = 3;
    // uj -> next = NULL;
    // fej -> next -> next = uj;

    // uj = (mynode*)malloc(sizeof(mynode));
    // uj -> szam = 12;
    // uj -> next = NULL;
    // fej -> next -> next -> next = uj;

    // mynode elso;
    // elso.szam = 5; // minősítő jel: pont
    //                // mező hivatkozás: rekordneve.mezőneve
    // mynode masodik;
    // masodik.szam = 8;
    // mynode harmadik;
    // harmadik.szam = 3;
    // mynode negyedik;
    // negyedik.szam = 12;
    // fej = &elso;
    // elso.next = &masodik;
    // masodik.next = &harmadik;
    // harmadik.next = &negyedik;
    // negyedik.next = NULL;

    // egyirányba láncolt listát while ciklussal dolgozok fel
    mynode* temp = fej;
    // a temppel végig megyek a listán, egészen addig amíg NULL nem lesz
    while(temp != NULL) {
        cout << temp -> szam << endl;
        temp = temp -> next;
    }

    mynode* akt = fej;
    while(akt != NULL) {
        mynode* temp3 = akt -> next;
        free(akt);
        akt = temp3;
    }

    return 0;
}
