import kagglehub

# Download latest version
path = kagglehub.dataset_download("samruddhi4040/online-sales-data")

print("Path to dataset files:", path)

# !pip install dash plotly pandas google-genai

"""Loading and Explore Data"""

import pandas as pd
import os

files = os.listdir(path)
print(files)
details_path = os.path.join(path, 'Details.csv')
orders_path = os.path.join(path, 'Orders.csv')

details_df = pd.read_csv(details_path)
orders_df = pd.read_csv(orders_path)

details_df.head()
orders_df.head()

# Merge into a single dataframe (this is the dataframe used everywhere below)
df = pd.merge(orders_df, details_df, on='Order ID', how='inner')
df.head()
df.info()
df.describe()

import plotly.express as px

subcat_sales = df.groupby('Sub-Category')['Amount'].sum().reset_index()
fig1 = px.bar(subcat_sales, x='Sub-Category', y='Amount', title='Sales by Sub-Category')
fig1.show()

cat_profit = df.groupby('Category')['Profit'].sum().reset_index()
fig2 = px.bar(
    cat_profit,
    x='Category',
    y='Profit',
    title='Profit by Category',
    color='Profit',
    color_continuous_scale='RdYlGn'
)
fig2.show()

"""generate ai insight from data"""

import os as _os
from google import genai

# Don't hardcode API keys in source — read from an environment variable instead.
# Set this in your shell or Colab secrets: os.environ["GEMINI_API_KEY"] = "..."
api_key = _os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Set the GEMINI_API_KEY environment variable before running this script.")

client = genai.Client(api_key=api_key)

prompt = f"Give insights for the following data:\n{df.describe().to_string()}"

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,  # was the literal string "prompt" before
)

# google-genai responses expose .text directly — no .choices[0].text (that's the OpenAI SDK shape)
ai_insight = response.text.strip()
print(ai_insight)

"""Dash app"""

from dash import Dash, html, dcc

app = Dash(__name__)  # app was never created before

app.layout = html.Div([
    html.H2("AI Insight"),
    html.P(ai_insight),
    dcc.Graph(figure=fig2),  # pick whichever figure you want to display
])

if __name__ == "__main__":
    app.run(debug=True)
