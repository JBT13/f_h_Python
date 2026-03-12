-- (A)

select max(B.size)
from beds B;
-- 102

-- (B)

select count(*)
from plants P
        join families F on F.ID = P.familyID
where F.name = 'Thespesia';
-- 18

-- (C)

-- Hint!
select count(*)
from families F;
-- 792

select count(*)
from families F
where F.name like 'A%';
-- 79

-- (D)

-- Hint!
select count(*)
from staff S
        left join plantedin I on S.ID = I.staffID
where I.staffID is null;
-- 11

select count(*)
from staff S
        left join plantedin I on S.ID = I.staffID
where I.staffID is null
        and S.position = 'Senior Planter';
-- 2

-- (E)

select count(*)
from (
	select I.staffID, count(distinct P.familyID)
	from plantedin I
		join plants P on I.plantID = P.ID
	group by I.staffID
	having count(distinct P.familyID) > 50
) X;
-- 24

-- (F)

select sum(number)
from (
	select S.name, count(*) as number
	from staff S
	group by S.name
	having count(*) > 1
) X;
-- 105

-- (G)

-- Hint!
select sum(1.0 * B.size * I.percentage / 100) as sqm
from families F
        join plants P on F.ID = P.familyID
        join plantedin I on P.ID = I.plantID
        join beds B on B.ID = I.bedID
where F.name = 'Thespesia';
-- 66.62000000000003
-- 66.62

select sum(1.0 * B.size * I.percentage / 100) as sqm
from families F
        join plants P on F.ID = P.familyID
        join plantedin I on P.ID = I.plantID
        join beds B on B.ID = I.bedID
where F.name = 'Vicia';
-- 27.3

-- (H)

select distinct(G.name)
from types T 
	join families F on T.ID = F.typeID
	join plants P on F.ID = P.familyID
	join plantedin I on P.ID = I.plantID
	join staff S on S.ID = I.staffID
	join beds B on B.ID = I.bedID
	join gardens G on G.ID = B.gardenID
where T.name = 'epiphyte'
	and S.position = 'Teamleader';
-- "Botanisk Have"
-- "Frederiksberg Have"

-- (I)

select B.description, G.name, sum(I.percentage) as capacity
from gardens G
	join beds B on B.gardenID = G.ID
	join plantedin I on B.ID = I.bedID
group by G.ID, B.ID
having sum(I.percentage) > 100
order by capacity desc;
-- "northwest"	"Kongens Have"	105
-- ... plus 8 more lines, for 9 lines in total

-- (J)

select G.ID, G.name, count(*)
from gardens G
	join beds B on G.ID = B.gardenID
group by G.ID
having count(*) = (
	select max(bedcount)
	from (
		select count(*) as bedcount
		from gardens G
			join beds B on G.ID = B.gardenID
		group by G.ID
	) X
);
-- 2	"Botanisk Have"	115
