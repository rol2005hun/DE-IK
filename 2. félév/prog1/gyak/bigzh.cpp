#include <iostream>
using namespace std;

int randomfeltolt(int* arr) {
    srand(time(NULL));
    for(int i = 0; i < sizeof(arr); i++) {
        arr[i] = rand() % 100;
    }
    return 0;
}

int parosokosszege(int* arr) {
    int sum = 0;
    for(int i = 0; i < sizeof(arr); i++) {
        if(arr[i] % 2 == 0) {
            sum += arr[i];
        }
    }
    return sum;
}

struct mynode {
    string nev;
    int eletkor;
    mynode* next;
};

mynode* hozzaadas(mynode* fej, string nev, int eletkor) {
    mynode* uj = new mynode;
    uj -> nev = nev;
    uj -> eletkor = eletkor;
    uj -> next = NULL;

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

string legidosebbnode(mynode* fej) {
    mynode* temp = fej;
    int max = 0;
    string nev;
    while(temp != NULL) {
        if(temp -> eletkor > max) {
            max = temp -> eletkor;
            nev = temp -> nev;
        }
        temp = temp -> next;
    }
    return nev;
}

mynode* novekvobeszur(mynode* fej, string nev, int eletkor) {
    mynode* uj = new mynode;
    uj -> nev = nev;
    uj -> eletkor = eletkor;
    uj -> next = NULL;

    if(fej == NULL || eletkor < fej -> eletkor) {
        uj -> next = fej;
        fej = uj;
        return fej;
    }

    mynode* temp = fej;
    while(temp -> next != NULL) {
        if(temp -> next -> eletkor > uj -> eletkor) {
            uj -> next = temp -> next;
            temp -> next = uj;
            return fej;
        }
        temp = temp -> next;
    }
    temp -> next = uj;
    return fej;
}

int main() {
    // 1. feladat
    cout << "- 1. feladat -" << endl;
    int* arr = new int[10];
    randomfeltolt(arr);
    cout << "Tomb elemei: ";
    for(int i = 0; i < sizeof(arr); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // 2. feladat
    cout << "- 2. feladat -" << endl;
    cout << "Parosok osszege: " << parosokosszege(arr) << endl;

    // 3. feladat
    cout << "- 3. feladat -" << endl;
    mynode* fej = NULL;
    fej = hozzaadas(fej, "Eva", 21);
    fej = hozzaadas(fej, "Bela", 23);
    fej = hozzaadas(fej, "Adam", 25);
    mynode* temp = fej;
    while(temp != NULL) {
        cout << temp -> nev << " ";
        cout << temp -> eletkor << endl;
        temp = temp -> next;
    }

    // 4. feladat
    cout << "- 4. feladat -" << endl;
    cout << "Legidosebb ember: " << legidosebbnode(fej) << endl;

    // 5. es 6. feladat
    cout << "- 5. es 6. feladat -" << endl;
    fej = novekvobeszur(fej, "Lakatos", 20);
    fej = novekvobeszur(fej, "Pista", 24);
    fej = novekvobeszur(fej, "Jozsi", 26);
    mynode* temp2 = fej;
    while(temp2 != NULL) {
        cout << temp2 -> nev << " ";
        cout << temp2 -> eletkor << endl;
        temp2 = temp2 -> next;
    }

    // felszabaditas a vegere
    mynode* akt = fej;
    while(akt != NULL) {
        mynode* temp3 = akt -> next;
        free(akt);
        akt = temp3;
    }
    
    return 0;
}
