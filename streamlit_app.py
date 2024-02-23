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
    # Define the match details
    home_team = match_details['Home']
    away_team = match_details['Away']
    home_win_percent = match_details['Home Win %']
    away_win_percent = match_details['Away Win %']
    draw_percent = match_details['Draw %']
    
    # Custom HTML and CSS to style the output
    html_content = f"""
    <div style="background-color: #1b3752; padding: 10px; border-radius: 10px; text-align: center; color: #1b3752; font-family: sans-serif;">
        <h2 style="color: white; text-shadow: 2px 2px 4px #000000;">MATCH PREDICTION</h2>
        <div style="margin: 20px; padding: 20px; background: #FFFFFF; border-radius: 10px; box-shadow: 2px 2px 4px #000000;">
            <h3 style="margin-bottom: 0; color: #1b3752;">{home_team} vs {away_team}</h3>
        </div>
        <div style="display: flex; justify-content: space-around; align-items: center; padding: 20px;">
            <div style="flex-grow: 1;">
                <h4>{home_team}</h4>
                <div style="height: 100px; width: 100px; background: #FFFFFF; border-radius: 50%; box-shadow: 2px 2px 4px #000000; margin: auto;">
                    <p style="padding-top: 40px;">{home_win_percent}</p>
                </div>
            </div>
            <div style="flex-grow: 1;">
                <h4>DRAW</h4>
                <div style="height: 100px; width: 100px; background: #FFFFFF; border-radius: 50%; box-shadow: 2px 2px 4px #000000; margin: auto;">
                    <p style="padding-top: 40px;">{draw_percent}</p>
                </div>
            </div>
            <div style="flex-grow: 1;">
                <h4>{away_team}</h4>
                <div style="height: 100px; width: 100px; background: #FFFFFF; border-radius: 50%; box-shadow: 2px 2px 4px #000000; margin: auto;">
                    <p style="padding-top: 40px;">{away_win_percent}</p>
                </div>
            </div>
        </div>
        <p color: #d1dae3; font-size: smaller;">Created by Ezra Richard</p>
    </div>
    """
    
    # Use st.markdown to display the HTML content
    st.markdown(html_content, unsafe_allow_html=True)

#st.markdown('<p style="position: fixed; bottom: 10px; left: 10px; color: gray; font-size: smaller;">Created by Ezra Richard</p>', unsafe_allow_html=True)

