from pprint import pprint
from bs4 import BeautifulSoup
import configs
from selenium import webdriver
from time import sleep


def getSoup(website):
    driver = webdriver.Chrome()
    driver.get(website)
    # TODO: use driver to click buttons on website to see other tabs
    careerStatsButton = driver.find_element_by_link_text('Career Stats')
    careerStatsButton.click()
    sleep(2)
    html = driver.page_source
    return BeautifulSoup(html, "html.parser")


def setStats(player, stat, statName):
    playerDict = {}
    playerDict[player.name] = {}
    for i, _ in enumerate(stat):
        playerDict[player.name][configs.STAT_CATEGORIES[i]] = float(stat[i])
    player.setStats(statName, playerDict[player.name])


def getPlayerStats(player):
    website = configs.NJABL_PLAYER_PAGE.format(playerId=player.pageId)
    soup = getSoup(website)
    setStats(player, soup.find_all('tr')[8].text.split('\n')[3:24], 'regularSeasonFall2018')
    setStats(player, soup.find_all('tr')[9].text.split('\n')[3:24], 'regularSeasonSpring2018')
    setStats(player, soup.find_all('tr')[10].text.split('\n')[2:23], 'careerTotals')
    pprint(player.regularSeasonFall2018)


def main():
    # getPlayerStats(configs.bloss)
    getPlayerStats(configs.andrew)


main()
