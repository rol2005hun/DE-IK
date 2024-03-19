#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Auto {
  string rendszam;
  string szin;
  string tipus;
  string marka;
  int evjarat;
  int ar;
};

class AutoKereskedes {
  private: vector < Auto > autok;

  public: void autoHozzaad(const Auto & autoToAdd) {
    autok.push_back(autoToAdd);
    cout << "Auto hozzaadva." << endl;
  }

  Auto * autoKereses(const string & keresesiKriterium, string & keresesiErtek) {
    for (auto & autoElem: autok) {
      Auto autoCopy = autoElem;
      transform(keresesiErtek.begin(), keresesiErtek.end(), keresesiErtek.begin(), ::tolower);
      transform(autoCopy.rendszam.begin(), autoCopy.rendszam.end(), autoCopy.rendszam.begin(), ::tolower);
      transform(autoCopy.szin.begin(), autoCopy.szin.end(), autoCopy.szin.begin(), ::tolower);
      transform(autoCopy.tipus.begin(), autoCopy.tipus.end(), autoCopy.tipus.begin(), ::tolower);
      transform(autoCopy.marka.begin(), autoCopy.marka.end(), autoCopy.marka.begin(), ::tolower);
      if (keresesiKriterium == "rendszam" && autoCopy.rendszam == keresesiErtek) {
        return &autoElem;
      } else if (keresesiKriterium == "szin" && autoCopy.szin == keresesiErtek) {
        return &autoElem;
      } else if (keresesiKriterium == "marka" && autoCopy.marka == keresesiErtek) {
        return &autoElem;
      } else if (keresesiKriterium == "tipus" && autoCopy.tipus == keresesiErtek) {
        return &autoElem;
      }
    }
    return nullptr;
  }


  void autoTorles(const string & rendszam) {
    string rendszamCopy = rendszam;
    transform(rendszamCopy.begin(), rendszamCopy.end(), rendszamCopy.begin(), ::toupper);
    for (auto it = autok.begin(); it != autok.end(); ++it) {
      if (it -> rendszam == rendszamCopy) {
        autok.erase(it);
        cout << "Auto torolve." << endl;
        return;
      }
    }
    cout << "Nincs ilyen rendszamu auto az adatbazisban." << endl;
  }

  void osszesAutoLekerdezes() {
    if (autok.empty()) {
      cout << "Nincsenek autok az adatbazisban." << endl;
      return;
    }

    cout << "\nOsszes auto az adatbazisban:" << endl;
    for (const auto & autoElem: autok) {
      cout << "Rendszam: " << autoElem.rendszam << ", Szin: " << autoElem.szin <<
        ", Evjarat: " << autoElem.evjarat << ", Ar: " << autoElem.ar <<
        ", Tipus: " << autoElem.tipus << ", Marka: " << autoElem.marka << endl;
    }
    char tovabb;
    cout << "\nFolytatja? (I/N): ";
    cin >> tovabb;
    if (tovabb != 'I' && tovabb != 'i') {
      cout << "Viszlat!" << endl;
      return;
    }
  }

  void menuMegjelenites() {
    char valasztas;
    do {
      cout << "\n*** AutoKereskedes Menu ***" << endl;
      cout << "A. Auto hozzaadasa" << endl;
      cout << "K. Auto keresese" << endl;
      cout << "O. Osszes auto lekerdezese" << endl;
      cout << "T. Auto torlese" << endl;
      cout << "X. Kilepes" << endl;
      cout << "Valasztas: ";
      cin >> valasztas;

      switch (valasztas) {
      case 'A':
      case 'a': {
        Auto autoToAdd;
        cout << "Rendszam: ";
        cin >> autoToAdd.rendszam;
        cout << "Szin: ";
        cin >> autoToAdd.szin;
        cout << "Tipus: ";
        cin >> autoToAdd.tipus;
        cout << "Marka: ";
        cin >> autoToAdd.marka;
        cout << "Evjarat: ";
        cin >> autoToAdd.evjarat;
        cout << "Ar: ";
        cin >> autoToAdd.ar;
        autoHozzaad(autoToAdd);
        break;
      }
      case 'K':
      case 'k': {
        char keresesiKriterium;
        string keresesiErtek;
        cout << "Keresesi kriterium (Rendszam - R, Szin - S, Marka - M, Tipus - T): ";
        cin >> keresesiKriterium;
        cout << "Keresesi ertek: ";
        cin >> keresesiErtek;

        Auto * keresettAuto = nullptr;
        switch (keresesiKriterium) {
        case 'r':
        case 'R':
          keresettAuto = autoKereses("rendszam", keresesiErtek);
          break;
        case 's':
        case 'S':
          keresettAuto = autoKereses("szin", keresesiErtek);
          break;
        case 'm':
        case 'M':
          keresettAuto = autoKereses("marka", keresesiErtek);
          break;
        case 't':
        case 'T':
          keresettAuto = autoKereses("tipus", keresesiErtek);
          break;
        default:
          cout << "Ervenytelen keresesi kriterium." << endl;
        }

        if (keresettAuto != nullptr) {
          cout << endl << "Keresett auto adatai:" << endl;
          cout << "Rendszam: " << keresettAuto -> rendszam << endl;
          cout << "Szin: " << keresettAuto -> szin << endl;
          cout << "Evjarat: " << keresettAuto -> evjarat << endl;
          cout << "Ar: " << keresettAuto -> ar << endl;
          cout << "Tipus: " << keresettAuto -> tipus << endl;
          cout << "Marka: " << keresettAuto -> marka << endl;
          char tovabb;
          cout << "\nFolytatja? (I/N): ";
          cin >> tovabb;
          if (tovabb != 'I' && tovabb != 'i') {
            cout << "Viszlat!" << endl;
            return;
          }
        } else {
          cout << "Nincs ilyen auto az adatbazisban." << endl;
        }
        break;
      }
      case 'O':
      case 'o': {
        osszesAutoLekerdezes();
        break;
      }
      case 'T':
      case 't': {
        string torlendoRendszam;
        cout << "Torlendo rendszam: ";
        cin >> torlendoRendszam;
        autoTorles(torlendoRendszam);
        break;
      }
      case 'X':
      case 'x':
        cout << "Viszlat!" << endl;
        break;
      default:
        cout << "Ervenytelen valasztas!" << endl;
      }
    } while (valasztas != 'X' && valasztas != 'x');
  }
};

int main() {
  AutoKereskedes kereskedes;

  // hozzaadunk nehany autot, hogy legyen mit keresni
  Auto auto1 = {"ABC123", "piros", "szedan", "Toyota", 2019, 10000};
  Auto auto2 = {"DEF456", "kek", "kombi", "Ford", 2020, 15000};
  Auto auto3 = {"GHI789", "feher", "hatchback", "Volkswagen", 2018, 8000};

  kereskedes.autoHozzaad(auto1);
  kereskedes.autoHozzaad(auto2);
  kereskedes.autoHozzaad(auto3);

  kereskedes.menuMegjelenites();

  return 0;
}
