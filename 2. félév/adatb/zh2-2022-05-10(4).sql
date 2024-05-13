--1. feladat
select ht.nev as tipusnev, hajo_tipus_id, h.nev as hajonev, hajo_tipus_id
from hajo.s_hajo_tipus ht
left join hajo.s_hajo h on hajo_tipus = hajo_tipus_id
order by tipusnev, hajonev

--2. feladat
select unique indulasi_kikoto kikotok from hajo.s_ut
where erkezesi_kikoto = 'It_Cat'
union
select unique erkezesi_kikoto from hajo.s_megrendeles
where indulasi_kikoto = 'It_Cat'
order by kikotok

--3. feladat
select vezeteknev, keresztnev, count(*) from hajo.s_ugyfel
join hajo.s_megrendeles on ugyfel = ugyfel_id
group by vezeteknev, keresztnev
order by count(*) desc
fetch first 4 rows only

--4. feladat
create table s_kikoto_email (
    kikoto_id varchar2(10) references s_kikoto(kikoto_id),
    email varchar2(200),
    constraint osszk primary key(kikoto_id, email)
)

--5. feladat
alter table s_kikoto_telefon drop constraint ideanev

--6. feladat
insert into s_hajo
select h.* from hajo.s_hajo h
join hajo.s_hajo_tipus on hajo_tipus = hajo_tipus_id
where max_kontener_dbszam <= 10

--7. feladat
drop table s_helyseg;
drop table s_orszag;
create table s_helyseg as select * from hajo.s_helyseg;
create table s_orszag as select * from hajo.s_orszag;

update s_helyseg set lakossag = round(lakossag / 2)
where helysegnev in (
    select helysegnev from hajo.s_helyseg h
    join hajo.s_orszag o on o.orszag = h.orszag
    where foldresz = 'Afrika'
) and lakossag > 500000

--8. feladat
create view nezet as
select kikoto_id, helysegnev, orszag, count(ut_id) as utak_szama from hajo.s_kikoto
join hajo.s_helyseg on helyseg = helyseg_id
full join hajo.s_ut on kikoto_id = erkezesi_kikoto
group by kikoto_id, helysegnev, orszag

--9. feladat
--create view nezet as
select unique kikoto_id, helysegnev, orszag from hajo.s_kikoto
join hajo.s_helyseg on helyseg = helyseg_id
join hajo.s_megrendeles on erkezesi_kikoto = kikoto_id
where megrendeles_id in (
    select megrendeles from hajo.s_hozzarendel
    where rakomanysuly = (
        select max(rakomanysuly) from hajo.s_hozzarendel
    )
)

--10. feladat
grant delete on s_orszag to panovics;
revoke delete on s_orszag from panovics
