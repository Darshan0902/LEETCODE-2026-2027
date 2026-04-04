# Write your MySQL query statement below
select query_name, round(avg(rating/position),2)as quality , round((SUM(case when rating < 3 then 1 else 0 end)/count(*) * 100),2) AS poor_query_percentage
From Queries 
group by query_name