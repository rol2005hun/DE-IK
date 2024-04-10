#include <iostream>
#include <windows.h>

using namespace std;

// Kurzor pozíciójának beállítása
void gotoxy(int x, int y) {
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

// A képernyő egy adott pontjának törlése
void clearPosition(int x, int y) {
    gotoxy(x, y);
    cout << " ";
}

int main() {
    int x = 1, y = 1;
    int dx = 1, dy = 1;
    const int width = 80, height = 24;

    // Falak kirajzolása
    for (int i = 0; i < width; ++i) {
        cout << "#";
    }
    for (int i = 1; i < height - 1; ++i) {
        gotoxy(0, i);
        cout << "#";
        gotoxy(width - 1, i);
        cout << "#";
    }
    gotoxy(0, height - 1);
    for (int i = 0; i < width; ++i) {
        cout << "#";
    }

    while (true) {
        gotoxy(x, y);  // Mozgatja a kurzort az új pozícióra
        cout << "O";  // Labda rajzolása
        
        Sleep(50);

        clearPosition(x, y);  // Eltávolítja a labdát az előző pozícióból

        // Frissíti a labda pozícióját
        x += dx;
        y += dy;

        // Ellenőrzi az ütközést a falakkal
        if (x <= 1 || x >= width - 2) {
            dx = -dx;
        }
        if (y <= 1 || y >= height - 2) {
            dy = -dy;
        }
    }

    return 0;
}
