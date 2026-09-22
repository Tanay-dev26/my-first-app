import streamlit as st
from google import genai
from dotenv import load_dotenv
import time

load_dotenv()

client = genai.Client()

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@600;700&family=Poppins:wght@400;500&display=swap');

    .vacation-bubble-outer {
        position: relative;
        padding: 8px;
        margin-bottom: 30px;
        /* Striped vacation border pattern without emojis */
        background: repeating-linear-gradient(
            -45deg,
            #ff5e62,
            #ff5e62 18px,
            #ff9966 18px,
            #ff9966 36px,
            #4ac29a 36px,
            #4ac29a 54px,
            #bdc3c7 54px,
            #bdc3c7 72px
        );
        border-radius: 36px;
        box-shadow: 0 12px 28px rgba(0, 0, 0, 0.2);
    }

    .vacation-bubble-card {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 32px 36px;
        border-radius: 30px;
        color: white;
        text-align: center;
        /* Glossy & 3D soft bubble depth lighting */
        box-shadow: 
            inset 0 6px 14px rgba(255, 255, 255, 0.45),
            inset 0 -8px 16px rgba(0, 0, 0, 0.45),
            0 10px 25px rgba(30, 60, 114, 0.35);
        border: 2px solid rgba(255, 255, 255, 0.3);
    }

    /* Funky 3D Layered Title */
    .funky-title {
        font-family: 'Fredoka', cursive, sans-serif;
        font-size: 2.6rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        margin: 0;
        color: #ffffff;
        text-transform: uppercase;
        /* Funky 3D text shadow depth effect */
        text-shadow: 
            2px 2px 0px #ff5e62,
            4px 4px 0px #ff9966,
            6px 6px 0px #2a5298,
            8px 8px 15px rgba(0, 0, 0, 0.5);
        transform: rotate(-1.5deg);
        display: inline-block;
    }

    .subtitle-text {
        font-family: 'Poppins', sans-serif;
        margin-top: 14px;
        margin-bottom: 0;
        opacity: 0.95;
        font-size: 1.05rem;
        letter-spacing: 0.5px;
        color: #f0f4f8;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    </style>

    <div class="vacation-bubble-outer">
        <div class="vacation-bubble-card">
            <h1 class="funky-title">🌐Voyager Travel Assistant</h1>
            <p class="subtitle-text">
                🌍Your AI itinerary planner, ✈️flight tracker, and local expert.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)