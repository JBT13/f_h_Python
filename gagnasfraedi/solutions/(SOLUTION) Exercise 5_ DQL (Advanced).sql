--  Copyright (C) 2016-2026, Björn Þór Jónsson

-- Query 13
select P.ID, P.name, count(*)
from People P 
    join Results R on P.ID = R.peopleID
    join Sports S on S.ID = R.sportID
where R.result = S.record
group by P.ID, P.name
having count(distinct S.ID) > 1;

-- Query 14

-- Correlated subquery, must repeatedly compute max for each row
select distinct P.ID, P.name, P.height, R.result, S.name, case (R.result = S.record) when true then 'Yes' else 'No' end as "record?"
from People P, Results R, Sports S
where P.ID = R.peopleID
  and S.ID = R.sportID
  and R.result = (
    select max(R1.result)
    from Results R1
    where R1.sportID = R.sportID
);



-- Uncorrelated subquery, can compute max only once
select distinct P.ID, P.name, P.height, R.result, S.name, case (R.result = S.record) when true then 'Yes' else 'No' end as "record?"
from People P, Results R, Sports S
where P.ID = R.peopleID
  and S.ID = R.sportID
  and (S.ID, R.result) in (
    select R1.sportID, max(R1.result)
    from Results R1
    group by R1.sportID
);

-- Query 15

-- Three variants, all logically equal
select P.ID, P.name
from People P
where not exists (
    select *
    from Results R
    where R.peopleID = P.ID
);

select P.ID, P.name
from People P
where P.ID not in (
    select R.peopleID
    from Results R
);

select P.ID, P.name
from People P 
	left join Results R on P.ID = R.peopleID
where R.peopleID is null;

-- Query 16

-- Could also do a sub-query instead of union
select P.ID, P.name
from People P 
    join Results R on P.ID = R.peopleID
    join Sports S on S.ID = R.sportID
where S.name = 'High Jump'
  and S.record = R.result
union
select P.ID, P.name
from People P 
    join Results R on P.ID = R.peopleID
    join Competitions C on C.ID = R.competitionID
where extract(year from C.held) = 2002 
  and extract(month from C.held) = 6;

-- Query 17

-- Could also do intersection instead of the sub-query
select distinct P.ID, P.name
from People P
    join Results R on R.peopleID = P.ID
    join Sports S on R.sportID = S.ID
where R.result = S.record
and P.ID in (
    select P.ID
    from People P
        join Results R on R.peopleID = P.ID
    group by P.ID, P.name
    having count(distinct sportID) = 1
);

-- Query 18

-- First use group by + having to compute the correct data, then just count the rows
select count(*)
from (
	select P.ID, count(distinct C.place)
	from People P
		join Results R on P.ID = R.peopleID
		join Competitions C on C.ID = R.competitionID
	group by P.ID
	having count(distinct C.place) >= 10
) X;

-- Query 19: Counting method

-- Add this row to get a non-empty result
insert into     
Results (peopleID, competitionID, sportID, result) 
values (26, 73, 7, 50.41);

select P.ID, P.name
from People P
	join Results R on P.ID = R.peopleID
	join Sports S on S.ID = R.sportID
where R.result = S.record
group by P.ID, P.name
having count(distinct R.sportID) = (
	select count(*)
	from Sports
);

-- Query 20: Counting method
select 	S.ID, S.name, S.record, min(R.result)
from Sports S 
	join Results R on S.ID = R.sportID
	join Competitions C on R.competitionID = C.ID
group by S.ID
having count(distinct C.place) = (
	select count(distinct C.place)
	from Competitions C
);

