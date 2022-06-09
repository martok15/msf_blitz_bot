import os
import discord
import pyautogui
import time
from discord import Webhook, RequestsWebhookAdapter
import datetime
import pandas as pd
import constants

pyautogui.FAILSAFE = True
cwd = os.getcwd()
start_time = time.time()
webhook_url = constants.webhook
webhook = Webhook.from_url(webhook_url,
                           adapter=RequestsWebhookAdapter())

# open bluestacks
os.startfile(constants.bluestacks)
time.sleep(2)
pyautogui.screenshot('bluestacks.png')


def close_bluestacks():
    os.system("taskkill /F /IM bluestacks.exe")


# start msf

if pyautogui.locateOnScreen(cwd + r'\screenshots\game_center.png', confidence=.8):
    time.sleep(2)
    my_games = pyautogui.locateCenterOnScreen(cwd + r'\screenshots\my_games.png',
                                              confidence=.8)
    time.sleep(2)
    pyautogui.moveTo(my_games)
    pyautogui.click(my_games)

time.sleep(2)

try:
    start_msf = pyautogui.locateCenterOnScreen(cwd +
                                               r'\screenshots\strikeforce_icon.png',
                                               confidence=.8)
    time.sleep(2)
    pyautogui.moveTo(start_msf)
    pyautogui.click(start_msf)
except:
    print('cant find msf')
    webhook.send('cant find msf')
    close_bluestacks()
    quit()

try:
    webhook.send('strikeforce started')
except:
    print('discord error')

# close pop-up offers
time.sleep(60)
i = 0
while i <= 10:
    if pyautogui.locateOnScreen(cwd + r'\screenshots\ok_raid.png', confidence=.8):
        ok_raid = pyautogui.locateCenterOnScreen(cwd + r'\screenshots\ok_raid.png',
                                                 confidence=.8)
        pyautogui.moveTo(ok_raid)
        pyautogui.click(ok_raid)

    time.sleep(2)

    if pyautogui.locateOnScreen(cwd + r'\screenshots\war_cont.png', confidence=.8):
        war_cont = pyautogui.locateCenterOnScreen(
            cwd + r'\screenshots\war_cont.png',
            confidence=.8)
        pyautogui.moveTo(war_cont)
        pyautogui.click(war_cont)

    time.sleep(2)

    if pyautogui.locateOnScreen(cwd + r'\screenshots\pop_up_x.png', confidence=.8):
        pop_up = pyautogui.locateCenterOnScreen(cwd + r'\screenshots\pop_up_x.png',
                                                confidence=.8)
        pyautogui.moveTo(pop_up)
        pyautogui.click(pop_up)
        pyautogui.moveTo(start_msf)
        time.sleep(2)
    i = i + 1

pyautogui.screenshot(cwd + r'\screenshots\after_popup.png')
try:
    webhook.send('closed pop-ups')
except:
    print('discord error')

# select blitz
pyautogui.move(400, 0, 2)
pyautogui.drag(-900, 0, 2)

if pyautogui.locateOnScreen(cwd + r'\screenshots\blitz.png', grayscale=True,
                            confidence=.8):
    blitz = pyautogui.locateCenterOnScreen(cwd + r'\screenshots\blitz.png',
                                           grayscale=True,
                                           confidence=.8)
    pyautogui.moveTo(blitz)
    pyautogui.click(blitz)
else:
    pyautogui.screenshot(cwd + r'\screenshots\cant_find_blitz.png')
    print("Can't Find Blitz")
    try:
        webhook.send('Cant Find Blitz')
    except:
        print('discord error')
        pyautogui.screenshot('no_blitz.png')
    close_bluestacks()
    quit()

time.sleep(5)

if pyautogui.locateOnScreen(cwd + r'\screenshots\go.png', grayscale=True,
                            confidence=.8):
    go_icon = pyautogui.locateCenterOnScreen(cwd + r'\screenshots\go.png',
                                             grayscale=True,
                                             confidence=.8)
    pyautogui.moveTo(go_icon)
    pyautogui.click(go_icon)
else:
    pyautogui.screenshot(cwd + r'\screenshots\cant_find_go.png')
    print("Can't Find Go")
    try:
        webhook.send('Cant find go')
    except:
        print('discord error')
    close_bluestacks()
    quit()
time.sleep(1)
pyautogui.screenshot(cwd + r'\screenshots\blitz_start.png')

# Send blitz start to discord

disc_start = discord.File(cwd + r'\screenshots\blitz_start.png')
try:
    webhook.send("Blitz Started", file=disc_start)
except:
    print('discord error')


def find_battle():
    if pyautogui.locateOnScreen(cwd + r'\screenshots\no_battle.png',
                                confidence=.8):
        find_opp = pyautogui.locateCenterOnScreen(
            cwd + r'\screenshots\find_opp.png',
            confidence=.8)
        pyautogui.moveTo(find_opp)
        pyautogui.click(find_opp)
        time.sleep(4)

    elif pyautogui.locateCenterOnScreen(cwd + r'\screenshots\cores.png',
                                        confidence=.8):
        next_arrow = pyautogui.locateCenterOnScreen(
            cwd + r'\screenshots\next_arrow.png',
            confidence=.8)
        pyautogui.moveTo(next_arrow)
        pyautogui.click(next_arrow)
        time.sleep(4)
    elif pyautogui.locateCenterOnScreen(cwd + r'\screenshots\battle_cores.png',
                                        confidence=.8):
        next_arrow = pyautogui.locateCenterOnScreen(
            cwd + r'\screenshots\next_arrow.png',
            confidence=.8)
        pyautogui.moveTo(next_arrow)
        pyautogui.click(next_arrow)
        time.sleep(4)
    else:
        print("can't find battle")


def battle():
    if pyautogui.locateOnScreen(cwd + r'\screenshots\battle.png', confidence=.8):
        battle_icon = pyautogui.locateCenterOnScreen(
            cwd + r'\screenshots\battle.png',
            confidence=.8)
        pyautogui.moveTo(battle_icon)
        pyautogui.click(battle_icon)
        time.sleep(5)
    else:
        print("no battle found")


victories = 0
defeats = 0


def record_results():
    if pyautogui.locateOnScreen(cwd + r'\screenshots\victory.png', confidence=.8):
        global victories
        victories = victories + 1
    else:
        global defeats
        defeats = defeats + 1


def continue_next():
    if pyautogui.locateOnScreen(cwd + r'\screenshots\continue.png',
                                confidence=.6):
        cont = pyautogui.locateCenterOnScreen(cwd + r'\screenshots\continue.png',
                                              confidence=.6)
        record_results()
        time.sleep(.5)
        pyautogui.moveTo(cont)
        pyautogui.click(cont)
        time.sleep(3)
        next_team = pyautogui.locateCenterOnScreen(
            cwd + r'\screenshots\next_arrow.png',
            confidence=.8)
        pyautogui.moveTo(next_team)
        pyautogui.click(next_team)

    else:
        print("no continue found")


# navigate to starting team:

while pyautogui.locateOnScreen(cwd + r'\screenshots\start_team.png',
                               confidence=.8) is None:
    next_arrow = pyautogui.locateCenterOnScreen(
        cwd + r'\screenshots\next_arrow.png',
        confidence=.8)
    pyautogui.moveTo(next_arrow)
    pyautogui.click(next_arrow)
    time.sleep(.5)
print('starting team found')

# first battle only:

if pyautogui.locateOnScreen(
        cwd + r'\screenshots\no_battle.png', confidence=.8):
    find_opp = pyautogui.locateCenterOnScreen(cwd + r'\screenshots\find_opp.png',
                                              confidence=.8)
    pyautogui.moveTo(find_opp)
    pyautogui.click(find_opp)
    time.sleep(2)

elif pyautogui.locateCenterOnScreen(cwd + r'\screenshots\cores.png',
                                    confidence=.8):
    next_arrow = pyautogui.locateCenterOnScreen(
        cwd + r'\screenshots\next_arrow.png',
        confidence=.8)
    pyautogui.moveTo(next_arrow)
    pyautogui.click(next_arrow)
    time.sleep(2)
elif pyautogui.locateCenterOnScreen(cwd + r'\screenshots\battle_cores.png',
                                    confidence=.8):
    next_arrow = pyautogui.locateCenterOnScreen(
        cwd + r'\screenshots\next_arrow.png',
        confidence=.8)
    pyautogui.moveTo(next_arrow)
    pyautogui.click(next_arrow)
    time.sleep(2)
else:
    print("first team can't battle")
time.sleep(2)
battle()
time.sleep(2)
continue_next()
time.sleep(2)

# loop through all teams until you reach starting team

while pyautogui.locateOnScreen(cwd + r'\screenshots\start_team.png',
                               confidence=.6) is None:
    time.sleep(1)
    find_battle()
    time.sleep(1)
    battle()
    time.sleep(1)
    continue_next()
    print('Victories: ' + str(victories))
    print('Defeats: ' + str(defeats))
    time.sleep(1)

pyautogui.screenshot(cwd + r'\screenshots\blitz_comp.png')
end_time = time.time()
elapsed_time = str(end_time - start_time)
total_battles = victories + defeats
if total_battles == 0:
    win_percent = 0
else:
    win_percent = "{:.2%}".format(victories / total_battles)
print("Blitz completed")
print("elapsed time: " + str(elapsed_time) + 's')

# Send Discord message and picture
disc_end = discord.File(cwd + r'\screenshots\blitz_comp.png')
try:
    webhook.send('Elapsed Time: ' + str(elapsed_time))
    webhook.send('Blitz Complete', file=disc_end)
    webhook.send('Total Battles: ' + str(total_battles))
    webhook.send('Win Percent: ' + str(win_percent))
except:
    print('discord error')
# close bluestacks
close_bluestacks()

print('Victories: ' + str(victories))
print('Defeats: ' + str(defeats))
print('Win percent: ' + str(win_percent))

# Create battle log data set
today_date = datetime.date.today()
df = pd.DataFrame([[today_date, end_time, elapsed_time, victories, defeats, total_battles, win_percent]],
                  columns=['Date', 'Time', 'Elapsed Time', 'Victories', 'Defeats', 'Total_Battles', 'Win_%'])
print(df)
time.sleep(3)
# create or append to csv
if os.path.isfile(cwd + r'\battle_log.csv'):
    df.to_csv(cwd + r'\battle_log.csv', mode='a', index=False, header=False)
else:
    df.to_csv(cwd + r'\battle_log.csv', index=False)

time.sleep(10)

quit()
