#! /usr/bin/env python
# David Fuller
#
# 8-6-2016

from Channels import Channels
from Email import Email
from datetime import datetime as dt
from threading import Timer
import os

# Constant
PATH = "/path/to/videos"
AMOUNT = 3   # Amount of videos to check in each channel

# Global variables
channels = Channels()
emailer = Email()

# Method handles the delay
def delayer():
    today = dt.today()
    nextTime = today.replace(day = today.day + 1, \
                             hour = 2, \
                             minute = 0, \
                             second = 0, \
                             microsecond = 0)
    deltaTime = nextTime - today
    seconds = deltaTime.seconds
    Timer(seconds, autoDownloader).start()

# Method finds and downloads appropriate videos to download
def autoDownloader():
    channels.readChannels()  # From file
    users = []
    videos = []
    newVideos = []
    videoIDs = []
    videoTitles =[]  

    # Populate ID and title lists - from YouTube
    for c in xrange(channels.getCount()):
        user = channels.getChannel(c)
        users.append(user)
        channels.viewChannelContent(user, False)
        counter = 1
        for element in channels.getVideoIDs():
            videoIDs.append(element)
            if counter >= AMOUNT:
                break
            counter = counter + 1

        counter = 1
        for element in channels.getVideoTitles():
            videoTitles.append(element)
            if counter >= AMOUNT:
                break
            counter = counter + 1

    for i in xrange(len(videoIDs)):
        videos.append(videoTitles[i] + "-" + videoIDs[i] + ".mp4")

    # Populate array of new videos I don't have    
    for index in xrange(len(videos)):
        if (index % AMOUNT == 0):
            usr = users[index / AMOUNT]
            chanFiles = []
        path = PATH + usr
        for root, dirs, files in os.walk(path):
            for f in files:
                chanFiles.append(f)
        if videos[index] not in chanFiles:
            newVideos.append([usr, videoIDs[index]])
    
    # Download videos, if there are any new
    if len(newVideos) <= 0:
        print "No new videos to downloads"
    else:
        for vid in newVideos:
            channels.downloadVideo(vid[0], vid[1])
            message = vid[0] + " " + vid[1] + " Has finished downloading"
            emailer.email(message)
    delayer()

# Main method to drive program
def main():
    autoDownloader()

# Begin program
main()
