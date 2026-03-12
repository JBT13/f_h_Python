--  Copyright (C) 2016-2026, Björn Þór Jónsson

-- Query 1
select name, record 
from Sports
order by name;

-- Query 2
select distinct name 
from Sports S 
join Results R on S.ID = R. sportID; 

-- Query 3
select count(distinct R.peopleID)
from Results R; 

-- Query 4

select distinct P.ID, P.Name
from Results R
join People P on P.ID = R.peopleID
join Sports S on S.ID = R.sportID
where R.result = S.record

-- Query 5
select distinct P.ID, P.name
from People P
	join Results R on P.ID = R.peopleID
	join Competitions C on C.ID = R.competitionID
where C.place = 'Hvide Sande' and extract(year from C.held) = 2009;

-- Query 6
select P.name
from People P
where P.name like '% J%sen';

-- Query 7
select P.name, S.name, 
	case when R.result is not null 
	then to_char(100*R.result/S.record, '990D99%') 
	else null 
	end as percentage
from People P 
	join Results R on P.ID = R.peopleID 
	join Sports S on S.ID = R.sportID;

-- Query 8
select count(distinct R.peopleID)
from Results R
where R.result is null;

-- Query 9
select P.ID, P.name
from People P 
    join Results R on P.ID = R.peopleID
group by P.ID
having count(*) >= 20;

-- Query 10
select S.ID, S.name, max(R.result) as maxres
from Sports S
    join Results R on S.ID = R.sportID
group by S.ID, S.name
order by S.ID;

-- Query 11
select S.name, count(distinct R.peopleID) as numathletes
from Results R 
    join Sports S on S.ID = R.sportID
where R.result = S.record
group by S.ID;

-- Question: Because some athletes have records in multiple sports, 
-- so they will be counted multiple times in this query, whereas 
-- they are only counted once in the previous query.


-- Query 12
select P.ID, P.name, max(R.result) as best, S.record-max(R.result) as difference
from People P 
	join Results R on P.ID = R.peopleID 
	join Sports S on S.ID = R.sportID
where S.name = 'Triple Jump'
group by P.ID, P.name, S.record
having count(*) >= 20;

-- formatted:
select P.ID, P.name, max(R.result) as best, 
	to_char(S.record-max(R.result), '0D99') as difference
from People P 
	join Results R on P.ID = R.peopleID 
	join Sports S on S.ID = R.sportID
where S.name = 'Triple Jump'
group by P.ID, P.name, S.record
having count(*) >= 20;

-- Question: Because of how floating-point numbers work.