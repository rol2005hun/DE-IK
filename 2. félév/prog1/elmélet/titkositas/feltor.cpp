#include <iostream>
#include <string>
#include <fstream>

using namespace std;

ifstream file("alma.txt");

string xorDecrypt(const string& text, const string& key) {
    string result = text;
    for (size_t i = 0; i < text.size(); ++i) {
        result[i] = text[i] ^ key[i % key.size()];
    }
    return result;
}

int main() {
    string titkositott;
    string fajlszoveg;
    string kulcs = "soboslaiabo$$";

    while(getline(file, titkositott)) {
        fajlszoveg += titkositott + "\n";
    }

    fajlszoveg = fajlszoveg.substr(0, fajlszoveg.size() - 1);

    cout << "Visszafejtett szoveg: " << xorDecrypt(fajlszoveg, kulcs) << endl;

    return 0;
}
