import urllib2
from pprint import pprint
from bs4 import BeautifulSoup
import configs


def tempGetPlayerStats(player):
    playerDict = {}
    statsPage = urllib2.urlopen(configs.NJABL_FALL_2018)
    soup = BeautifulSoup(statsPage, 'lxml')
    playerStatRows = soup.tbody.find_all('tr')
    for i, _ in enumerate(playerStatRows):
        if player == playerStatRows[i].text.split('\n')[3]:
            playerStats = playerStatRows[i].text.split('\n')[5:26]
            break
    playerDict[player] = {}
    for i, _ in enumerate(playerStats):
        playerDict[player][configs.STAT_CATEGORIES[i]] = float(playerStats[i])
    pprint(playerDict)


def getPlayerStats(player):
    playerDict = {}
    statsPage = urllib2.urlopen(configs.NJABL_FALL_2018)
    soup = BeautifulSoup(statsPage, 'lxml')
    playerStatRows = soup.tbody.find_all('tr')
    for i, _ in enumerate(playerStatRows):
        if player == playerStatRows[i].text.split('\n')[3]:
            playerStats = playerStatRows[i].text.split('\n')[5:26]
            break
    playerDict[player] = {}
    for i, _ in enumerate(playerStats):
        playerDict[player][configs.STAT_CATEGORIES[i]] = float(playerStats[i])
    pprint(playerDict)


def main():
    tempGetPlayerStats(configs.BLOSS)
    tempGetPlayerStats(configs.ANDREW)


main()
