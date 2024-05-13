--1. feladat
select megrendeles_id, igenyelt_kontenerszam from hajo.s_megrendeles
where igenyelt_kontenerszam = any (
    select igenyelt_kontenerszam from hajo.s_megrendeles
    where to_char(megrendeles_datuma, 'yyyy.mm') = '2021.02'
)

--2. feladat
select unique helyseg_id, helysegnev, orszag from hajo.s_helyseg
join hajo.s_ugyfel u on helyseg_id = u.helyseg
left join hajo.s_kikoto k on helyseg_id = k.helyseg
order by orszag, helysegnev

--2. feladat
select nev, count(*) from hajo.s_hajo
join hajo.s_ut on hajo = hajo_id
where max_kontener_dbszam <= 10
group by nev
having count(*) > 0
fetch first 2 rows only

--3. feladat
select nev,count(*) from hajo.s_hajo JOIN hajo.s_ut ON hajo=hajo_id
    where max_kontener_dbszam<11
    group by hajo_id,nev 
    order by count(*) ASC
    fetch first 2 rows only;

--4. feladat
create table s_szemlyet (
    azon number(5) constraint pk primary key,
    vezeteknev varchar2(40),
    keresztnev varchar2(40),
    szdat date,
    email varchar2(200),
    tartozik varchar2(10),
    constraint tart foreign key(hajo_id) references s_hajo,
    constraint osszk unique(vezeteknev, keresztnev, szdat)
)

--5. feladat
alter table s_kikoto_telefon drop constraint SYS_C00169549

--6. feladat
DELETE from s_ut
    where ut_id in (select ut from s_szallit 
    where 20>(select SUM(kontener) from s_szallit where ut=ut_id) and ut=ut_id 
        )and to_char( indulasi_ido,'YYYY.MM')='2021.06';

--7. feladat
drop table s_kikoto;
create table s_kikoto as select * from hajo.s_kikoto;
update s_kikoto set leiras = helyseg || ', ' || leiras
where kikoto_id in (
    select kikoto_id from hajo.s_kikoto
    where leiras like '%terminálterület: nagy,%'
)

--8. feladat
create view megrendelesek as
select m.*, hi.orszag as indulasi_helyseg_orszag, he.orszag as erkezesi_helyseg_orszag
from hajo.s_megrendeles m
join hajo.s_kikoto ki on ki.kikoto_id = m.indulasi_kikoto
join hajo.s_helyseg hi on ki.helyseg = hi.helyseg_id
join hajo.s_kikoto ke on ke.kikoto_id = m.erkezesi_kikoto
join hajo.s_helyseg he on ke.helyseg = he.helyseg_id

--9. feladat
varom sobot

--10. feladat
grant modify on s_ugyfel to panovics
