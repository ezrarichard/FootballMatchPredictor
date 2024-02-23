import requests
import pandas as pd
from io import StringIO

def fetch_data(url):
    """Fetch data from the given URL and return a pandas DataFrame."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if the request failed
    return pd.read_csv(StringIO(response.text))

def process_data(data):
    """Process the data and add calculated columns."""
    # Create 'Game_ID' column
    data['Game_ID'] = data['Home'] + ' vs ' + data['Away']
    
    # Columns to sum for Home, Away, and Draw
    home_to_sum = ['GD=1', 'GD=2', 'GD=3', 'GD=4', 'GD=5', 'GD>5']
    away_to_sum = ['GD<-5', 'GD=-5', 'GD=-4', 'GD=-3', 'GD=-2', 'GD=-1']
    draw_to_sum = ['GD=0']
    
    # Calculate and format percentages
    data['Home Win %'] = (data[home_to_sum].sum(axis=1) * 100).apply(lambda x: f'{x:.2f}%')
    data['Away Win %'] = (data[away_to_sum].sum(axis=1) * 100).apply(lambda x: f'{x:.2f}%')
    data['Draw %'] = (data[draw_to_sum].sum(axis=1) * 100).apply(lambda x: f'{x:.2f}%')
    
    return data

# URL of the API endpoint
url = 'http://api.clubelo.com/Fixtures'
data = fetch_data(url)
processed_data = process_data(data)
