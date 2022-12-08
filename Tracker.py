import

def get_NBA_stats():
    year=input("Which NBA season are you interested in?: ")
player=input("For which player do you want to get stats?: ")

BASE_URL = 'https://www.espn.com/nba/'
PLAYER_LIST_URL = 'http://www.espn.com/nba/players'
PLAYERS_ID_URL = 'https://www.espn.com/nba/player/_/id/[ID]/[player]'
PLAYERS_GAMELOG_URL = 'https://www.espn.com/nba/player/gamelog/_/id/[ID]/[player]'

season_list = [
	'1996-97',
	'1997-98',
	'1998-99',
	'1999-00',
	'2000-01',
	'2001-02',
	'2002-03',
	'2003-04',
	'2004-05',
	'2005-06',
	'2006-07',
	'2007-08',
	'2008-09',
	'2009-10',
	'2010-11',
	'2011-12',
	'2012-13',
	'2013-14',
	'2014-15',
	'2015-16',
	'2016-17',
	'2017-18',
	'2018-19',
	'2019-20',
    '2020-21'
]

class NBAPointGuardStats(NBAStats):
    def keys():
        return [ 'id', 'player_id', 'GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%','FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'EFF']      
class NBAShootingGuardStats(NBAStats):
    def keys():
        return [ 'id', 'player_id', 'GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%','FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'EFF']
class NBASmallForwardStats(NBAStats):
    def keys():
        return [ 'id', 'player_id', 'GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%','FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'EFF']
class NBAPowerForwardStats(NBAStats):
    def keys():
        return [ 'id', 'player_id', 'GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%','FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'EFF']
class NBACenter(NBAStats):
    def keys():
        return [ 'id', 'player_id', 'GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%','FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'EFF']
