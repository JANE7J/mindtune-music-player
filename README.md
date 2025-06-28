🎧 MindTune – Mood-Based Music Player

MindTune is a brainwave-inspired music player that simulates EEG signals to determine the user's mental state (Calm, Focused, or Neutral) and plays Spotify playlists accordingly.

🧠 Key Features:-
- 🧪 Simulates EEG brainwave data (Alpha & Beta waves)
- 😌 Classifies mood as:
  - Calm (High Alpha)
  - Focused (High Beta)
  - Neutral (Balanced)
- 🎶 Plays matching Spotify playlists based on the mood
- ⏯️ Controls for play, pause, and skip
- 🎨 Displays current track info and album art
- 🖥️ Simple web interface using Flask

🚀 Tech Stack:-
- Python 🐍
- Flask 🌐
- Spotipy (Spotify Web API wrapper) 🎧
- NumPy 🔢
- HTML & CSS 💻

 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/JANE7J/mindtune-music-player.git
cd mindtune-music-player

2. Create and activate a virtual environment:
python -m venv mindtune-env
mind tune-env\Scripts\activate     # On Windows

3. Install dependencies:
pip install -r requirements.txt

4. Set environment variables:
Create a .env file in the root with:
FLASK_SECRET_KEY=your_flask_secret_key
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback

5.Run the app:
python app.py

Then open http://127.0.0.1:8888 in your browser

📌 Note

    ⚠️ Spotify Premium is required for playback control (play, pause, skip).
    If you're using a free account, you can only view the current playing song.

💡 Future Enhancements

    Integrate with real EEG devices (like Muse or OpenBCI)

    Add recommendation system based on mood history

    Export session logs / mood tracking
