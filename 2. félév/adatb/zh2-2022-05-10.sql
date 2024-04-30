--1. feladat
select megrendeles_id, fizetett_osszeg from hajo.s_megrendeles
where fizetett_osszeg > (
    select max(fizetett_osszeg) from hajo.s_megrendeles
    where to_char(megrendeles_datuma, 'yyyy.mm') = '2021.04'
)

--2. feladat
select vezeteknev, keresztnev, orszag from hajo.s_ugyfel
join hajo.s_megrendeles on ugyfel = ugyfel_id
left join hajo.s_helyseg on helyseg = helyseg_id
where fizetett_osszeg < 1000000
order by vezeteknev, keresztnev

--3. feladat
select orszag, count(*) from hajo.s_helyseg
join hajo.s_kikoto on helyseg = helyseg_id
join hajo.s_megrendeles on kikoto_id = indulasi_kikoto
group by kikoto_id, orszag
order by count(*) desc nulls last
fetch first 3 rows only

--4. feladat
create table s_szemelyzet (
    azonosito number(4) primary key,
    vezeteknev varchar(40) not null,
    keresztnev varchar(40) not null,
    szuletesi_datum date,
    email_cim varchar(200),
    hajohoz_tartozik varchar(10) references hajo.s_hajo not null
)

--5. feladat
create table s_kikoto_telefon as select * from hajo.s_kikoto_telefon; --ez csak egy temp utasítás, alsó kell a ZH-ra
alter table s_kikoto_telefon add email varchar(200) default 'nem ismert'

--6. feladat
insert into s_hajo select hajo_id, s_hajo.nev, netto_suly, max_kontener_dbszam, max_sulyterheles, hajo_tipus
from hajo.s_hajo join hajo.s_hajo_tipus on hajo_tipus = hajo_tipus_id where s_hajo_tipus.nev = 'Small feeder' and netto_suly > 250

--7. feladat
create table s_megrendeles as select * from hajo.s_megrendeles; --ez csak egy temp utasítás, alsó kell a ZH-ra
update s_megrendeles set fizetett_osszeg = fizetett_osszeg * 1.15
where megrendeles_id in (
    select max(megrendeles_id)
    from hajo.s_megrendeles
    join hajo.s_ugyfel on ugyfel = ugyfel_id
    join hajo.s_helyseg on helyseg = helyseg_id
    where orszag = 'Franciaország'
    group by ugyfel_id
)

--8. feladat
create view nezet as
select kikoto_id, helysegnev, orszag, count(megrendeles_id) as megrendelesek_szama from hajo.s_kikoto
left join hajo.s_helyseg on helyseg_id = helyseg
left join hajo.s_megrendeles on kikoto_id = erkezesi_kikoto
group by kikoto_id, helysegnev, orszag

--9. feladat
create view nezet2 as select ut_id, indulasi_ido, erkezesi_ido, indulasi_kikoto, erkezesi_kikoto, hajo, nev, max_sulyterheles, sum(rakomanysuly) rs
from hajo.s_ut join hajo.s_szallit on ut = ut_id join hajo.s_hozzarendel on s_szallit.megrendeles = s_hozzarendel.megrendeles join hajo.s_hajo
on hajo = hajo_id having sum(rakomanysuly) > max_sulyterheles / 2
group by ut_id, indulasi_ido, erkezesi_ido, indulasi_kikoto, erkezesi_kikoto, hajo, nev, max_sulyterheles

--10. feladat
create table s_ut as select * from hajo.s_ut; --ez csak egy temp utasítás, alsó kell a ZH-ra
grant references on s_ut to panovics;
