import streamlit as st
from FootballMatchPredictor import fetch_data, process_data  # Adjust the import based on your script's name

# Fetch and process data
url = 'http://api.clubelo.com/Fixtures'
data = fetch_data(url)
processed_data = process_data(data)

# Streamlit app
st.title('Football Match Predictor')

# Step 1: Dropdown to select the Country
selected_country = st.selectbox('Select the Country:', processed_data['Country'].unique())

# Step 2: Filter games based on the selected country for Game ID selection
filtered_games_by_country = processed_data[processed_data['Country'] == selected_country]

# Dropdown to select the Game ID based on the selected country
game_id = st.selectbox('Select the Game ID:', filtered_games_by_country['Game_ID'].unique())

# Find the match details for selected Game ID
match_details = filtered_games_by_country.loc[filtered_games_by_country['Game_ID'] == game_id, ['Home', 'Away', 'Home Win %', 'Away Win %', 'Draw %']].iloc[0]

# Button to make the prediction
if st.button('Predict'):
    # Display the results with the names of the clubs
    st.write(f"Match: {match_details['Home']} vs {match_details['Away']}")
    st.metric(label=f"{match_details['Home']} Win %", value=match_details['Home Win %'])
    st.metric(label=f"{match_details['Away']} Win %", value=match_details['Away Win %'])
    st.metric(label="Draw %", value=match_details['Draw %'])
