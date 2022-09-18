from random import randint
import requests

def skip_to_next():
    SKIP_TO_NEXT = 	f"https://api.spotify.com/v1/me/player/next"
    STN_ACCESS_TOKEN = "BQAmBXYPVXjZqF-qvuXrBYxeTuczfGFZSf4RuXaYDngWr4oF35AwFIEp8qXUOcXzK6MEXg3QNGRota1fhw0njEj5yHc9Ev2khh5tt9Z46wL98TWaV1mbZ4X9CdWSC6MKVM-deD5ZN1kdg7uO-_DKYwU9PWg7AvmldXC5v2m4yYJtB22Hd4nJUaurIBYZrbMAYOXp8VA"

    response = requests.post(
        SKIP_TO_NEXT,
        headers={
            "Authorization": f"Bearer {STN_ACCESS_TOKEN}"
        },
        params={"device_id": "337a5a74f4247f040ab6e594c687da4004dfbc07"}
    )

def next_song(past_index, new_mood):
    if new_mood == "happy":
        new_index = randint(1, 4)
    if new_mood == "sad":
        new_index = randint(5, 8)
    if new_mood == "chill":
        new_index = randint(9, 12)
    if new_mood == "angry":
        new_index = randint(13, 16)
    if new_mood == "stressed":
        new_index = randint(17, 20)

    while past_index < new_index:
        skip_to_next()
        past_index += 1
    
    if past_index > new_index:
        past_index = 0
        
    while past_index < new_index:
        skip_to_next()
        past_index += 1

    return past_index




