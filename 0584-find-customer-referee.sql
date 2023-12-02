-- Tim H 2023
-- https://leetcode.com/problems/find-customer-referee/description/
select name from Customer
where
    referee_id IS NULL OR referee_id <> 2