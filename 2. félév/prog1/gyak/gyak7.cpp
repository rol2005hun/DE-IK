#include <iostream>
using namespace std;

struct mynode {
    string nev;
    int eletkor;
    mynode* next;
};

mynode* beszur_eletkor_szerint_novekvo(mynode* fej, string nev1, int eletkor1) {
    mynode* uj = new mynode;
    uj -> nev = nev1;
    uj -> eletkor = eletkor1;
    uj -> next = NULL;

    if(fej == NULL) {
        fej = uj;
        return fej;
    }
    mynode* temp = fej;
    while(temp -> next != NULL) {
        if(temp->next->eletkor>uj->eletkor) {
            uj->next = temp->next;
            temp->next = uj;
            return fej;
        }
        temp = temp -> next;
    }
    temp -> next = uj;
    return fej;
}

void beszur_vegen(mynode** fej, string nev, int eletkor) {
    mynode* uj = new mynode;
    uj->nev = nev;
    uj->eletkor = eletkor;
    uj->next=NULL;
    if(*fej = NULL) {
        *fej = uj;
    }
    mynode* temp = *fej;
    while(temp->next!=NULL) {
        // nem tudom, en mar kiegtem :D
        // tsa
    }
}

void felszabadit(mynode* lista) {
    free(lista);
}

void kiir(mynode* lista) {
    mynode* temp = lista;
    while(temp != NULL) {
        cout << temp -> nev << " ";
        cout << temp -> eletkor << endl;
        temp = temp -> next;
    }

    mynode* akt = lista;
    while(akt != NULL) {
        mynode* temp2 = akt -> next;
        felszabadit(akt);
        akt = temp2;
    }
}

int main() {
    mynode* fej = NULL;

    fej = beszur_eletkor_szerint_novekvo(fej, "Eva", 21);
    fej = beszur_eletkor_szerint_novekvo(fej, "Bela", 23);
    fej = beszur_eletkor_szerint_novekvo(fej, "Adam", 25);

    fej = beszur_eletkor_szerint_novekvo(fej, "Zeno", 22);
    fej = beszur_eletkor_szerint_novekvo(fej, "Ilona", 19);
    fej = beszur_eletkor_szerint_novekvo(fej, "Lajos", 30);

    kiir(fej);

    return 0;
}
