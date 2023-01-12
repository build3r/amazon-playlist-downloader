import pandas as pd #to make parsing easier
import json
json_data = json.loads(open('<path>/playlist.json').read()) ## see read me how to generate this file
play_list_json = json_data['methods'][2]['template']['widgets'][0] #kind of fragile, check data if it has changed
all = pd.json_normalize(play_list_json)['items'][0]
print(len(all)) #verify you all songsa are here
lst = []
cols=['name','artist','album']
for it in all:
    name = it['primaryText'] #name of the song
    artist = it['secondaryText1'] # Artist
    album = it['secondaryText2'] #Album
    lst.append([name, artist, album])
playslist = pd.DataFrame(lst, columns=cols) 
playslist.to_csv("all_amazon_playlist.csv") #save to csv file
print("Extraction Successful")
