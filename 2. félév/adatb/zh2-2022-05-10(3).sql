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
