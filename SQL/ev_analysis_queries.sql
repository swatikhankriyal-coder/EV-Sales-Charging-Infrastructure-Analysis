CREATE DATABASE ev_project ;
USE ev_project;
SHOW TABLES;
DESCRIBE ev_bi;
  SELECT * FROM ev_bi;
-- 1. Which states have the highest EV adoption?
SELECT State, 
EV_Sales_Quantity FROM ev_bi
ORDER BY EV_Sales_Quantity DESC;
-- 2.  Which states have the strongest charging infrastructure?
SELECT State, Charging_Stations 
FROM ev_bi 
ORDER BY Charging_Stations DESC;
-- 3.Which States have the highest infrastructure gap? 
SELECT State,
       EV_Sales_Quantity,
       Charging_Stations,
       EV_per_Charging_Station
FROM ev_bi
WHERE Charging_Stations > 0
ORDER BY EV_per_Charging_Station DESC;

-- 4.Which are the top 10 states with highest EV sales in india 
SELECT *
FROM ev_bi 
ORDER BY  EV_Sales_Quantity DESC
LIMIT 10;
-- 5.Which are the top 10 states with the highest number of EV charging stations in India?-- 
SELECT *
FROM ev_bi 
ORDER BY  Charging_Stations DESC
LIMIT 10;
-- 6.Which states have fewer charging stations than the national average?
SELECT * FROM ev_bi
WHERE Charging_Stations<
(SELECT AVG (Charging_Stations) FROM ev_bi);
--  7.Which states have the EV sales higher than the national average?
SELECT* FROM ev_bi 
WHERE EV_Sales_Quantity> 
(SELECT AVG (EV_Sales_Quantity) FROM ev_bi );
-- 8.What is the average EV sales across all states in India ?
SELECT AVG(EV_Sales_Quantity) AS Average_EV_Sales
FROM ev_bi;
-- 9. -- What is the average number of charging stations across all state in india ?
SELECT SUM(EV_Sales_Quantity)
FROM ev_bi;
-- 10.What is the total Ev sales across all states in india?
SELECT SUM(EV_Sales_Quantity)
FROM ev_bi;
-- 11.What is the toatal no. of charging stations across all states in india?
SELECT SUM(Charging_Stations)
FROM ev_bi;
-- 12.Which state have high EV sales but below average charging stations?
SELECT *
FROM ev_bi
WHERE EV_Sales_Quantity >
(SELECT AVG(EV_Sales_Quantity)FROM ev_bi)
AND Charging_Stations <
(SELECT AVG(Charging_Stations)FROM ev_bi);
