CREATE DATABASE personal_dashboard;

\c personal_dashboard;

--table for expenses
CREATE TABLE expenses (
    expense_id SERIAL PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    expense_date DATE NOT NULL DEFAULT CURRENT_DATE,
    description TEXT
);

--