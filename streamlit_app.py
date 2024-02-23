import streamlit as st
from FootballMatchPredictor import fetch_data, process_data  # Adjust the import based on your script's name

# Fetch and process data
url = 'http://api.clubelo.com/Fixtures'
data = fetch_data(url)
processed_data = process_data(data)

# Streamlit app setup
st.title('Football Match Predictor')

# Dropdown to select the Country
selected_country = st.selectbox('Select the Country:', processed_data['Country'].unique())

# Filter games based on the selected country
filtered_games = processed_data[processed_data['Country'] == selected_country]

# Dropdown to select the Game ID based on the selected country
game_id = st.selectbox('Select the Game ID:', filtered_games['Game_ID'].unique())

# Button to make the prediction
if st.button('Predict'):
    # Find the match details for the selected game
    match_details = filtered_games.loc[filtered_games['Game_ID'] == game_id, ['Home Win %', 'Away Win %', 'Draw %']].values[0]
    
    # Display the results using st.metric
    st.metric(label="Teams", value=game_id)
    st.metric(label="Home Win %", value=match_details[0])
    st.metric(label="Away Win %", value=match_details[1])
    st.metric(label="Draw %", value=match_details[2])
