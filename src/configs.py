from models import Player

GP = 'Games Played'
AB = 'At Bats'
R = 'Runs'
H = 'Hits'
B1 = 'Singles'
B2 = 'Doubles'
B3 = 'Triples'
HR = 'Home Runs'
TB = 'Total Bases'
BB = 'Walks'
RBI = 'Runs Batted In'
HBP = 'Hit By Pitch'
K = 'Strikeouts'
SB = 'Stolen Bases'
AVG = 'Average'
OBP = 'On Base Percentage'
SLG = 'Slugging'
OPS = 'On Base Plus Slugging'
SF = 'Sac Flies'
SAC = 'Sacrifices'
PA = 'Plate Appearances'

STATS_LIST = [GP, AB, R, H, B1, B2, B3, HR, TB, BB, RBI, HBP, K, SB, AVG, OBP, SLG, OPS, SF, SAC, PA]

NJABL_PLAYER_PAGE = 'https://www.newjerseyabl.com/roster_players/{pageId}'

STAT_CATEGORIES = ['regularSeasonFall2018', 'regularSeasonSpring2018', 'careerTotals']

TD_STAT_MAP = {
    'regularSeasonFall2018': {'statText': '2018 Fall\nRegular Season', 'start': 3, 'end': 24},
    'regularSeasonSpring2018': {'statText': '2018 Spring\nRegular Season', 'start': 3, 'end': 24},
    'careerTotals': {'statText': 'Career Totals', 'start': 2, 'end': 23},
}

andrew = Player('Andrew Demoleas', '26469546')
bloss = Player('Ryan Godfrey', '26469533')

PLAYERS = [
    andrew,
    bloss,
]

DRE = {

}
BEN = {

}
BROC = {

}
CHRISTIAN = {

}
FRANK = {

}
BRENT = {

}
TYLER = {

}
AIRTIGHT = {

}
MATEUSZ = {

}
LUIGI = {

}
JOHN = {

}
STEVE = {

}
ROB = {

}