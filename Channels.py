# David Fuller
#
# 7-28-2016

from FileHandler import FileHandler
from StringTokenizer import StringTokenizer
from Scraper import Scraper

# Define Channels class
class Channels(object):
    COMMA = ','
    MAX = 10   # Number of videos per channel to display
    
    # Constructor
    def __init__(self):        
        self.fileHandler = FileHandler("channels")
        self.tokenizer = StringTokenizer(self.COMMA)
        self.scraper = Scraper()
        self.channels = []
        self.count = 0
        
    # Method returns video IDs
    def getVideoIDs(self):
        return self.scraper.getVideoIDs()

    # Method returns video titles
    def getVideoTitles(self):
        return self.scraper.getVideoTitles()

    # Method returns number of channels
    def getCount(self):
        return self.count

    # Method returns channel name
    def getChannel(self, index):
        return self.channels[index]

    # Method returns whether channel is valid or not
    def isValid(self, choice):
        tempChoice = int(choice)
        if (tempChoice < 0 or \
            tempChoice >= len(self.channels)):
            return False
        return True

    # Method appends channel to channels
    def appendChannel(self, inputString):
        self.channels.append(inputString)
        self.count = self.count + 1

    # Method creates channels from file
    def readChannels(self):
        channelstring = self.fileHandler.read()
        channelstring = channelstring.rstrip('\n')
        self.tokenizer.setString(channelstring)
        while (not self.tokenizer.atEnd()):
            self.channels.append(self.tokenizer.getToken())
            self.count = self.count + 1

    # Debug method to print all channels
    def printChannels(self):
        i = 0
        for c in self.channels:
            print (str(i) + ":", c)
            i = i + 1

    # Method commits channels to file
    def commitChannels(self):
        self.fileHandler.write(self.channels, self.COMMA, False)

    # Method prints given channel content
    def viewChannelContent(self, channel, doPrint):
        self.scraper.setChannelUrl(channel)
        self.scraper.scrape()
        self.scraper.scrape()   # ran twice for good reason
        if (doPrint):
            self.scraper.printContent(channel, self.MAX)

    # Method deletes a channel
    def deleteChannel(self, index):
        del self.channels[index]
        self.count = self.count - 1

    # Method downloads a single video
    def downloadVideo(self, channel, videoID):
        self.scraper.downloadVideo(channel, videoID)
        
