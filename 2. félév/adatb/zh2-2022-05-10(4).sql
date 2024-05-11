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
