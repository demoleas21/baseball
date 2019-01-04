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
    sleep(1)
    html = driver.page_source
    return BeautifulSoup(html, "html.parser")


def setStats(player, stat, statName):
    playerDict = {}
    for i, _ in enumerate(stat):
        playerDict[configs.STATS_LIST[i]] = float(stat[i])
    player.setStats(statName, playerDict)


def getStats(soup, categories):
    stats = {}
    for category in categories:
        tds = configs.TD_STAT_MAP[category]
        tableRows = soup.find_all('tr')
        for row in tableRows:
            if tds['statText'] in row.text:
                stat = row.text.split('\n')[tds['start']:tds['end']]
                stats[category] = stat
                break
    return stats


def setPlayerStats(player):
    website = configs.NJABL_PLAYER_PAGE.format(pageId=player.pageId)
    soup = getSoup(website)
    stats = getStats(soup, configs.STAT_CATEGORIES)
    for category in configs.STAT_CATEGORIES:
        setStats(player, stats[category], category)
    pprint(player.regularSeasonFall2018)


def main():
    # setPlayerStats(configs.bloss)
    # setPlayerStats(configs.andrew)
    for player in configs.PLAYERS:
        setPlayerStats(player)

main()
