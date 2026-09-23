# Voyager Travel Assistant

A lightweight AI-powered travel planner built with Streamlit and Google Generative AI. It is designed to help travelers explore destinations, build itineraries, and get quick travel guidance in a friendly, visual interface.

## Websitelink
Url: https://mypersonaltravelassistant.streamlit.app/

## Features

- AI travel recommendations and trip planning
- Stylish Streamlit UI with a vacation-themed design
- Easy setup with environment variables
- Built to work with Google GenAI models

## Project overview

This app uses:

- Python
- Streamlit
- Google GenAI SDK
- python-dotenv

The main entry point is `main.py`.

## Requirements

- Python 3.9+
- pip
- A Google API key for the GenAI service

## Setup

1. Open a terminal in the project folder.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install streamlit python-dotenv google-genai
```

4. Create a `.env` file in the project root and add your API key:

```env
GEMINI_API_KEY=your_api_key_here
```

> If your environment uses a different key name, adjust it to match your setup.

## Run the app

```bash
streamlit run main.py
```

Then open the local URL shown in the terminal in your browser.

## Project structure

```text
travel_assistant/
├── main.py
├── .env
├── README.md
└── .venv/
```

## Notes

- The app currently loads environment variables with `python-dotenv`.
- The core AI client is initialized in `main.py` using the Google GenAI package.
- You can extend this project by adding itinerary generation, destination search, flights, hotels, or travel tips.

## License

This project is provided as a starter app for learning and personal use.
