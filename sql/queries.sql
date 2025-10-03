--total expenses
SELECT category, SUM(amount) AS total 
FROM expenses 
GROUP BY category
ORDER BY total DESC;

--monthly expenses

SELECT TO_CHAR(expense_date, 'YYYY-MM') AS month,
        SUM(amount) AS total
FROM expenses
GROUP BY month 
ORDER BY month;