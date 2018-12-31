import urllib2
from pprint import pprint
from bs4 import BeautifulSoup
import configs
from selenium import webdriver


def getSoup(website):
    driver = webdriver.Chrome()
    driver.get(website)
    html = driver.page_source
    return BeautifulSoup(html, "html.parser")


def getPlayerStats(player):
    playerDict = {}
    website = configs.NJABL_PLAYER_PAGE.format(playerId=player[configs.PLAYER_ID])
    soup = getSoup(website)
    playerStatRows = soup.tbody.find_all('tr')
    for i, _ in enumerate(playerStatRows):
        if player[configs.NAME] == playerStatRows[i].text.split('\n')[3]:
            playerStats = playerStatRows[i].text.split('\n')[5:26]
            break
    playerDict[player[configs.NAME]] = {}
    for i, _ in enumerate(playerStats):
        playerDict[player[configs.NAME]][configs.STAT_CATEGORIES[i]] = float(playerStats[i])
    pprint(playerDict)


def main():
    getPlayerStats(configs.BLOSS)
    # getPlayerStats(configs.ANDREW)


main()
