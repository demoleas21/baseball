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
    website = configs.NJABL_PLAYER_PAGE.format(playerId=player.pageId)
    soup = getSoup(website)
    # TODO: use driver to click buttons on website to see other tabs
    playerStatRows = soup.find_all('tr')
    for i, _ in enumerate(playerStatRows):
        if player.name == playerStatRows[i].text.split('\n')[3]:
            playerStats = playerStatRows[i].text.split('\n')[5:26]
            break
    playerDict[player.name] = {}
    for i, _ in enumerate(playerStats):
        playerDict[player.name][configs.STAT_CATEGORIES[i]] = float(playerStats[i])
    pprint(playerDict)


def main():
    getPlayerStats(configs.bloss)
    # getPlayerStats(configs.ANDREW)


main()
