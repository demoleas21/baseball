from bs4 import BeautifulSoup
import urllib2
import lxml

GP = 'Games Played'
AB = 'At Bats'
R = 'Runs'
STAT_CATEGORIES = [GP, AB, R, H, B1, B2, B3, HR, TB, BB, RBI, HBP, K, AVG, OBP, SLG, OPS, SF, SAC, PA]

def soupie():
    njabl = 'https://www.newjerseyabl.com/stats/team_instance/3824651?subseason=536707&tab=team_instance_player_stats&tool=3261383'
    statsPage = urllib2.urlopen(njabl)
    soup = BeautifulSoup(statsPage, 'lxml')
    tbody = soup.tbody
    bloss = tbody.td.next.next.next.text.split('\n')[1]
    print tbody
    print bloss


def main():
    soupie()

main()
