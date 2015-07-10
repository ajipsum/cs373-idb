import json

# json_data = None
# with open("nba_players_data.json") as json_file:
#   json_data = json.load(json_file)


# for key in json_data:
#   player_dic = json_data[key]
#   player_youtube_links = player_dic['youtube_links']
#   new_links = []
#   for i in range(len(player_youtube_links)):
#     link = player_youtube_links[i]
#     embed_link = "https://www.youtube.com/embed/" + link[link.index('=') + 1:]
#     print(embed_link)
#     new_links += [embed_link]
#   # print(new_links)
#   player_dic['youtube_links'] = new_links

# with open('test.json', 'w+') as outfile:
#   json.dump(json_data, outfile)

json_data = None
with open("nbaGames.json") as json_file:
  json_data = json.load(json_file)


