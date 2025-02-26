# Git parancsok
## Alapok
1. Állítsd be a felhasználónevedet és email címedet
	```
	git config --global user.name "uname"
	git config --global user.email email@email.com
	```
	
	Vagy csak a helyi tárolóban
	```
	git config user.name "uname"
	git config user.email email@email.com
	```
2. Initializáld a tárolót
	```
	git init
	```
3. Add hozzá a fájlokat a tárolóhoz
	```
	git add .
	```
	Itt a pont hozzáadja az összes fájlt ami megtalálható a branchben.
4. Nézd meg, hogy hozzá lettek-e adva a kívánt fájlok
	```
	git status
	```
5. Véglegesítsd a módosításokat
	```
	git commit -am "docs: update README.md"
	```
## Más fontos parancsok
1. Új branch készítése
	```
	git branch newbranch
	```
	Készít egy új branchet newbranch néven.
2. Branch változtatása
	```
	git checkout newbranch
	```
	Átvált a **newbranch** néven futó branchre.
3. Branchek listázása
	```
	git branch --list
	```
4. Commitok logjának lekérése
	```
	git log --oneline --all --graph
	```
5. Két branch összefésülése
	```
	git checkout master
	```
	Át megyünk a **master** branchbe, mivel ezt szeretnénk főbranchnek.
	```
	git merge newbranch
	```
	A **newbranch** branchben lévő fájlokat összefésüli.
	```
	git branch -d newbranch
	```
	Ha nem szükséges már a **newbranch** branch nekünk, akkor törölhetjük.

## A tároló feltöltése GitHub-ra
1. Hozzárendeljük a remote linket
	```
	git remote add origin https://github.com/<username>/<reponame>.git
	```
2. Nevezd át master-re a helyi branchedet
	```
	git branch -M master
	```
3. Felpusholjuk a GitHub tárolóba
	```
	git push -u origin master
	```
	Ekkor előugrik egy ablak a GitHub-os bejelentkezéssel. Ha sikeresen bejelentkezel, akkor automatikusan feltölti a fájlokat, és máris készen vagy.

## Megjegyzések
- Ha nem jut eszedbe egy parancsnak a paraméterei, akkor használd a **git help <parancsnév>** parancsot.
- Ezek **Windowson** működnek jól, ha fel vannak telepítve a szükséges dolgok, Linuxon/Mac-en eltérhetnek kicsit.

## Más linkek
1. Órai linkek
- [Working with Git](https://gist.github.com/jeszy75/4b40aa2a8917e2df772ff6e21ed21509)
- [Git kezdőlépések](https://gist.github.com/jeszy75/7d7e33d008a94f6ac1deee6b18af4d65)
2. Letöltési linkek
- [Git - Downloading Package](https://git-scm.com/downloads/win)
