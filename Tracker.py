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

for row in player_info:
            season_id=season_id, # this is key, need this to join and sort by seasons
            player_id=row[0],
            player_name=row[1],
            team_id=row[2],
            team_abbreviation=row[3],
            age=row[4],
            gp=row[5],
            w=row[6],
            l=row[7],
            w_pct=row[8],
            min=row[9],
            fgm=row[10],
            fga=row[11],
            fg_pct=row[12],
            fg3m=row[13],
            fg3a=row[14],
            fg3_pct=row[15],
            ftm=row[16],
            fta=row[17],
            ft_pct=row[18],
            oreb=row[19],
            dreb=row[20],
            reb=row[21],
            ast=row[22],
            tov=row[23],
            stl=row[24],
            blk=row[25],
            blka=row[26],
            pf=row[27],
            pfd=row[28],
            pts=row[29],
            plus_minus=row[30],
            nba_fantasy_pts=row[31],
            dd2=row[32],
            td3=row[33],
            gp_rank=row[34],
            w_rank=row[35],
            l_rank=row[36],
            w_pct_rank=row[37],
            min_rank=row[38],
            fgm_rank=row[39],
            fga_rank=row[40],
            fg_pct_rank=row[41],
            fg3m_rank=row[42],
            fg3a_rank=row[43],
            fg3_pct_rank=row[44],
            ftm_rank=row[45],
            fta_rank=row[46],
            ft_pct_rank=row[47],
            oreb_rank=row[48],
            dreb_rank=row[49],
            reb_rank=row[50],
            ast_rank=row[51],
            tov_rank=row[52],
            stl_rank=row[53],
            blk_rank=row[54],
            blka_rank=row[55],
            pf_rank=row[56],
            pfd_rank=row[57],
            pts_rank=row[58],
            plus_minus_rank=row[59],
            nba_fantasy_pts_rank=row[60],
            dd2_rank=row[61],
            td3_rank=row[62],
            cfid=row[63],
player.save()

print ("Done inserting player general traditional season total data to the database!")
