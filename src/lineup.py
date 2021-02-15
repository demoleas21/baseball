from pprint import pprint
from bs4 import BeautifulSoup
import configs
from selenium import webdriver
from time import sleep


def getSoup(website):
    # TODO: Reorganize and abstract away button clicks
    driver = webdriver.Chrome()
    driver.get(website)
    careerStatsButton = driver.find_element_by_link_text('Career Stats')
    careerStatsButton.click()
    sleep(1)
    batterButton = driver.find_element_by_link_text('Batter')
    if batterButton:  # TODO: this will crash if not found
        batterButton.click()
    gameLogButton = driver.find_element_by_link_text('Game Log')
    gameLogButton.click()
    sleep(1)
    html = driver.page_source
    return BeautifulSoup(html, "html.parser")


def setStats(player, stat, statName):
    playerDict = {}
    for i, _ in enumerate(stat):
        playerDict[configs.STATS_LIST[i]] = float(stat[i])
    if statName[0].isdigit():
        statName = 'game:' + statName
    player.setStats(statName, playerDict)


def getStats(soup, categories):
    stats = {}
    tableRows = soup.find_all('tr')
    for category in categories:
        tds = configs.STAT_CATEGORIES[category]
        for row in tableRows:
            stat = row.text.split('\n')[tds['start']:tds['end']]
            if tds['statText'] in row.text and len(stat) > 10:
                # TODO record meta data for games
                stats[category] = stat
                break
    return stats


def setPlayerStats(player):
    website = configs.NJABL_PLAYER_PAGE.format(pageId=player.pageId)
    soup = getSoup(website)
    stats = getStats(soup, configs.STAT_CATEGORIES.keys())
    for category in configs.STAT_CATEGORIES.keys():
        setStats(player, stats[category], category)
    pprint(player.regularSeasonFall2018)


def main():
    # setPlayerStats(configs.bloss)
    setPlayerStats(configs.dre)
    # setPlayerStats(configs.andrew)
    # for player in configs.PLAYERS:
    #     setPlayerStats(player)

main()
