## 🎧 MindTune – Mood-Based Music App

MindTune is an intelligent, mood-based music player that uses simulated brainwave signals to detect a user’s mental state—such as Calm, Focused, or Neutral—and plays suitable music playlists accordingly using online platforms like YouTube.
## 🧠 Project Idea

Inspired by Brain-Computer Interface (BCI) concepts, MindTune emulates EEG signals (Alpha and Beta waves) to identify emotional states. Based on the interpreted mood, it dynamically plays a playlist that aligns with the user's mental state, creating a personalized and immersive music experience.
## 🔄 Workflow Overview

    EEG Simulation: Randomized simulation of Alpha and Beta wave patterns.

    Mood Classification:

        High Alpha → Calm

        High Beta → Focused

        `Balanced** → Neutral

    Playlist Mapping: Based on the detected mood, appropriate playlist URLs are selected from platforms like YouTube.

    Web Interface:

        Shows mood status

        Embeds YouTube music player

        Displays track metadata (title, thumbnail, etc.)

    Playback Controls: Basic play/pause/next functionality embedded into the player.

## 🚀 Tech Stack

    Python 🐍

    Flask 🌐 – Lightweight web framework

    NumPy 🔢 – Simulating brainwave values

    HTML/CSS 🎨 – Frontend design

    JavaScript 🎬 – Embedding and controlling YouTube player

    YouTube Data API (Planned) 📺 – For dynamic playlist fetching

## 📦 Setup Instructions

Clone the repository

    git clone https://github.com/JANE7J/mindtune-music-player.git
    cd mindtune-music-player

Create and activate virtual environment

    python -m venv mindtune-env
    mindtune-env\Scripts\activate   # For Windows

Install dependencies

    pip install -r requirements.txt

Run the application

    python app.py

    Open your browser and visit: http://127.0.0.1:8888

⚠️ Notes

    This version simulates EEG signals. Real device integration is planned.

    Currently supports YouTube playlists using embed links.

## 💡 Future Enhancements

🎧 Integrate with real EEG devices like Muse/OpenBCI.
🔁 Mood-tracking history and session logs.

    🎯 Personalized recommendations based on usage.

    🔍 Auto-fetch playlists using YouTube Data API.

    📱 Mobile-optimized UI for better accessibility.
