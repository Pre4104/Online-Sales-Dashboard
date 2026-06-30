# Online Sales Dashboard with AI Insights

A small data analysis + dashboard project built on the [Online Sales Data dataset](https://www.kaggle.com/datasets/samruddhi4040/online-sales-data) from Kaggle. It merges order and order-detail data, visualizes sales and profit with Plotly, generates a natural-language insight summary using the Gemini API, and displays everything in a Dash web app.

## What it does

- Downloads the dataset via `kagglehub`
- Merges `Orders.csv` and `Details.csv` on `Order ID`
- Plots sales by sub-category and profit by category with Plotly
- Sends summary statistics to Gemini (`gemini-2.0-flash`) and prints back an AI-generated insight
- Renders the insight and a chart in a Dash app

## Setup

1. Clone the repo and install dependencies:

   ```bash
   pip install kagglehub dash plotly pandas google-genai
   ```

2. Set your Gemini API key as an environment variable (never commit it to the repo):

   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open the local URL Dash prints in the terminal (usually `http://127.0.0.1:8050`).

## Notes

- The Kaggle dataset download requires Kaggle API credentials configured for `kagglehub` (see [kagglehub docs](https://github.com/Kaggle/kagglehub)).
- Replace the `model` argument in `generate_content` if you'd like to use a different Gemini model.

## License

MIT
