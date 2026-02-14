-- Business Queries for Sales Data

-- 1. Top 5 transactions by amount
SELECT Transaction_ID, Customer_Name, Amount, Category, Purchase_Date
FROM sales
ORDER BY Amount DESC
LIMIT 5;

-- 2. Total revenue and average transaction value per category
SELECT Category, 
       COUNT(*) as Transaction_Count,
       SUM(Amount) as Total_Revenue,
       AVG(Amount) as Avg_Transaction_Value
FROM sales
GROUP BY Category
ORDER BY Total_Revenue DESC;

-- 3. Monthly sales trend (Revenue)
SELECT strftime('%Y-%m', Purchase_Date) as Month,
       SUM(Amount) as Monthly_Revenue,
       COUNT(*) as Monthly_Transactions
FROM sales
GROUP BY Month
ORDER BY Month;

-- 4. Top 5 customers by total spend
SELECT Customer_Name, 
       SUM(Amount) as Total_Spent,
       COUNT(*) as Purchase_Count
FROM sales
GROUP BY Customer_Name
ORDER BY Total_Spent DESC
LIMIT 5;

-- 5. Average transaction value by age group
SELECT 
    CASE 
        WHEN Age < 25 THEN '18-24'
        WHEN Age < 35 THEN '25-34'
        WHEN Age < 45 THEN '35-44'
        WHEN Age < 55 THEN '45-54'
        ELSE '55+'
    END as Age_Group,
    COUNT(*) as Transaction_Count,
    AVG(Amount) as Avg_Amount
FROM sales
GROUP BY Age_Group
ORDER BY Age_Group;

-- 6. Most popular categories by volume
SELECT Category, COUNT(*) as Count
FROM sales
GROUP BY Category
ORDER BY Count DESC;
