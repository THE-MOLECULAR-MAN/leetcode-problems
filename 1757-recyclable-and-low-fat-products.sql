-- Tim H 2023
-- Problem: 1757
-- https://leetcode.com/problems/recyclable-and-low-fat-products/description/
SELECT 
  product_id 
FROM 
  Products 
where 
  low_fats = 'Y' 
  and recyclable = 'Y'
