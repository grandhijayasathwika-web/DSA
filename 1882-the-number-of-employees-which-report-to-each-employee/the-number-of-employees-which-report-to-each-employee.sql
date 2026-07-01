# Write your MySQL query statement below
select e.employee_id,e.name,
count(a.employee_id) as reports_count,
round(avg(a.age)) as average_age
from employees a join employees e
on a.reports_to=e.employee_id
group by e.employee_id,e.name
order by e.employee_id
