# Project Created By: Finnegan McGuire
# Status: COMPLETED (Possible Additions in the future)
# Date Started: 11/16/2019 (1:20 AM, EST)

# Imports
import json
import requests

summonerName = input('Summoner Name: ')
APIKey = input('API KEY: ')
print('COMMANDS: ')
print('getaccount | listmasterys | checkmatchinfo | getfreechamps')

addressAccInfo = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={APIKey}'
addressChampRot = f'https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={APIKey}'

# Parses JSON into a manipulatable information from the JSON link
def parse(link):
    jsonlink = requests.get(link)
    parseinfo = jsonlink.json()
    return parseinfo

# Changes the id of a champ to the champ name (NOT USED)
# This is correctly implamented on lines 56 - 64
def changnumtochamp(id, num):
    if id == ChampionList['data'][num]['key']:
        id.replace(id, ChampionList['data'][num]['id'])
    return id

# Getting Json Info from League Of Legends API web address
AccInfo = parse(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}?api_key={APIKey}')
encryptedId = AccInfo['id']

# Parsing all the JSON info into usable data
ChampionList = parse(f'http://ddragon.leagueoflegends.com/cdn/9.22.1/data/en_US/champion.json')
ChampRot = parse(f'https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={APIKey}')
ChampMastery = parse(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedId}?api_key={APIKey}')
ChampionListMasterys = parse(f'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedId}?api_key={APIKey}')
Gamemodes = parse(f'http://static.developer.riotgames.com/docs/lol/gameModes.json')

appRunning = True
FREE_CHAMPION_IDS = ChampRot['freeChampionIds']

# COMMANDS / While Loop to keep shit runnin
while appRunning:

    userInput = input('> ').lower()

    if userInput == 'getaccount':
        print('-----------------')
        for items in AccInfo:
            print(items.title() + ': ' + str(AccInfo[items]))

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

    if userInput == 'checkmatchinfo':
        matchID = input('Match ID: ')
        addressMatch = f'https://na1.api.riotgames.com/lol/match/v4/matches/{matchID}?api_key={APIKey}'
        MatchInfo = parse(addressMatch)

        print('------------------------')
        print('Season: ' + str(MatchInfo['seasonId']))
        print('Map: ' + str(MatchInfo['mapId']).replace('11', 'Summoners Rift'))
        print(MatchInfo['teams']['teamId'])
    if userInput == 'getfreechamps':
        print(ChampRot['freeChampionIds'])
    if userInput == '':
        break

