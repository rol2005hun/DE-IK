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
    azonosito number(4),
    vezeteknev varchar(40),
    keresztnev varchar(40),
    szuletesi_datum date,
    email_cim varchar(200),
    hajohoz_tartozik varchar(10) not null
)

--5. feladat
create table s_kikoto_telefon as select * from hajo.s_kikoto_telefon;
alter table s_kikoto_telefon add email varchar(200) default 'nem ismert'

--6. feladat
create table s_hajo as
select * from hajo.s_hajo join hajo.s_hajo_tipus on hajo_tipus = hajo_tipus_id where s_hajo_tipus.nev = 'Small feeder' and netto_suly > 250

--7. feladat
ez ma nehez pa
