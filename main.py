import streamlit as st
from google import genai
from dotenv import load_dotenv
import time

load_dotenv()

client = genai.Client()
st.set_page_config(
    page_title="Tanay's Travel Assistant",      # This changes the browser tab text
    page_icon="🚀",                  # Optional: Changes the browser tab favicon
    layout="centered"                   # Optional: "centered" or "wide"
)

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
st.markdown(
        """
        <style>
        @keyframes border-glow {
            0% { border-left-color: #3b82f6; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
            50% { border-left-color: #10b981; box-shadow: -3px 0 8px rgba(16, 185, 129, 0.3); }
            100% { border-left-color: #3b82f6; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
        }

        @keyframes dot-pulse {
            0%, 100% { opacity: 0.3; transform: scale(0.9); }
            50% { opacity: 1; transform: scale(1.1); }
        }

        .travel-box {
            background-color: rgba(248, 250, 252, 0.8);
            border: 1px solid rgba(226, 232, 240, 0.8);
            border-left: 4px solid #3b82f6;
            border-radius: 6px;
            padding: 10px 14px;
            margin: 10px 0 18px 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 0.82rem;
            line-height: 1.4;
            animation: border-glow 2.5s infinite ease-in-out;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .live-dot {
            width: 8px;
            height: 8px;
            background-color: #10b981;
            border-radius: 50%;
            display: inline-block;
            flex-shrink: 0;
            animation: dot-pulse 1.8s infinite ease-in-out;
        }

        .travel-box-content {
            color: #334155;
        }

        .travel-box-title {
            font-weight: 700;
            color: #0f172a;
            margin-right: 6px;
        }

        /* Streamlit Dark Theme Support */
        @media (prefers-color-scheme: dark) {
            .travel-box {
                background-color: rgba(30, 41, 59, 0.5);
                border-color: rgba(51, 65, 85, 0.8);
            }
            .travel-box-content { color: #cbd5e1; }
            .travel-box-title { color: #f8fafc; }
        }
        </style>

        <div class="travel-box">
            <span class="live-dot"></span>
            <div class="travel-box-content">
                <span class="travel-box-title">One-Stop Travel Hub:</span>
                Seamless flight search, hotel finder    & itinerary planning.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        /* Main background applied to the parent app container */
        .stApp {{
            background: linear-gradient(
                rgba(15, 23, 42, 0.75), 
                rgba(15, 23, 42, 0.75)
            ),
            url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Optional: Light glassmorphism for Streamlit sidebar */
        [data-testid="stSidebar"] {{
            background-color: rgba(15, 23, 42, 0.65) !important;
            backdrop-filter: blur(8px);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

travel_bg_url = "https://images.unsplash.com/photo-1488646953014-85cb44e25828"
set_background(travel_bg_url)

location=st.text_input("Enter your travel destination (e.g., Paris, Tokyo):")
days_nr=st.number_input("Enter number of days for the trip:", min_value=1, max_value=30, value=2)
budget=st.selectbox("Select your budget type:", ["Low", "Medium", "High"])
travel_type=st.selectbox("Select your travel type:", ["Solo", "Couple", "Family", "Group"])
month_visit=st.multiselect("Select the month(s) you plan to visit:",
                          ["January", "February", "March", "April", "May", "June",
                           "July", "August", "September", "October", "November", "December"])
start_loc=st.text_input("Enter your starting location (e.g., New York, London):")
currency=st.selectbox("Select your preferred currency for cost breakdown:", ["USD", "EUR", "GBP", "INR", "JPY", "AUD"])



prompt = f"""You are a Travel Planner, User is saying he/she wants to 
go to {location} and for {days_nr} days , he is on a budget of type {budget}
Travel Type is :  {travel_type}
Plan a trip and suggest some local attractions, restaurants, and activities based on the travel 
type and budget.Provide probale flight options from {start_loc} to {location} and accommodation suggestions.
Provide a brief itinerary for each day and travel tips.
Make sure to include any cultural or seasonal considerations for the destination as per Months of Visit:{', '.join(month_visit)}.
Also,add relavent links for more info about that place which are official and aunthentic.Add emojis to every bullet point at 
the starting which will make the user feel good after seeing it.
Give the estimated breakdown of cost for every point covered in the data and provide total cost in the last.
(Probable costs in {currency} and in tabular format) """


if st.button("Plan Trip", type="primary"):
    interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt
        )
    
    with st.spinner("Wait for it...", show_time=True):
        time.sleep(5)
    with st.skeleton(height=100):
        time.sleep(5)
        

    st.snow()
    st.success("Trip planned successfully!")
    st.write(interaction.output_text)