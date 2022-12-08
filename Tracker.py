import

def get_NBA_stats():
    year=input("Which NBA season are you interested in?: ")
player=input("For which player do you want to get stats?: ")

BASE_URL = 'https://www.espn.com/nba/'
PLAYER_LIST_URL = 'http://www.espn.com/nba/players'
PLAYERS_ID_URL = 'https://www.espn.com/nba/player/_/id/[ID]/[player]'
PLAYERS_GAMELOG_URL = 'https://www.espn.com/nba/player/gamelog/_/id/[ID]/[player]'

class

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
