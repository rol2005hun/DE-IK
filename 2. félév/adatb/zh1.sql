select megrendeles, kontener, round(rakomanysuly, 2) from hajo.s_hozzarendel where rakomanysuly > 15
select * from hajo.s_kikoto where leiras like '%kikötőméret: kicsi%' and leiras like '%mobil daruk%'
select to_char(indulasi_ido, 'YYYY.MM.DD HH:MI:SS') from hajo.s_ut where to_char(indulasi_ido, 'MI') != '00' order by to_char(indulasi_ido, 'YYYY.MM.DD HH:MI')
select hajo_tipus, count(*) from hajo.s_hajo where max_sulyterheles > 500 group by hajo_tipus
select to_char(megrendeles_datuma, 'YYYY.MM'), count(*) from hajo.s_megrendeles group by to_char(megrendeles_datuma, 'YYYY.MM') having count(*) >=6 order by to_char(megrendeles_datuma, 'YYYY.MM')
select vezeteknev, keresztnev, telefon from hajo.s_ugyfel where helyseg in (select helyseg_id from hajo.s_helyseg where orszag = 'Szíria')
select s_hajo_tipus.nev, min(netto_suly) from hajo.s_hajo_tipus join hajo.s_hajo on hajo_tipus_id = hajo_tipus group by s_hajo_tipus.nev
select s_orszag.orszag, helysegnev from hajo.s_orszag join hajo.s_helyseg on s_helyseg.orszag = s_orszag.orszag where s_orszag.foldresz = 'Ázsia' and helyseg_id in (select helyseg from hajo.s_kikoto) order by helysegnev
select nev, hajo_id, indulasi_kikoto, erkezesi_kikoto from hajo.s_hajo join hajo.s_ut on hajo = hajo_id where indulasi_ido = (select max(indulasi_ido) from hajo.s_ut)
select erkezesi_kikoto from hajo.s_ut where indulasi_ido = (select min(indulasi_ido) from hajo.s_ut)
