import streamlit as st
from FootballMatchPredictor import fetch_data, process_data  # Adjust the import based on your script's name

# Fetch and process data
url = 'http://api.clubelo.com/Fixtures'
data = fetch_data(url)
processed_data = process_data(data)

# Streamlit app
st.title('Football Match Predictor')

# Dropdown to select the Game ID
game_id = st.selectbox('Select the Game ID:', processed_data['Game_ID'].unique())

# Button to make the prediction
if st.button('Predict'):
    # Find the match details
    match_details = processed_data.loc[processed_data['Game_ID'] == game_id, ['Home Win %', 'Away Win %', 'Draw %']].values[0]
    
    # Display the results
    st.write(f'Teams: {game_id}')
    st.write(f'Home Win %: {match_details[0]}')
    st.write(f'Away Win %: {match_details[1]}')
    st.write(f'Draw %: {match_details[2]}')
