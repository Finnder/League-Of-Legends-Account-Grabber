# Project Created By: Finnegan McGuire
# Status: In Progress
# Date Started: 11/16/2019 (1:20 AM, EST)

# Imports
import json
import requests
import termcolor
from termcolor import colored

summonerName = input('Summoner Name: ')
APIKey = input('API KEY: ')
print('COMMANDS: ')
print('getaccount | listmasterys | checkmatchinfo | getfreechamps')

# API LINKS
addressAccInfo = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={APIKey}'
addressChampRot = f'https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={APIKey}'


# Parses JSON into a manipulible information from the JSON link
def parse(link):
    jsonlink = requests.get(link)
    parseinfo = jsonlink.json()
    return parseinfo

# Getting Json Info from League Of Legends API web address
AccInfo = parse(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={APIKey}')
encryptedId = AccInfo['id']

# Parsing all the JSON info into usable data
ChampionList = parse(f'http://ddragon.leagueoflegends.com/cdn/9.22.1/data/en_US/champion.json')
ChampRot = parse(f'https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={APIKey}')
ChampMastery = parse(
    f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedId}?api_key={APIKey}')
ChampionListMasterys = parse(
    f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedId}?api_key={APIKey}')
Gamemodes = parse(f'http://static.developer.riotgames.com/docs/lol/gameModes.json')

appRunning = True
FREE_CHAMPION_IDS = ChampRot['freeChampionIds']

# COMMANDS / While Loop to keep shit runnin
while appRunning:
    userInput = input('> ').lower()

    if userInput == 'getaccount':
        print('-----------------')
        for items in AccInfo:
            print(items.title() + ': ' + colored(str(AccInfo[items]), 'red', attrs=['blink', 'bold']))

    # Lists Masteries and changes champion id's to champion names for a more readible experience for user.
    if userInput == 'listmasterys':
        for items in ChampionListMasterys:
            print('------------------')

            # Convert Champion Id's into Champ Name
            for x in items:
                if x.lower() == 'championid':
                    for y in ChampionList['data']:
                        if items[x] == int(ChampionList['data'][y]['key']):
                            items[x] = ChampionList['data'][y]['name']

                print(x.title() + ': ' + str(items[x]))

    # Idetifies specific match (Match Id Needed) & Displays Info
    if userInput == 'checkmatchinfo':
        matchID = input('Match ID: ')
        addressMatch = f'https://na1.api.riotgames.com/lol/match/v4/matches/{matchID}?api_key={APIKey}'
        MatchInfo = parse(addressMatch)

        print('------------------------')
        print('Season: ' + str(MatchInfo['seasonId']))
        print('Map: ' + str(MatchInfo['mapId']).replace('11', 'Summoners Rift'))
        print(MatchInfo['teams']['teamId'])

    # Displays Free Champion Data (Shows Id's and not names of champs so can be changed for easier readable info for user)
    if userInput == 'getfreechamps':
        print(ChampRot['freeChampionIds'])
    if userInput == '':
        break
