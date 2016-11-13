# David Fuller
#
# 8-1-2016

from __future__ import unicode_literals
import urllib.request
import lxml.html
import requests
import os
import subprocess
import youtube_dl

# Define Scraper class
class Scraper(object):
    # Scrape number is number of links to scrape from page
    SCRAPE_NUMBER = 60   # To ensure there are at least 10 video links
    PATH = "/path/to/download/videos/to/"
    
    # Constructor
    def __init__(self):
        self.url = ""
        self.modifier = 0
        self.videoID = []
        self.videoTitle = []

    # Method returns video IDs
    def getVideoIDs(self):
        return self.videoID

    # Method returns video titles
    def getVideoTitles(self):
        return self.videoTitle

    # Method sets channel url given YouTube username
    def setChannelUrl(self, channel):
        self.url= "https://www.youtube.com/user/" + channel + "/videos"

    # Method performs division and rounds up
    def roundUp(self, num, denom):
        return int(num / denom) + (num % denom > 0)

    # Method determines element to start storing IDs and titles at
    def startAt(self, idCount, titleCount):
        halfIDCount = int(.5 * idCount)
        start = self.roundUp(halfIDCount, 2) + titleCount - halfIDCount - idCount
        if (start % 2 == 0 and idCount % 2 == 0 and \
            halfIDCount % 2 != 0 and titleCount % 2 == 0):
            start = start + 1
        elif (start % 2 == 0 and idCount % 2 != 0 and \
              halfIDCount % 2 != 0 and titleCount % 2 == 0):
            start = start - 3
        elif (start % 2 == 0 and idCount % 2 != 0 and \
              halfIDCount % 2 == 0 and titleCount % 2 != 0):
            start = start
        elif (start % 2 != 0 and idCount % 2 == 0 and \
              halfIDCount % 2 != 0 and titleCount % 2 == 0):
            start = start + 6
        elif (start % 2 != 0 and idCount % 2 == 0 and \
              halfIDCount % 2 == 0 and titleCount % 2 != 0):
            if (start == 1):
                start = start + 17
            else:
                start = start - 1
        elif (start % 2 != 0 and idCount % 2 != 0 and \
              halfIDCount % 2 == 0 and titleCount % 2 == 0):
            start = start
        return start

    # Method scrapes content from YouTube channel
    def scrape(self):
        channel = urllib.request.urlopen(self.url)
        tree = lxml.html.fromstring(channel.read())
        vidID = []
        vidTitle = []
        self.videoID[:] = []
        self.videoTitle[:] = []
        counter = 1

        # Acquire IDs
        for ID in tree.xpath('//a/@href'):
            if ('/watch?v=' in ID):
                vidID.append(str(ID)[9:])
            if counter >= self.SCRAPE_NUMBER:
                break
            counter = counter + 1

        # Acquire titles
        counter = 1
        for title in tree.xpath('//a/@title'):
            vidTitle.append(title)
            if counter >= self.SCRAPE_NUMBER:
                break
            counter = counter + 1
        
        # videoTitle starting index modifier
        self.modifier = self.startAt(len(vidID), len(vidTitle))

        # Append video IDs
        for ID in vidID:
            if ID not in self.videoID:
                self.videoID.append(ID)

        # Append video Titles
        for index in range(len(self.videoID)):
            if vidTitle[index + self.modifier] not in self.videoTitle:
                self.videoTitle.append(vidTitle[index + self.modifier])

    # Method prints content dictionary
    def printContent(self, channel, amount):
        os.system('clear')
        print (channel)
        print ("")
        counter = 1
        for i in range(0, len(self.videoID)):
            print (self.videoID[i], " - ", self.videoTitle[i][:80])
            if counter >= amount:
                break
            counter = counter + 1
        print ("")
        
    # Method downloads video
    def downloadVideo(self, channel, videoID):
        # Download to directory
        path = self.PATH + channel
        if (not os.path.exists(path)):
            os.makedirs(path)
        os.chdir(path)

        # Youtube URL
        url = "https://www.youtube.com/watch?v=" + videoID
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as YouTubeDownloader:
            YouTubeDownloader.download([url])
