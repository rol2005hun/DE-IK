% X-nek apja Y
apja(zsuzsa, andor).
apja(istvan, laszlo).
apja(tamas, istvan).

% X-nek anyja Y
anyja(zsuzsa, noemi).
anyja(istvan, eva).
anyja(tamas, zsuzsa).

% X-nek szülője Y
szulo(X, Y) :- apja(X, Y).
szulo(X, Y) :- anyja(X, Y).

% X-nek gyermeke Y
gyermeke(X, Y) :- szulo(Y, X).

% X-nek nagyszülője Y
nagyszulo(X, Y) :- szulo(X, Z), szulo(Z, Y).
