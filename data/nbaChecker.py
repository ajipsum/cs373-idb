import json
import sys
import time

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

nbaGames = None
with open("nbaGames_highlights.json") as json_file:
	nbaGames = json.load(json_file)

sorted_games = sorted(nbaGames, key=lambda game: nbaGames[game]['date'])
print(sorted_games)
print(type(sorted_games))

count = 1
for game in sorted_games:
	actual_nba_game = nbaGames[game]
	# actual_nba_game['id'] = count
	date_String = time.strftime('%m-%d-%Y', time.gmtime(actual_nba_game['date']))
	actual_nba_game['date_string'] = date_String
	count += 1

with open('nbaGames_highlights.json', 'w+') as outfile:
		json.dump(nbaGames, outfile)


# players = None
# with open("nba_players_data.json") as json_file:
#   players = json.load(json_file)

# sorted_players_by_name = sorted(players, key=lambda player: player)
# print(sorted_players_by_name)
# print(type(sorted_players_by_name))

# count = 1
# for player in sorted_players_by_name:
# 	actual_player = players[player]
# 	# print(type(actual_nba_game))
# 	# sys.exit()
# 	actual_player['id'] = count
# 	count += 1

# with open('nba_players_data.json', 'w+') as outfile:
#     json.dump(players, outfile)
