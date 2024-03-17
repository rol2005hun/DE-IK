#include <iostream>
#include <string>
#include <fstream>

using namespace std;

fstream file("alma.txt", ios::in | ios::out);

string xorEncrypt(const string& text, const string& key) {
    string result = text;
    for (size_t i = 0; i < text.size(); ++i) {
        result[i] = text[i] ^ key[i % key.size()];
    }
    return result;
}

int main() {
    string fajlszoveg;
    string nemtitkositott;
    string kulcs = "soboslaiabo$$";
    string titkositott;

    while(getline(file, fajlszoveg)) {
        nemtitkositott += fajlszoveg;
    }

    titkositott = xorEncrypt(nemtitkositott, kulcs);

    file.clear();
    file.seekp(0);

    file << titkositott;
    file.close();

    cout << "Alap szoveg: " << nemtitkositott << endl;
    cout << "Titkositott szoveg: " << titkositott << endl;

    return 0;
}
