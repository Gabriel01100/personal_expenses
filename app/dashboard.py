import os
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dotenv import load_dotenv
load_dotenv()

engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

#data pandas load
df = pd.read_sql("SELECT * FROM expenses", engine)

#month expenses prepare
df['month'] = pd.to_datetime(df['expense_date']).dt.to_period('M').astype(str)
monthly_totals = df.groupby('month')['amount'].sum().reset_index()

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Personal Expense Dashboard"


# Figures
fig1 = px.bar(df, x="category", y="amount", color="category", title="Expenses by Category")
fig1.update_layout(paper_bgcolor="white", plot_bgcolor="#f9f9f9", font=dict(size=14))

fig2 = px.line(df.groupby("month")["amount"].sum().reset_index(),
               x="month", y="amount", title="Monthly Expenses Trend")
fig2.update_layout(paper_bgcolor="white", plot_bgcolor="#f9f9f9", font=dict(size=14))

fig3 = px.pie(df, names="category", values="amount", title="Category Share")
fig3.update_traces(textinfo="percent+label")



app.layout = html.Div([
    html.H1("Personal Expense Dashboard"),

    html.Div([
        html.Div([dcc.Graph(figure=fig1, className="dash-graph")], className="dashboard-card"),
        html.Div([dcc.Graph(figure=fig2, className="dash-graph")], className="dashboard-card"),
        html.Div([dcc.Graph(figure=fig3, className="dash-graph")], className="dashboard-card")
    ], className="dashboard-container"),

    html.Div("Created with Dash & PostgreSQL", className="footer")
])

if __name__ == "__main__":
    app.run(debug=True)
