#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

struct Kutya {
    string nev;
    string faj;
    int kor;
    string szin;
};

class Menhely {
private:
    vector<Kutya> kutyak;

public:
    Menhely() {
        ifstream file("menhely.txt");
        string sor;
        if (file.is_open()) {
            while (getline(file, sor)) {
                stringstream ss(sor);
                Kutya kutya;
                string kor;
                getline(ss, kutya.nev, '-');
                getline(ss, kutya.faj, '-');
                getline(ss, kor, '-');
                kutya.kor = stoi(kor);
                getline(ss, kutya.szin);
                kutyak.push_back(kutya);
            }
            file.close();
        } else {
            cout << "Nem sikerult megnyitni a menhely.txt fajlt." << endl;
        }
    }

    void KutyaKereses() {
        cout << "Adja meg a keresesi kriteriumot (Nev/Faj/Kor/Szin): ";
        string keresesiKriterium;
        cin >> keresesiKriterium;
        transform(keresesiKriterium.begin(), keresesiKriterium.end(), keresesiKriterium.begin(), ::tolower);
        if(keresesiKriterium != "nev" && keresesiKriterium != "faj" && keresesiKriterium != "kor" && keresesiKriterium != "szin") {
            cout << "Hibas keresesi kriterium." << endl;
            return;
        }

        string ertek;
        cout << "Adja meg a keresesi erteket: ";
        cin >> ertek;
        transform(ertek.begin(), ertek.end(), ertek.begin(), ::tolower);

        bool talalat = false;
        for (const auto& kutya : kutyak) {
            string kutyaNev = kutya.nev;
            transform(kutyaNev.begin(), kutyaNev.end(), kutyaNev.begin(), ::tolower);

            string kutyaFaj = kutya.faj;
            transform(kutyaFaj.begin(), kutyaFaj.end(), kutyaFaj.begin(), ::tolower);

            string kutyaSzin = kutya.szin;
            transform(kutyaSzin.begin(), kutyaSzin.end(), kutyaSzin.begin(), ::tolower);

            if ((keresesiKriterium == "nev" && kutyaNev.find(ertek) != string::npos) ||
                (keresesiKriterium == "faj" && kutyaFaj.find(ertek) != string::npos) ||
                (keresesiKriterium == "kor" && to_string(kutya.kor) == ertek) ||
                (keresesiKriterium == "szin" && kutyaSzin.find(ertek) != string::npos)) {
                cout << "Nev: " << kutya.nev << ", Faj: " << kutya.faj << ", Kor: " << kutya.kor << ", Szin: " << kutya.szin << endl;
                talalat = true;
            }
        }

        if (!talalat) {
            cout << "Nincs ilyen kutya." << endl;
        }
    }
};

int main() {
    Menhely menhely;

    char folytatja;
    do {
        menhely.KutyaKereses();
        cout << "Szeretne tovabbi kutyakat keresni? (I/N): ";
        cin >> folytatja;
    } while (folytatja == 'I' || folytatja == 'i');

    cout << "Viszlat! Nezzen vissza kesobb is.";

    return 0;
}
