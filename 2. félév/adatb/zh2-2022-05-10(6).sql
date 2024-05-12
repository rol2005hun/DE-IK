--1. feladat
select unique hajo_id, nev from hajo.s_hajo
join hajo.s_ut on hajo = hajo_id
join hajo.s_kikoto on erkezesi_kikoto = kikoto_id
join hajo.s_helyseg on helyseg = helyseg_id
where orszag != 'Franciaország'

--vagy

select unique hajo_id, nev from hajo.s_hajo
join hajo.s_ut on hajo = hajo_id
where erkezesi_kikoto not in (
    select kikoto_id from hajo.s_kikoto
    join hajo.s_helyseg on helyseg = helyseg_id
    where orszag = 'Franciaország'
)

--2. feladat
select unique kikoto_id from hajo.s_kikoto
where kikoto_id in (
    select erkezesi_kikoto from hajo.s_ut
    where indulasi_kikoto = 'It_Cat'
) or kikoto_id in (
    select indulasi_kikoto from hajo.s_ut
    where erkezesi_kikoto = 'It_Cat'
)

--3. feladat
select vezeteknev, keresztnev, count(*) as megr from hajo.s_ugyfel
join hajo.s_megrendeles on ugyfel = ugyfel_id
group by vezeteknev, keresztnev
order by megr desc
fetch first 4 rows only

--4. feladat
create table s_kikoto_email (
    kikoto_id varchar2(10) references s_kikoto(kikoto_id),
    email varchar2(200),
    constraint pk primary key(kikoto_id, email)
)

--5. feladat
alter table s_hajo drop constraint nev
alter table s_hajo_tipus drop constraint nev
drop table s_hajo
drop table s_hajo_tipus
