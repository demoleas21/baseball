from pprint import pprint
from bs4 import BeautifulSoup
import configs
from selenium import webdriver
from time import sleep


def getSoup(website):
    driver = webdriver.Chrome()
    driver.get(website)
    careerStatsButton = driver.find_element_by_link_text('Career Stats')
    careerStatsButton.click()
    sleep(3)
    html = driver.page_source
    return BeautifulSoup(html, "html.parser")


def getPlayerStats(player):
    playerDict = {}
    website = configs.NJABL_PLAYER_PAGE.format(playerId=player.pageId)
    soup = getSoup(website)
    # TODO: use driver to click buttons on website to see other tabs
    regularSeasonFall2018 = soup.find_all('tr')[8].text.split('\n')[3:24]
    regularSeasonSpring2018 = soup.find_all('tr')[9].text.split('\n')[3:24]
    careerTotals = soup.find_all('tr')[10].text.split('\n')[3:24]
    playerDict[player.name] = {}
    for i, _ in enumerate(regularSeasonFall2018):
        playerDict[player.name][configs.STAT_CATEGORIES[i]] = float(regularSeasonFall2018[i])
    player.setStats('regularSeasonFall2018', playerDict[player.name])
    pprint(player.regularSeasonFall2018)


def main():
    getPlayerStats(configs.bloss)
    # getPlayerStats(configs.ANDREW)


main()
