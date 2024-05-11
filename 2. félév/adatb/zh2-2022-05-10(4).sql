--1. feladat
select ht.nev as tipusnev, hajo_tipus_id, h.nev as hajonev, hajo_tipus_id
from hajo.s_hajo_tipus ht
left join hajo.s_hajo h on hajo_tipus = hajo_tipus_id
order by tipusnev, hajonev

--2. feladat
