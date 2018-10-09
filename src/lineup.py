import urllib2
from pprint import pprint
from bs4 import BeautifulSoup
import configs


def soupie():
    playerDict = {}
    njabl = 'https://www.newjerseyabl.com/stats/team_instance/3824651?subseason=536707&tab=team_instance_player_stats&tool=3261383'
    statsPage = urllib2.urlopen(njabl)
    soup = BeautifulSoup(statsPage, 'lxml')
    tbody = soup.tbody
    bloss = tbody.td.next.next.next.text.split('\n')[1]
    playerStats = [float(text.text) for text in tbody.tr.find_all('td')[2:]]
    playerDict[bloss] = zip(configs.STAT_CATEGORIES, playerStats)
    pprint(playerDict)


def main():
    soupie()

main()
