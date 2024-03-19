#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string xorEncrypt(const string& text, const string& key) {
    string result = text;
    for (size_t i = 0; i < text.size(); i++) {
        result[i] = text[i] ^ key[i % key.size()];
    }
    return result;
}

int main() {
    string fajlszoveg;
    string fajlnev;
    string nemtitkositott;
    string kulcs;
    string titkositott;

    cout << "Kerlek add meg a titkositando fajl nevet: ";
    cin >> fajlnev;

    fstream file(fajlnev, ios::in | ios::out | ios::binary);
    if(!file) {
        cout << "Nem letezik ilyen fajl!" << endl;
        return 1;
    }

    cout << "Kerlek add meg a kulcsot (ne felejtsd el, kell a visszafejteshez): ";
    cin >> kulcs;

    while(getline(file, fajlszoveg)) {
        nemtitkositott += fajlszoveg;
        if (!file.eof()) {
            nemtitkositott += "\n";
        }
    }


    titkositott = xorEncrypt(nemtitkositott, kulcs);

    file.clear();
    file.seekp(0);

    file << titkositott;
    file.close();

    cout << "Alap szoveg: \n" << nemtitkositott << endl;
    cout << "Titkositott szoveg: " << titkositott << endl;

    return 0;
}
