# Personal Expense Dashboard

A professional dashboard to track and visualize personal expenses using **PostgreSQL + Python + Dash + Plotly**.

## Features
- View total expenses by category
- Analyze monthly expenses
- Visualize expense distribution
- PostgreSQL backend for persistence

## Tech Stack
- Python (Pandas, Plotly, Dash)
- PostgreSQL
- dotenv for environment variables

## Setup Instructions
1. Clone the repository:
    git clone https://github.com/Gabriel01100/personal_expenses.git
2. Install dependencies:

    pip install -r requirements.txt
3. Create PostgreSQL database and tables:

    psql -f sql/create_tables.sql

    psql -f sql/insert_data.sql

4. Configure `.env` with your database credentials.
5. Run the dashboard:

    python app/dashboard.py


## Project Structure
- `sql/` → database scripts
- `app/` → Dash application
- `.env` → environment variables
- `requirements.txt` → dependencies
- `README.md` → project documentation
