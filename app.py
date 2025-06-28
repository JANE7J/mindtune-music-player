import os
import time
import threading
import numpy as np
from flask import Flask, redirect, request, session, url_for, jsonify
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

SCOPE = "user-library-read user-read-playback-state user-modify-playback-state"

sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    cache_path=".cache"
)

current_mood = "Neutral"

PLAYLISTS = {
    "Calm": "spotify:playlist:37i9dQZF1DX3Ogo9pFvBkY",
    "Focused": "spotify:playlist:37i9dQZF1DXcF6B6QPhFDv",
    "Neutral": "spotify:playlist:37i9dQZF1DXcBWIGoYBM5M"
}

DEVICE_ID = "629db429cd56dd6fc82e640dcd8b23b31760f181"

# ----------------------------------------
# Helper: Get valid Spotify client
# ----------------------------------------
def get_spotify_client():
    token_info = session.get('token_info', None)
    if not token_info:
        return None
    if sp_oauth.is_token_expired(token_info):
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        session['token_info'] = token_info
    return Spotify(auth=token_info['access_token'])

# ----------------------------------------
# Simulated EEG and mood classification
# ----------------------------------------
def simulate_eeg_data():
    alpha = np.random.uniform(5, 15)
    beta = np.random.uniform(10, 30)
    return alpha, beta

def classify_mood(alpha, beta):
    if alpha > beta:
        return "Calm"
    elif beta > alpha:
        return "Focused"
    else:
        return "Neutral"

# ----------------------------------------
# Music control functions
# ----------------------------------------
def play_playlist_for_mood(sp, mood):
    playlist_uri = PLAYLISTS.get(mood, PLAYLISTS["Neutral"])
    devices = sp.devices()
    if devices['devices']:
        sp.start_playback(device_id=DEVICE_ID, context_uri=playlist_uri)
        print(f"Started playing {mood} playlist.")
    else:
        print("No active Spotify device found.")

def pause_music(sp):
    sp.pause_playback(device_id=DEVICE_ID)
    print("Paused playback.")

def play_music(sp):
    sp.start_playback(device_id=DEVICE_ID)
    print("Started/Resumed playback.")

def skip_next(sp):
    sp.next_track(device_id=DEVICE_ID)
    print("Skipped to next track.")

def get_current_track(sp):
    current = sp.current_user_playing_track()
    if current and current['item']:
        track = current['item']
        return {
            "name": track['name'],
            "artist": track['artists'][0]['name'],
            "album_art": track['album']['images'][0]['url']
        }
    return None

# ----------------------------------------
# Background mood updater thread
# ----------------------------------------
def mood_update_loop():
    global current_mood
    while True:
        sp = get_spotify_client()
        if sp:
            alpha, beta = simulate_eeg_data()
            mood = classify_mood(alpha, beta)
            if mood != current_mood:
                current_mood = mood
                print(f"Mood changed to: {mood}")
                play_playlist_for_mood(sp, mood)
        time.sleep(10)

# ----------------------------------------
# Flask Routes
# ----------------------------------------
@app.route('/')
def index():
    sp = get_spotify_client()
    if not sp:
        return redirect(url_for('login'))
    track = get_current_track(sp)
    return f"""
    <h2>Current mood: {current_mood}</h2>
    <h3>Now Playing:</h3>
    <p>{track['name'] if track else 'No song playing'}</p>
    <p>{track['artist'] if track else ''}</p>
    <img src="{track['album_art'] if track else ''}" alt="Album Art" width="200" height="200"><br><br>
    <button onclick="fetch('/play')">Play</button>
    <button onclick="fetch('/pause')">Pause</button>
    <button onclick="fetch('/skip')">Skip</button><br><br>
    <a href='/logout'>Logout</a>
    """

@app.route('/login')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session['token_info'] = token_info
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/devices')
def list_devices():
    sp = get_spotify_client()
    if not sp:
        return "Spotify not authenticated", 401
    devices = sp.devices()
    return jsonify(devices)

@app.route('/mood')
def get_mood():
    return jsonify({"mood": current_mood})

@app.route('/pause')
def pause():
    sp = get_spotify_client()
    if sp:
        pause_music(sp)
    return "Paused"

@app.route('/play')
def play():
    sp = get_spotify_client()
    if sp:
        play_music(sp)
    return "Playing"

@app.route('/skip')
def skip():
    sp = get_spotify_client()
    if sp:
        skip_next(sp)
    return "Skipped"

# ----------------------------------------
# Run the Flask app
# ----------------------------------------
if __name__ == "__main__":
    mood_thread = threading.Thread(target=mood_update_loop)
    mood_thread.daemon = True
    mood_thread.start()
    app.run(port=8888, debug=True)
