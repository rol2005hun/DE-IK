#include <iostream>

using namespace std;

struct mynode {

    string nev;

    int eletkor;

    mynode* next; // a next mutat a következő láncszámra

};

mynode* beszur_vegen(mynode* fej, string nev, int eletkor) {

    mynode* uj = new mynode;

    uj->nev = nev;

    uj->eletkor = eletkor;

    uj->next = NULL;

    if (fej == NULL) { fej = uj; return fej; }

    mynode* temp = fej;

    while(temp->next != NULL) { temp = temp->next; }

    temp->next = uj;

    return fej;

}

mynode* beszur_eletkor_szerint_novekvo(mynode* fej, string nev, int eletkor) {

    mynode* uj = new mynode;

    uj->nev = nev;

    uj->eletkor = eletkor;

    uj->next = NULL;

    if (fej == NULL) { fej = uj; return fej; }

    mynode* elozo = NULL;

    mynode* akt = fej;

    while (!(eletkor < akt->eletkor)) { 

        elozo = akt; 

        akt = akt->next;

        if (akt == NULL) break;

    }

    if (akt == NULL) { fej = beszur_vegen(fej, nev, eletkor); }

    if (elozo == NULL) {

        fej = uj;

        uj->next = akt;

    }

    else {

        elozo->next = uj;

        uj->next = akt;

    }

    return fej;

}

int main()

{

    mynode* fej = NULL;

    fej = beszur_vegen(fej, "Eva", 21);

    fej = beszur_vegen(fej, "Bela", 23);

    fej = beszur_vegen(fej, "Adam", 25);

    fej = beszur_eletkor_szerint_novekvo(fej, "Zeno",  22);

    fej = beszur_eletkor_szerint_novekvo(fej, "Ilona", 19);

    fej = beszur_eletkor_szerint_novekvo(fej, "Ádám",  30);

    mynode* temp = fej;

    while (temp != NULL) {

        cout << temp->nev << ", " << temp->eletkor << endl;

        temp = temp->next;

    }   

}

