import requests
user_id = "hpmu6h0ms4l2w600tc3v26oqd"
SPOTIFY_CREATE_PLAYLIST_URL = f"https://api.spotify.com/v1/users/{user_id}/playlists"
ACCESS_TOKEN = "BQCmLvzGNveIRwBFvElUJxoPoTirJGvopcY9liaeli4mV0gdqL5sRv7K5taM3hSOO2EopoMdrNPRsDAlnPVUM-RqWT_oxu6sYkpUjz5Xp9PhNzMAefeEAojhOSihclWbP1lAzFTy1s1BkrBG8EJIRaLEyNKmYhnmFicPIJQQtYmRpSETIco-a5Iq-ce6jz-KI1zbJZ2MqOsuBwflhDYK0EMXwHpjuzpPv90gy8UPOXZvKVwB4hROYP4MFb8Stu8l"

def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
        "name": name,
        "description": "New playlist description",
        "public": public
        }
    )
    json_resp = response.json()
    return json_resp

def main():
    playlist = create_playlist_on_spotify(
        name="My Private Playlist",
        public=False
    )

    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()
