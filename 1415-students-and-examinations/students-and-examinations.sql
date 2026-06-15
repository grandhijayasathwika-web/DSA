# Write your MySQL query statement below
select s.student_id,s.student_name,e.subject_name,count(a.student_id) as attended_exams
from students s cross join subjects e
left join examinations a
on a.student_id=s.student_id 
and a.subject_name=e.subject_name
group by s.student_id,s.student_name,e.subject_name
order by s.student_id,s.student_name,e.subject_name;
