#!/usr/bin/env python
# David Fuller
#
# 7-28-2016

from Channels import Channels
from Email import Email
import os

# Constants
channels = Channels()
emailer = Email()
MAIN_MENU = "0: View Channel Content\n" + \
            "1: View Channels\n" + \
            "2: Add Channel\n" + \
            "3: Delete Channel\n" + \
            "4: Download a Video\n" + \
            "5: Quit"

# Method clears screen
def cls():
    os.system('clear')

# Method handles viewing content
def viewContent():
    viewChannels()
    choice = int(raw_input("\nChoice: "))
    if (not channels.isValid(choice)):
        return
    channels.viewChannelContent(channels.getChannel(choice), True)

# Method handles viewing channels
def viewChannels():
    cls()
    print ("")
    channels.printChannels()
    print ("")

# Method handles adding channels
def addChannel():
    viewChannels()
    name = raw_input("\nEnter channel name: ")
    if (not name == ""):
        channels.appendChannel(name)
        channels.commitChannels()

# Method handles deleting channels
def deleteChannel():
    viewChannels()
    choice = int(raw_input("Choice: "))
    if (not channels.isValid(choice)):
        return
    channels.deleteChannel(choice)
    channels.commitChannels()

# Method downloads a single video given video id
def downloadVideo():
    channel = raw_input("Enter YouTube username: ")
    videoID = raw_input("Enter video ID: ")
    channels.downloadVideo(channel, videoID)
    message = channel + " " + videoID + " Has finished downloading"
    emailer.email(message)

# Method closes app
def closeApp():
    cls()
    raise SystemExit

# Method decides whether menu choice is valid or not
def menuChoiceIsValid(menu, choice):
    tempChoice = int(choice)
    length = menu.count('\n')
    if (tempChoice < 0 or \
        tempChoice > length):
        return False
    return True

# Get user input from menu
def menuInput(menu):
    print (menu)
    return raw_input("\nChoice? ")

# Handles main menu
def mainMenu():
    cls()
    while True:
        choice = menuInput(MAIN_MENU)
        switch = {
            "0": viewContent,
            "1": viewChannels,
            "2": addChannel,
            "3": deleteChannel,
            "4": downloadVideo,
            "5": closeApp}
        if (menuChoiceIsValid(MAIN_MENU, choice)):
            switch[choice]()

# Main method to drive program
def main():
    channels.readChannels()   # From file
    mainMenu()

# Begin program
main()
