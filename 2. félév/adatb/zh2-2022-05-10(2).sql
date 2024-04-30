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
select  from hajo.s_hajo join hajo.s_ut on hajo = hajo_id
where nev = 'SC Nina'
fetch first 3 rows only
order by 
