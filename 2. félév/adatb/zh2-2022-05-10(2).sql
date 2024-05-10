--1. feladat
select unique helyseg_id, orszag, helysegnev from hajo.s_helyseg join hajo.s_kikoto on helyseg = helyseg_id
join hajo.s_ut on indulasi_kikoto = kikoto_id join hajo.s_hajo on hajo = hajo_id
where nev = 'SC Bella'

--2. feladat
select unique helyseg_id, orszag, helysegnev from hajo.s_helyseg
where helyseg_id in (
    select helyseg from hajo.s_ugyfel
) or helyseg_id in (
    select helyseg from hajo.s_kikoto
)
order by orszag, helysegnev

--3. feladat
select indulasi_kikoto, erkezesi_kikoto from hajo.s_hajo join hajo.s_ut on hajo = hajo_id
where nev = 'SC Nina'
order by erkezesi_ido - indulasi_ido
fetch first 3 rows only

--4. feladat
create table s_szemelyzet (
    azonosito varchar(10) primary key,
    vezeteknev varchar(50),
    keresztnev varchar(50),
    szuletesi_datum date,
    telefonszam number(20) not null,
    tartozik varchar(10) references hajo.s_hajo
)

--5. feladat
create table s_kikoto_telefon as select * from hajo.s_kikoto_telefon; --ez csak egy temp utasítás, alsó kell a ZH-ra
alter table s_kikoto_telefon drop constraint ide a nev

--6. feladat
insert into s_hajo select hajo_id, s_hajo.nev, netto_suly, max_kontener_dbszam, max_sulyterheles, hajo_tipus
from hajo.s_hajo join hajo.s_hajo_tipus on hajo_tipus = hajo_tipus_id where s_hajo_tipus.nev = 'Small feeder' and netto_suly > 250

--7. feladat
create table s_ugyfel as select * from hajo.s_ugyfel; --ez csak egy temp utasítás, alsó kell a ZH-ra
update s_ugyfel set keresztnev = upper(keresztnev), vezeteknev = upper(vezeteknev)
where (vezeteknev, keresztnev) in (select vezeteknev, keresztnev from ( 
    select ugyfel_id, keresztnev, vezeteknev, sum(fizetett_osszeg) as fo from hajo.s_ugyfel join hajo.s_megrendeles on ugyfel = ugyfel_id
    group by ugyfel_id, keresztnev, vezeteknev
) where fo in (select max(fo) from (
    select ugyfel_id, keresztnev, vezeteknev, sum(fizetett_osszeg) as fo from hajo.s_ugyfel join hajo.s_megrendeles on ugyfel = ugyfel_id
    group by ugyfel_id, keresztnev, vezeteknev
)))

--8. feladat
create view megrendelesek as
select m.*, hi.orszag as indulasi_helyseg_orszag, he.orszag as erkezesi_helyseg_orszag
from hajo.s_megrendeles m
join hajo.s_kikoto ki on ki.kikoto_id = m.indulasi_kikoto
join hajo.s_helyseg hi on ki.helyseg = hi.helyseg_id
join hajo.s_kikoto ke on ke.kikoto_id = m.erkezesi_kikoto
join hajo.s_helyseg he on ke.helyseg = he.helyseg_id

--9. feladat

