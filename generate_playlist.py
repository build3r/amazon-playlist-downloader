import pandas as pd #to make parsing easier
all = pd.read_json('playlist.json') ## see read me how to generate this file
all = pd.json_normalize(all)
print(len(all)) #verify you all songsa are here
lst = []
cols=['name','artist','album']
for it in all['items']:
    name = it['primaryText'] #name of the song
    artist = it['secondaryText1'] # Artist
    album = it['secondaryText2'] #Album
    lst.append([name, artist, album])
playslist = pd.DataFrame(lst, columns=cols) 
playslist.to_csv("all_amazon_playlist.csv") #save to csv file
