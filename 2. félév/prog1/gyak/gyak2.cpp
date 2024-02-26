#include <iostream>
using namespace std;

int main()
{
	// string name; // változó deklaráció
	// cout << "Kérlek írd be a neved\n";
	// cin >> name;
	// cout << "Szia " << name << endl;
	// // bekérek két számot és kíirom a nagyobbat
	// int a, b;
	// cout << "Kérlek írj be egy számot\n";
	// cin >> a;
	// cout << "Kérlek írd be a második számot\n";
	// cin >> b;

	// if szintaxia
	// if (feltétel) { igaz ág } else { hamis ág }
	// if szemantikája
	// ha igaz a feltétel, akkor az igaz ág fut le
	// egyébként a hamis ág
	// A program utasításokból áll
	// Az utasítás lehet:
	// Szekvencia, szelekció, iteráció
	// Szelekcióból két fajta van:
	// 2 ágú: if
	// sok ágú: switch

	/* if (a == b) cout << "Egyenlő";
	else if (a > b) cout << a;
	else cout << b; */

	// // feladat: kérj be 3 számot, és írd ki a legnagyobbat

	// int a, b, c;

	// cin >> a >> b >> c;

	// if (a >= b && a >= c) cout << a;
	// else if (b >= a && b >= c) cout << b;
	// else cout << c;
	 
	// && logikai és operátor
	// || logikai vagy operátor
	// mindkettő úgynevezett rövid-zár kiértékelésű
	// azaz
	// false && x > 5, ilyenkor a 2. operandust ki sem értékeli
	// true || x > 5
	// !(x > 5) == x <= 5

	// // feladat: kérjünk be 3 oldalhosszt, írassuk ki lehet-e ebből 3szöget szerkeszteni
	// // szabály: bármely két oldal összege > a 3.
	// // pl.: 3,4,5

	// int a, b, c;
	// cin >> a >> b >> c;
	// if ((a + b) > c && (a + c) > b && (b + c) > a) cout << "lehet";
	// else cout << "nem lehet";

	// feladat: kérjünk be 3 szöget, írassuk ki lehet-e belőle szerkeszteni 3szöget

	/* float a, b, c;

	cin >> a >> b >> c;

	if (a + b + c == 180) cout << "lehet";
	else cout << "nem lehet"; */

	// feladat: bekérem az életkort, 0-1 csecsemő, 2-6 kisgyerek, 6-9 gyerek, 10-18 tini, 18 > felnőtt

	int a;
	cin >> a;
	if (a >= 0 && a < 2) cout << "csecsemő";
	else if (a >= 2 && a < 6) cout << "kisgyerek";
	else if (a >= 6 && a < 10) cout << "gyerek";
	else if (a >= 10 && a < 18) cout << "tini";
	else cout << "felnőtt";

	return 0;
}
