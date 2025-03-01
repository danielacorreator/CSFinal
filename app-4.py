import streamlit as st
import json

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(45deg, #FF9A9E, #FAD0C4, #FBC2EB, #A6C1EE, #C2E9FB);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: black;
    }
    /* Default text color */
    .stMarkdown {
        color: black !important;
    }
    /* Style black boxes */
    .black-box {
        display: inline-block;
        background-color: black;
        color: white;
        padding: 4px 8px;
        border-radius: 5px;
        font-weight: bold;
    }
    /* Style buttons for muscle groups */
    div.stButton > button {
        background-color: black !important;
        color: white !important;
        border-radius: 10px;
        font-weight: bold;
        padding: 10px;
        width: 100%;
        border: 2px solid white;
    }
    div.stButton > button:hover {
        background-color: white !important;
        color: black !important;
        border: 2px solid black;
    }
    /* Style Exercise headers inside expanders */
    .exercise-header {
        background-color: black;
        color: white;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with open('workouts.json', 'r') as file:
    workouts_data = json.load(file)

def display_workouts(muscle_group):
    selected_workouts = next((item for item in workouts_data if item["muscle_group"] == muscle_group), None)
    
    if not selected_workouts:
        st.warning(f"No workouts found for {muscle_group.capitalize()}")
        return

    st.markdown(f"## 🏋️‍♂️ **{muscle_group.capitalize()} Workouts** 🏋️‍♀️")
    st.markdown("---")

    for i, exercise in enumerate(selected_workouts['workouts'], 1):
        st.markdown(
            f"<div class='exercise-header'>🏅 Exercise #{i}: {exercise['exercise']}</div>",
            unsafe_allow_html=True
        )

        with st.expander(f"Details for {exercise['exercise']}", expanded=False):
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown("**📦 SETS**")
                st.markdown(f"<span class='black-box'>{exercise['sets']}</span>", unsafe_allow_html=True)
            
            with col2:
                st.markdown("**🔁 REPS**")
                st.markdown(f"<span class='black-box'>{exercise['reps']}</span>", unsafe_allow_html=True)
            
            with col3:
                st.markdown("**⏱️ REST**")
                st.markdown(f"<span class='black-box'>{exercise['rest']}</span>", unsafe_allow_html=True)
            
            with col4:
                st.markdown("**🏋️ EQUIPMENT**")
                st.markdown(f"<span class='black-box'>{exercise['weight']}</span>", unsafe_allow_html=True)

            intensity_color = "🔴 **High Intensity**" if exercise['intensity'].lower() == "high" else "🟠 **Medium Intensity**"
            st.markdown(f"**Intensity:** {intensity_color}")

            st.video(exercise['short_video'])

st.markdown(
    """
    <h1 style="text-align: center; font-size: 50px; font-weight: bold; text-transform: uppercase;">
        💪 WELCOME TO YOUR DIGITAL PERSONAL TRAINER!⚡️
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown("---")
st.subheader("🔥 **What do you want to train today?** 🔥")

muscle_groups = {
    '🦵 **Legs**': 'legs',
    '🏋️ **Chest**': 'chest',
    '🥵 **Back**': 'back',
    '👟 **Shoulders**': 'shoulders',
    '💪 **Arms**': 'arms',
    '🤸 **Core**': 'core'
}

cols = st.columns(3)
for i, (display_name, muscle_key) in enumerate(muscle_groups.items()):
    with cols[i % 3]:
        if st.button(display_name, use_container_width=True):
            st.session_state.selected_muscle = muscle_key

if 'selected_muscle' not in st.session_state:
    st.session_state.selected_muscle = 'legs'

display_workouts(st.session_state.selected_muscle)

st.markdown("---")
st.markdown("💡 **Tip:** Maintain proper form and breathe consistently during exercises!")
st.markdown("🚀 **You're one step closer to your fitness goals!** 🔥")


