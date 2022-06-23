import requests
user_id = ""
create_playlist_url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
get_playlist_url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
typ = 'tracks'
rang = "short_term"
val = 0
lim = 50
get_top_url = f'https://api.spotify.com/v1/me/top/{typ}?time_range={rang}&limit={lim}&offset={val}'
access_token = ''

def create_playlist_on_spotify(name,public):
    response = requests.post(
        create_playlist_url,
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "name": name,
            "public":public
        }
    )
    json_resp = response.json()
    return json_resp



def get_user_playlists():
    response = requests.get(get_playlist_url,
    headers={
        "Authorization": f"Bearer {access_token}"
    }
    )
    playlist = response.json()
    return playlist

def get_top():
    response = requests.get(get_top_url,
    headers={
        "Authorization" : f"Bearer {access_token}",
    })
    return response.json()

store = get_user_playlists()

for i in range(len(store)):
    print(store["items"][i]['name'])

create_playlist_on_spotify(name="test",public=False)


x = get_top()

for i in range(lim):
    print(i+1)
    print("Album name: " + x["items"][i]['album']['name']) #album name    
    print("Artist name: " + x["items"][i]['album']['artists'][0]['name']) #artist name
    print("Song name: " + (x['items'][i]['name'])) #Name of the song
    print("-"*50)

