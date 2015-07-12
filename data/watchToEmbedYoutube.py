import json

nbaGames = None
nbaPlayers = None
with open("nbaGames_highlights.json") as json_file:
  nbaGames = json.load(json_file)
with open("nba_players_data.json") as json_file:
  nbaPlayers = json.load(json_file)

for v in nbaGames:
	need_to_add_games = False
	game = nbaGames[v]
	if game['season'] == '2014':
		youtube_links_list = game['youtube_links']
		new_list = []
		for a in youtube_links_list:
			if 'watch' in a:
				embed_link = "https://www.youtube.com/embed/" + a[a.index('=') + 1:]
				new_list += [embed_link]
				need_to_add_games = True
		if need_to_add_games:
			game['youtube_links'] = new_list

with open('nbaGames_highlights.json', 'w+') as outfile:
    json.dump(nbaGames, outfile)

for v in nbaPlayers:
	need_to_add_players = False
	player = nbaPlayers[v]
	youtube_links_list = player['youtube_links']
	new_list = []
	for a in youtube_links_list:
		if 'watch' in a:
			embed_link = "https://www.youtube.com/embed/" + a[a.index('=') + 1:]
			new_list += [embed_link]
			need_to_add_players = True
	if need_to_add_players:
		player['youtube_links'] = new_list

with open('nba_players_data.json', 'w+') as outfile:
    json.dump(nbaPlayers, outfile)