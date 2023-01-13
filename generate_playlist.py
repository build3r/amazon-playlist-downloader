import pandas as pd #to write as CSV or any other format
import json
json_data = json.loads(open('<path>/playlist.json').read()) ## see readme on how to generate this file
play_list_json = json_data['methods'][2]['template']['widgets'][0]['items'] #kind of fragile, check data if it has changed
print(len(play_list_json)) #verify you all songsa are here
lst = []
cols=['name','artist','album']
for it in play_list_json:
    name = it['primaryText'] #name of the song
    artist = it['secondaryText1'] # Artist
    album = it['secondaryText2'] #Album
    lst.append([name, artist, album])
print(f"Extracted {len(lst)} songs")
playslist = pd.DataFrame(lst, columns=cols) 
playslist.to_csv("all_amazon_playlist.csv") #save to csv file
print(f"Successfully created Playlist!")

