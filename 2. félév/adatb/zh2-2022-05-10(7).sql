--1. feladat
select unique hajo_id, nev from hajo.s_hajo
left join hajo.s_ut on hajo = hajo_id
where erkezesi_kikoto not in (
    select kikoto_id from hajo.s_kikoto
    join hajo.s_helyseg on helyseg = helyseg_id
    where orszag = 'Franciaország'
)

--2. feladat
select helyseg_id, orszag, helysegnev from hajo.s_helyseg
join hajo.s_ugyfel on helyseg = helyseg_id
where lakossag > 1e6 and months_between(sysdate, szul_dat) / 12 > 50
order by orszag, helysegnev

--3. feladat
select vezeteknev, keresztnev, count(*) as kontener from hajo.s_ugyfel
join hajo.s_megrendeles on ugyfel = ugyfel_id
group by vezeteknev, keresztnev
order by kontener desc nulls last
fetch first 10 rows only

--4. feladat
create table s_hajo_javitas (
    azon varchar2(10) constraint nn not null,
    jav_kezd date,
    jav_vege date,
    jav_ar number(10, 2),
    leiras varchar2(200),
    constraint fk foreign key(azon) references s_hajo(nev),
    constraint pk primary key(azon, jav_kezd),
    constraint megnez check(jav_vege > jav_kezd)
)

--5. feladat
alter table s_kikoto_telefon drop column email;
alter table s_kikoto_telefon add email varchar2(200) default 'nem ismert'

--6. feladat
delete from s_kikoto
where kikoto_id in (
    select kikoto_id from hajo.s_kikoto
    join hajo.s_helyseg on helyseg = helyseg_id
    where leiras like '%szárazdokk%' and (
    orszag = 'Olaszország' or orszag = 'Líbia')
)

--7. feladat
update s_helyseg set lakossag = lakossag * 1.05
where orszag in (
    select orszag from hajo.s_orszag
    where foldresz = 'Ázsia'
)

--8. feladat
create view nezet as
select hajo_tipus_id, ht.nev, count(hajo) as utak from hajo.s_hajo_tipus ht
left join hajo.s_hajo on hajo_tipus = hajo_tipus_id
left join hajo.s_ut on hajo_id = hajo
group by hajo_tipus_id, ht.nev
order by ht.nev

--9. feladat
select kikoto_id, count(*) as utak from hajo.s_kikoto
join hajo.s_ut u on u.indulasi_kikoto = kikoto_id
join hajo.s_ut u2 on u2.erkezesi_kikoto = kikoto_id
group by kikoto_id
having count(*) = (
    select max(ertek) from (
        select kikoto_id, count(*) as ertek from hajo.s_kikoto
        join hajo.s_ut on indulasi_kikoto = kikoto_id
        group by kikoto_id
    )
) or count(*) = (
    select max(ertek) from (
        select kikoto_id, count(*) as ertek from hajo.s_kikoto
        join hajo.s_ut on erkezesi_kikoto = kikoto_id
        group by kikoto_id
    )
)

--10. feladat
grant insert on s_megrendeles to public;
revoke insert on s_megrendeles from public;
