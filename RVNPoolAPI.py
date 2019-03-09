#-----------Welcome to DeAdSeC Python RVN API----------#
#-------Made By DeAdSeC-------#
#---Version 1.0.0---#

import urllib.request as lib
import json
import time as t
import os
import sys

#You can change all options bellow
api_key = '' #Not Available Wont Do Nothing
api_website = '' #Put here your API link
time = 5 #Time to wait between info update
MinHashRate = 50 #Minium hashrate value for console alert
TraceBack = 1 # 0 For OFF | 1 For ON

#Dont change anything bellow here
W = "\033[0m" # white (normal)
R = "\033[31m" # red
G = "\033[32m" # green
O = "\033[33m" # orange
B = "\033[34m" # blue
P = "\033[35m" # purple
C = "\033[36m" # cyan
GR = "\033[37m" # gray
D = "\033[2m" # dims current color. {W} resets.
Plus = f'{W}{D}[{W}{G}+{W}{D}]{W}'
Danger = f'{O}[{R}!{O}]{W}'
WTF = f'{W}[{C}?{W}]'
BHashRate = 0
sys.tracebacklimit = TraceBack #Removes/Enables traceback

def OS():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    while True:
        OS()
        #Loads needed varables and json from API
        jsonOBJ = lib.urlopen(api_website)
        data = json.load(jsonOBJ)
        UserStats = data['getuserstatus']
        Data = UserStats['data']
        Shares = Data['shares']

        username = Data['username']
        VShares = Shares['valid']
        NShares = Shares['invalid']
        Hashrate = Data['hashrate']

        if Hashrate > BHashRate: #Comprares the hashrate to the Highest hasrate
            BHashRate = Hashrate #Updates the Highest hashrate

        if Hashrate <= MinHashRate:
            print(f'{Plus}{W} New data recived {Plus}')
            print(f'{W}    ----------------{W}')
            print(f'{Plus}{W} Owner UserName: {O}{username}{W}')
            print(f'{Plus}{W} Valid Shares: {O}{VShares}{W}')
            print(f'{Plus}{W} Invalid Shares: {O}{NShares}{W}')
            print(f'{Plus}{W} Highest Hashrate: {O}{BHashRate} MH/s{W}')
            print(f'{Plus}{W} Hashrate: {O}{Hashrate} MH/s{W}')
            print(f'{Danger}{R} HASHRATE BELLOW {MinHashRate}{W}')
        else:
            print(f'{Plus}{W} New data recived {Plus}')
            print(f'{W}    ----------------{W}')
            print(f'{Plus}{W} Owner UserName: {O}{username}{W}')
            print(f'{Plus}{W} Valid Shares: {O}{VShares}{W}')
            print(f'{Plus}{W} Invalid Shares: {O}{NShares}{W}')
            print(f'{Plus}{W} Highest Hashrate: {O}{BHashRate} MH/s{W}')
            print(f'{Plus}{W} Hashrate: {O}{Hashrate} MH/s{W}')

        t.sleep(time)

except KeyboardInterrupt:
    print(f'\n{Danger}{R} Script interrupted by Keyboard!{Danger}{W}')
