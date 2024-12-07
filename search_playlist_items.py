#search_playlist_items.py

import googleapiclient.discovery
import googleapiclient.errors
import json
import os


api_service_name = "youtube"
api_version = "v3"


youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

def get_all_channel_tutorials(file_path, playlistId_argument):

    with open(playlistId_argument, 'r') as file:
        playlistIds = json.load(file)

    if os.path.exists(file_path) and os.path.getsize(file_path) != 0:
        print(f"File {file_path} exists.")
        with open(file_path, 'r') as file:
            all_tutorials = json.load(file)
        return all_tutorials
    else:

        all_tutorials = {}
        counter = 0
            
        for playlist in playlistIds:

            request = youtube.playlistItems().list(
                    part="snippet",
                    maxResults=50,
                    playlistId=playlist,
                    fields = 'items(snippet/title, snippet/resourceId/videoId)'
                )

            response = request.execute() #dict type

            for tutorial in response.get('items'):
                all_tutorials[tutorial['snippet']['resourceId']['videoId']] = tutorial['snippet']['title'] #dictionary with videoID and tutorial title

            counter += 1

            if counter == 8000:
                break
    
        with open(file_path, 'w') as file:
            json.dump(all_tutorials, file)
        all_tutorials_json = json.dumps(all_tutorials, indent=4)
        print(all_tutorials_json)
        return all_tutorials





#next: loop through the different playlists to get the playlists items for them.
# for playlist_ID in result from the search_channel_playlists
# save the songs in a list (use extend), and then once gone through all the channels, dump in json file
# search through the 
