// módosítók: nincs egy se
// visszatérítési típus: int
// név: main
// paraméter lista: ()

#include <iostream>
using namespace std;

int add(int x)
{
	return x + 1;
}

int main()
{
	int x = 15;
	cout << x << " hello";
	return 0; // return kulcsszó után visszatérítési érték, ha nem void
}
