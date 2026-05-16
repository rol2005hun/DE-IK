lany('edina').
lany('frida').
lany('gabriella').

fiu('jozsef').
fiu('vince').

nev(X) :- lany(X).
nev(X) :- fiu(X).

varos('budapest').
varos('debrecen').
varos('miskolc').
varos('pecs').
varos('szeged').

szak('biologia').
szak('informatika').
szak('jog').
szak('kemia').
szak('magyar').

diak(X, csoport(X,_,_,_,_)).
diak(X, csoport(_,X,_,_,_)).
diak(X, csoport(_,_,X,_,_)).
diak(X, csoport(_,_,_,X,_)).
diak(X, csoport(_,_,_,_,X)).

vezeteknev(d(X,_,_,_), X).
keresztnev(d(_,X,_,_), X).
egyetem(d(_,_,X,_), X).
tanul(d(_,_,_,X), X).

megoldas(T) :-
    T = csoport(
        d('egressy', _, _, _),
        d('fenyvesi', F_K, F_V, 'jog'),
        d('gallyas', _, _, _),
        d('jeney', J_K, 'pecs', _),
        d('vadkerti', 'gabriella', _, _)
    ),
    
    % 1. A FENYVESI vezetéknevű LÁNY JOGOT tanul, de NEM DEBRECENben.
    lany(F_K),
    varos(F_V), F_V \= 'debrecen',
    
    % 2. JÓZSEF (ő NEM GALLYAS) az egyik FŐVÁROSI (BUDAPEST) egyetemen tanul, de NEM BIOLÓGIÁt.
    diak(D2, T), keresztnev(D2, 'jozsef'), egyetem(D2, 'budapest'),
    vezeteknev(D2, Vez2), Vez2 \= 'gallyas',
    tanul(D2, Sz2), szak(Sz2), Sz2 \= 'biologia',
    
    % 3. VADKERTI GABRIELLA NEM a SZEGEDI-KÉMIA szakos hallgató.
    % (A szegedi kémiás diák létezik, de a vezetékneve biztosan nem Vadkerti)
    diak(D3, T), egyetem(D3, 'szeged'), tanul(D3, 'kemia'),
    vezeteknev(D3, Vez3), Vez3 \= 'vadkerti',
    
    % 4. JENEY (PÉCS) keresztneve NEM VINCE.
    nev(J_K), J_K \= 'vince',
    
    % 5. FRIDA MAGYARtanár szeretne lenni.
    diak(D5, T), keresztnev(D5, 'frida'), tanul(D5, 'magyar'),
    
    % 6. EDINA vezetékneve VAGY EGRESSY, VAGY MISKOLCon tanul.
    diak(D6, T), keresztnev(D6, 'edina'),
    vezeteknev(D6, Vez6), egyetem(D6, Var6), varos(Var6),
    ( Vez6 = 'egressy', Var6 \= 'miskolc' ; Vez6 \= 'egressy', Var6 = 'miskolc' ),
    
    % 7. Az INFORMATIKUSnak készűlő egyetemista nemrég NŐSÜLT. (tehát csak fiú lehet)
    diak(D7, T), tanul(D7, 'informatika'),
    keresztnev(D7, K7), fiu(K7),
    
    diak(E1, T), keresztnev(E1, 'edina'),
    diak(E2, T), keresztnev(E2, 'frida'),
    diak(E3, T), keresztnev(E3, 'gabriella'),
    diak(E4, T), keresztnev(E4, 'jozsef'),
    diak(E5, T), keresztnev(E5, 'vince'),
    
    diak(V_1, T), egyetem(V_1, 'budapest'),
    diak(V_2, T), egyetem(V_2, 'debrecen'),
    diak(V_3, T), egyetem(V_3, 'miskolc'),
    diak(V_4, T), egyetem(V_4, 'pecs'),
    diak(V_5, T), egyetem(V_5, 'szeged'),
    
    diak(S1, T), tanul(S1, 'biologia'),
    diak(S2, T), tanul(S2, 'informatika'),
    diak(S3, T), tanul(S3, 'jog'),
    diak(S4, T), tanul(S4, 'kemia'),
    diak(S5, T), tanul(S5, 'magyar').


% Kiíratás formázva
futtat :-
    megoldas(T),
    T = csoport(A, B, C, D, E),
    kiir_diak(A),
    kiir_diak(B),
    kiir_diak(C),
    kiir_diak(D),
    kiir_diak(E),
    nl.

kiir_diak(d(Vezeteknev, Keresztnev, Varos, Szak)) :-
    format('~w ~w, aki ~w egyetemre jar es ~w szakos.~n', [Vezeteknev, Keresztnev, Varos, Szak]).
