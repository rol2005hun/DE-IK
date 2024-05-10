--1. feladat
select ugyfel_id, vezeteknev, keresztnev, megrendeles_id from hajo.s_ugyfel
left join hajo.s_megrendeles on ugyfel = ugyfel_id
order by vezeteknev, keresztnev, megrendeles_id

--2. feladat
select * from hajo.s_megrendeles
join hajo.s_ugyfel on ugyfel = ugyfel_id
where keresztnev = 'Yiorgos' and fizetett_osszeg > 2000000
    and megrendeles_id not in (
        select megrendeles from hajo.s_szallit
    )
--3. feladat
select nev, count(*) from hajo.s_hajo
join hajo.s_ut on hajo_id = hajo
group by nev
order by count(*) desc
fetch first 3 rows only

--4. feladat
create table s_hajo_javitas (
    azonosito varchar(10) references hajo.s_hajo,
    jav_kezd date,
    jav_veg date,
    jav_ar number(10, 2),
    leiras varchar(200),
    primary key(azonosito, jav_kezd)
)

--5. feladat
alter table s_ugyfel modify email varchar(50)

--6. feladat
insert into s_ugyfel
select u.* from hajo.s_ugyfel u
join hajo.s_helyseg on helyseg = helyseg_id
where orszag = 'Olaszország'

--7. feladat
create table s_ut as select * from hajo.s_ut; --ez csak egy temp utasítás, alsó kell a ZH-ra
create table s_helyseg as select * from hajo.s_helyseg; --ez csak egy temp utasítás, alsó kell a ZH-ra
update s_ut set indulasi_kikoto = (
    select kikoto_id from hajo.s_kikoto
    join hajo.s_helyseg on helyseg_id = helyseg
    where helysegnev = 'Algeciras'
) where ut_id in (
    select ut_id from hajo.s_ut
    join hajo.s_kikoto on indulasi_kikoto = kikoto_id
    join hajo.s_helyseg on helyseg = helyseg_id
    where to_char(indulasi_ido, 'yyyy.mm') = '2021.07'
    and helysegnev = 'Valencia'
)

--8. feladat
create view utak as
select u.*, hi.orszag as indulasi, he.orszag as erkezesi from hajo.s_ut u
join hajo.s_kikoto ki on ki.kikoto_id = indulasi_kikoto
join hajo.s_helyseg hi on ki.helyseg = hi.helyseg_id
join hajo.s_kikoto ke on ke.kikoto_id = erkezesi_kikoto
join hajo.s_helyseg he on ke.helyseg = he.helyseg_id

--9. feladat
select kikoto_id, helysegnev, orszag from hajo.s_kikoto
join hajo.s_helyseg on helyseg = helyseg_id
where kikoto_id in (
    select indulasi_kikoto as indulasok from hajo.s_ut
    group by indulasi_kikoto
    having count(*) = (
        select max(count(*)) from hajo.s_ut
        group by indulasi_kikoto
    )
) or kikoto_id in (
    select erkezesi_kikoto as erkezesek from hajo.s_ut
    group by erkezesi_kikoto
    having count(*) = (
        select max(count(*)) from hajo.s_ut
        group by erkezesi_kikoto
    )
)

--10. feladat
grant update (vezeteknev, keresztnev) s_ugyfel to panovics
