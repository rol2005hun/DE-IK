--1. feladat
select o.orszag, o.lakossag, nvl(helysegnev, 'nem ismert') from hajo.s_orszag o
left join hajo.s_helyseg h on o.orszag = h.orszag
where o.lakossag < (
    select lakossag from hajo.s_orszag
    where orszag = 'Magyarország'
)

--2. feladat
