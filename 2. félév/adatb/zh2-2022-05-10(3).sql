-- ennek csak 7 feladat latszodik
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
-- ez mar nem latszik
