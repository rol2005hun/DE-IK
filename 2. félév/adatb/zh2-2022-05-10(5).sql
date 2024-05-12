--1. feladat
select o.orszag, o.lakossag, nvl(helysegnev, 'nem ismert') from hajo.s_orszag o
left join hajo.s_helyseg h on o.orszag = h.orszag
where o.lakossag < (
    select lakossag from hajo.s_orszag
    where orszag = 'Magyarország'
)
order by lakossag desc

--2. feladat
select h.nev as hajonev, max_sulyterheles, ht.nev as tipusnev from hajo.s_hajo h
join hajo.s_hajo_tipus ht on hajo_tipus = hajo_tipus_id
where hajo_id not in (
    select hajo from s_ut
)

--3. feladat
select nev, count(*) from hajo.s_hajo
join hajo.s_ut on hajo_id = hajo
group by nev
order by count(*) desc
fetch first 3 rows only

--4. feladat
create table s_szemelyzet (
    azonosito number(5) constraint pk primary key,
    vezeteknev varchar2(40) constraint nn not null,
    keresztnev varchar2(40) constraint nn2 not null,
    szuldat date,
    email varchar2(200),
    tartozik varchar2(10) references s_hajo(hajo_id) constraint nn3 not null,
    constraint osszk unique(vezeteknev, keresztnev, szuldat)
)

--5. feladat
alter table s_ugyfel modify email varchar2(50)

--6. feladat
drop table s_kikoto;
create table s_kikoto as select * from hajo.s_kikoto;
delete from s_kikoto where ( kikoto_id, helyseg, leiras ) in (
    select k.* from hajo.s_kikoto k
    join hajo.s_helyseg on helyseg = helyseg_id
    where leiras like '%szárazdokk%' and (orszag = 'Olaszország' or
    orszag = 'Líbia')
)

--7. feladat
drop table s_kikoto;
create table s_kikoto as select * from hajo.s_kikoto;
update s_kikoto set leiras = helyseg || ', ' || leiras
where kikoto_id in (
    select kikoto_id from hajo.s_kikoto
    where leiras like '%terminálterület: nagy,%'
)

--8. feladat
create view nezet as
select k.kikoto_id, orszag, helysegnev, count(kt.kikoto_id) as telszamok from hajo.s_kikoto k
join hajo.s_helyseg on helyseg = helyseg_id
left join hajo.s_kikoto_telefon kt on k.kikoto_id = kt.kikoto_id
group by k.kikoto_id, orszag, helysegnev

--9. feladat
select unique kikoto_id, helysegnev, orszag from hajo.s_kikoto
join hajo.s_helyseg on helyseg_id = helyseg
join hajo.s_ut on indulasi_kikoto = kikoto_id
join hajo.s_szallit sz on ut = ut_id
join hajo.s_hozzarendel h on (h.megrendeles = sz.megrendeles and sz.kontener = h.kontener)
where rakomanysuly = (
    select max(rakomanysuly) from hajo.s_hozzarendel
)

--10. feladat
grant insert on s_megrendeles to public;
revoke insert on s_megrendeles from public;
