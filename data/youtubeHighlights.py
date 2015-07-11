#adds youtube highlight link to each game for season 2014-2015
import requests
import sys
from bs4 import BeautifulSoup
import time
import re
import json

nbaGames = None
nbaTeams = None
with open("nbaGames.json") as json_file:
  nbaGames = json.load(json_file)
with open("nbaTeams.json") as json_file:
  nbaTeams = json.load(json_file)

i = 1
for game in nbaGames:
	game_info = nbaGames[game] #is dictionary
	if(game_info['season'] == '2014'):


		#https://www.youtube.com/results?search_query=lakers+vs+rockets+2014-10-28
		home_id = game_info['home_id']
		away_id = game_info['away_id']
		home_name = nbaTeams[str(home_id)]['team_name']
		away_name = nbaTeams[str(away_id)]['team_name']
		reg_time = time.strftime('%Y-%m-%d', time.gmtime(game_info['date']))
		# print('https://www.youtube.com/results?search_query=' + home_name + '+vs+' + away_name + "+" + reg_time)
		# sys.exit()
		player_youtube = requests.get('https://www.youtube.com/results?search_query=' + home_name + "+vs+" + away_name + "+" + reg_time)
		player_youtube_soup = BeautifulSoup(player_youtube.text)
		# print(player_youtube_soup)
		# sys.exit()
		player_youtube_links = player_youtube_soup.find_all('a', class_='yt-uix-sessionlink        spf-link ')
		num_vids = 3
		num_count = 0
		youtube_links_list = []
		for v in player_youtube_links:
			if num_count == num_vids:
				break
			# print("Player Youtube Video " + str(num_count) + ": " + 'https://www.youtube.com' + v['href'])
			# youtube_links_list += ['https://www.youtube.com' + v['href']]
			temp_link = 'https://www.youtube.com' + v['href']
			embed_link = "https://www.youtube.com/embed/" + temp_link[temp_link.index('=') + 1:]
			youtube_links_list += [temp_link]
			num_count += 1

		game_info['youtube_links'] = youtube_links_list
		print(i)
		i += 1


#dump updated nbaGames json into another json file
with open('nbaGames_highlights.json', 'w+') as outfile:
    json.dump(nbaGames, outfile)