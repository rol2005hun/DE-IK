select kontener || ' ' || megrendeles, round(rakomanysuly, 2) from hajo.s_hozzarendel
select * from hajo.s_kikoto where leiras like '%kikötőméret: kicsi%mobil daruk%'
select * from hajo.s_ut where to_char(indulasi_ido, 'MI') != '00'
select hajo_tipus, count(hajo_tipus) from hajo.s_hajo where max_sulyterheles > 500 group by hajo_tipus
select to_char(megrendeles_datuma, 'YYYY, MM') from hajo.s_megrendeles group by to_char(megrendeles_datuma, 'YYYY, MM') having count(to_char(megrendeles_datuma, 'YYYY, MM')) > 6 order by to_char(megrendeles_datuma, 'YYYY, MM')
select vezeteknev || ' ' || keresztnev, telefon from hajo.s_ugyfel where helyseg in (select helyseg_id from hajo.s_helyseg where orszag = 'Szíria')
select s_hajo_tipus.nev, min(s_hajo.netto_suly) from hajo.s_hajo_tipus join hajo.s_hajo on hajo_tipus = s_hajo.hajo_tipus group by s_hajo_tipus.nev
select orszag || ' - ' || helysegnev from hajo.s_helyseg join hajo.s_kikoto on helyseg = helyseg_id where orszag in (select orszag from hajo.s_orszag where foldresz = 'Ázsia') order by helysegnev
select nev, hajo_id, indulasi_kikoto, erkezesi_kikoto from hajo.s_hajo join hajo.s_ut on hajo_id = hajo where indulasi_ido = (select max(indulasi_ido) from hajo.s_ut)
select erkezesi_kikoto from hajo.s_ut where indulasi_ido = (select min(indulasi_ido) from hajo.s_ut)
