-- Tim H 2023
-- https://leetcode.com/problems/big-countries/description/

select name, population, area from World

where

    area >= 3000000 OR
    population >= 25000000
    