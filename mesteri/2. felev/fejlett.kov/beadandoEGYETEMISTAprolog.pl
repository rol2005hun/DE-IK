megoldas(Diakok) :-
    Diakok = [
        ['egressy', _, _, _],
        ['fenyvesi', _, _, _],
        ['gallyas', _, _, _],
        ['jeney', _, _, _],
        ['vadkerti', _, _, _]
    ],
    
    member([_, 'edina', _, _], Diakok),
    member([_, 'frida', _, _], Diakok),
    member([_, 'gabriella', _, _], Diakok),
    member([_, 'jozsef', _, _], Diakok),
    member([_, 'vince', _, _], Diakok),

    member([_, _, 'budapest', _], Diakok),
    member([_, _, 'debrecen', _], Diakok),
    member([_, _, 'miskolc', _], Diakok),
    member([_, _, 'pecs', _], Diakok),
    member([_, _, 'szeged', _], Diakok),

    member([_, _, _, 'biologia'], Diakok),
    member([_, _, _, 'informatika'], Diakok),
    member([_, _, _, 'jog'], Diakok),
    member([_, _, _, 'kemia'], Diakok),
    member([_, _, _, 'magyar'], Diakok),
    
    % 1. A FENYVESI vezetéknevű LÁNY JOGOT tanul, de NEM DEBRECENben.
    member(['fenyvesi', FenyvesiKeresztneve, FenyvesiEgyeteme, 'jog'], Diakok),
    member(FenyvesiKeresztneve, ['edina', 'frida', 'gabriella']),
    FenyvesiEgyeteme \= 'debrecen',
    
    % 2. JÓZSEF (ő NEM GALLYAS) az egyik FŐVÁROSI(BUDAPEST) egyetemen tanul, de NEM BIOLÓGIÁt.
    member([JozsefVezetekneve, 'jozsef', 'budapest', JozsefSzakja], Diakok),
    JozsefVezetekneve \= 'gallyas',
    JozsefSzakja \= 'biologia',
    
    % 3. VADKERTI GABRIELLA NEM a SZEGEDI-KÉMIA szakos hallgató.
    member([_, _, 'szeged', 'kemia'], Diakok),
    member(['vadkerti', 'gabriella', VadkertiEgyeteme, VadkertiSzakja], Diakok),
    (VadkertiEgyeteme \= 'szeged'; VadkertiSzakja \= 'kemia'),
    
    % 4. JENEY (PÉCS) keresztneve NEM VINCE.
    member(['jeney', JeneyKeresztneve, 'pecs', _], Diakok),
    JeneyKeresztneve \= 'vince',
    
    % 5. FRIDA MAGYARtanár szeretne lenni.
    member([_, 'frida', _, 'magyar'], Diakok),
    
    % 6. EDINA vezetékneve VAGY EGRESSY, VAGY MISKOLCon tanul.
    member([EdinaVezetekneve, 'edina', EdinaEgyeteme, _], Diakok),
    ((EdinaVezetekneve = 'egressy', EdinaEgyeteme \= 'miskolc');
    (EdinaVezetekneve \= 'egressy', EdinaEgyeteme = 'miskolc')),
    
    % 7. Az INFORMATIKUSnak készűlő egyetemista nemrég NŐSÜLT. (tehát csak fiú lehet)
    member([_, InformatikusKeresztneve, _, 'informatika'], Diakok),
    member(InformatikusKeresztneve, ['jozsef', 'vince']).