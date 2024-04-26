#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <iomanip>

using namespace std;

// Első feladat megoldása
void calculateItemFrequencies(const vector<vector<string>>& transactions) {
    map<string, int> itemCounts;

    for (const auto& transaction : transactions)
        for (const auto& item : transaction)
            itemCounts[item]++;

    cout << "1. feladat eredmenyei:" << endl;
    for (const auto& pair : itemCounts)
        cout << pair.first << ": " << fixed << setprecision(2) << ((double)pair.second / transactions.size() * 100) << "%" << endl;
}

// Második feladat megoldása
void calculateItemCombinations(const vector<vector<string>>& transactions) {
    map<string, int> itemCombinations;

    for (const auto& transaction : transactions)
        for (size_t i = 0; i < transaction.size(); ++i)
            for (size_t j = i + 1; j < transaction.size(); ++j)
                itemCombinations[transaction[i] + " " + transaction[j]]++;

    cout << "\n2. feladat eredmenyei:" << endl;
    for (const auto& pair : itemCombinations)
        cout << pair.first << " = " << pair.second << endl;
}

int main() {
    vector<vector<string>> transactions;
    ifstream file("transactions.txt");
    if (!file.is_open()) {
        cout << "Hiba a fajl megnyitasakor!" << endl;
        return 1;
    }

    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        vector<string> transaction;
        string item;
        while (ss >> item) {
            transaction.push_back(item);
            transactions.push_back(transaction);
        }
    }

    calculateItemFrequencies(transactions);
    calculateItemCombinations(transactions);

    return 0;
}
