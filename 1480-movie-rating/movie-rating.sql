# Write your MySQL query statement below
(select u.name as results
from users u join movierating m
on u.user_id=m.user_id
group by u.user_id
order by count(*) desc,u.name
limit 1)
UNION ALL
(select m.title as results
from movies m join movierating mr
on m.movie_id=mr.movie_id
where mr.created_at between '2020-02-01' and '2020-02-29'
group by m.movie_id
order by avg(mr.rating) desc,m.title
limit 1);
