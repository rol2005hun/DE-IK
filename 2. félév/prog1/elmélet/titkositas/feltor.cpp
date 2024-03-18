#include <iostream>
#include <string>
#include <fstream>

using namespace std;

fstream file("alma.txt", ios::in | ios::out);

string xorDecrypt(const string& text, const string& key) {
    string result = text;
    for (size_t i = 0; i < text.size(); i++) {
        result[i] = text[i] ^ key[i % key.size()];
    }
    return result;
}

int main() {
    string titkositott;
    string fajlszoveg;
    string kulcs = "soboslaiabo$$";
    string visszafejtett;

    while(getline(file, titkositott)) {
        fajlszoveg += titkositott;
        if (!file.eof()) {
            fajlszoveg += "\n";
        }
    }

    visszafejtett = xorDecrypt(fajlszoveg, kulcs);

    cout << "Titkositott szoveg: " << fajlszoveg << endl; 
    cout << "Visszafejtett szoveg: " << visszafejtett << endl;
    cout << "Visszaallitsam a fajl tartalmat az eredeti szoveg tartalmara? (I/n) ";

    char x;
    cin >> x;
    if(x == 'i' || x == 'I') {
        file.clear();
        file.seekp(0);

        file << visszafejtett;
    }

    file.close();

    return 0;
}
