/* Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) 
as both their first and last characters. Your result cannot contain duplicates. */

select distinct city
from station
where left(city,1) in ('a','e','i','o','u')
    and right(city, 1) in ('a','e','i','o','u')

/* Query the Name of any student in STUDENTS who scored higher than  Marks. 
Order your output by the last three characters of each name. If two or more 
students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), 
secondary sort them by ascending ID. */

SELECT NAME
FROM STUDENTS
WHERE MARKS > 75
ORDER BY RIGHT(NAME,3),ID ASC

/* Caso de los Triangulos */

SELECT CASE
            WHEN A + B > C AND B + C > A AND A + C > B THEN
                CASE 
                    WHEN A = B AND B = C THEN 'Equilateral'
                    WHEN A = B OR B = C OR A = C THEN 'Isosceles'
                    ELSE 'Scalene'
                END
            ELSE 'Not A Triangle'
        END
FROM TRIANGLES;

-- Caso de Profesiones agregar letra y contar totales
--Query1
SELECT CONCAT(Name, "(", LEFT(Occupation, 1), ")") 
FROM OCCUPATIONS
ORDER BY Name;

-- Query2
SELECT
CONCAT("There are a total of ", COUNT(Occupation), " ", 
       LOWER(Occupation), "s.") AS occurences
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY occurences;


