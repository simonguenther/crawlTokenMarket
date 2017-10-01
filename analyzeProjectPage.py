import urllib
import sys
import json
import re
import cfscrape
import codecs
from bs4 import BeautifulSoup

class ProjectPage:
    def __init__(self):
       #print "Analyzing project page"
       pass

    def setContent(self,html):
        content = html
        global soup 
        soup = BeautifulSoup(content, "lxml")

    def getProjectName(self):
        for results in soup.findAll("div", {"id":"asset-logo-wrapper"}):
            item = results.parent.text.strip()
            if item is None:
                return ""
            else:
                return item

    def getSymbol(self):
        for results in soup.find("th",text="Symbol"):
            item = results.findNext("td").text
            if item is None:
                return ""
            else:
                return item

    
    def getCrowdsaleOpeningDate(self):
        if soup.find("th",text="Crowdsale opening date") is None:
            return ""

        for results in soup.find("th",text="Crowdsale opening date"):
            item = results.findNext("td").findNext("p").text.strip()
            if item is None:
               return ""
            else:
                return item

    def getCrowdsaleClosingDate(self):
        if soup.find("th",text="Crowdsale closing date") is None:
            return ""

        for results in soup.find("th",text="Crowdsale closing date"):
            item = results.findNext("td").findNext("p").text.strip()
            if item is None:
                return ""
            else:
                return item

    def getConcept(self):
        if soup.find("th",text="Concept") is None:
            return ""

        for results in soup.find("th",text="Concept"):
            item = results.findNext("td").findNext("p").text.strip().encode("utf-8")
            if item is None:
                return ""
            else:
                return item

    def getYoutubeChannel(self):
        pattern = re.compile(r'[a-zA-Z:/.]*youtube.com\/[a-zA-Z:/.0-9_]*')
        a = len(soup.findAll("a", href=pattern))
        if a==0:
            return ""
            

        for results in soup.findAll("a", href=pattern):
            item = results["href"]
            if item is None:
                return ""
            else:
                return item
        
    
    def getWebsiteURL(self):
        if soup.findAll("i",{"class":"fa fa-globe fa-fw"}) is None:
            return ""

        for results in soup.findAll("i",{"class":"fa fa-globe fa-fw"}):
            item = results.parent["href"]
            if item is None:
                return ""
            else:
                return item
    
    def getBlogURL(self):
        for results in soup.findAll("i",{"class":"fa fa-rss fa-fw"}):
            if "available" in results.parent.text:
                return ""

            item = results.parent["href"]
            if item is None:
                return ""
            else:
                return item
    
    def getWhitepaperURL(self):
        for results in soup.findAll("i",{"class":"fa fa-file-text-o fa-fw"}):
            if "available" in results.parent.text:
                return ""

            item = results.parent["href"]
            if item is None:
                return ""
            else:
                return item

    def getFacebookURL(self):
        for results in soup.findAll("i",{"class":"fa fa-facebook fa-fw"}):
            if "available" in results.parent.text:
                return ""

            item = results.parent["href"]
            if "tokenmarket" in item:
                continue

            if item is None:
                return ""
            else:
                return item.replace("https://www.facebook.com/","").strip("/")

    def getTwitterURL(self):
        for results in soup.findAll("i",{"class":"fa fa-twitter fa-fw"}):
            if "available" in results.parent.text:
                return ""

            item = results.parent["href"]
            if "tokenmarket" in item:
                continue

            if item is None:
                return ""
            else:
                return item.replace("https://twitter.com/","")
    
    def getLinkedInURL(self):
        for results in soup.findAll("i",{"class":"fa fa-linkedin fa-fw"}):
            if "available" in results.parent.text:
                return ""

            item = results.parent["href"]
            if "tokenmarket" in item:
                continue

            if item is None:
                return ""
            else:
                return item
    
    def getSlackInviteURL(self):
        for results in soup.findAll("i",{"class":"fa fa-slack fa-fw"}):
            if "available" in results.parent.text:
                return ""

            item = results.parent["href"]
            if item is None or "discordapp" in item:
                return ""
            else:
                return item
    
    def getDiscordInviteURL(self):
        for results in soup.findAll("i",{"class":"fa fa-slack fa-fw"}):
            if "available" in results.parent.text:
                return ""

            item = results.parent["href"]
            if item is None or "slack" in item:
                return ""
            else:
                return item

    def getTelegramInviteURL(self):
        for results in soup.findAll("i",{"class":"fa fa-mobile fa-fw"}):
            if "available" in results.parent.text:
                return ""

            item = results.parent["href"]
            if item is None:
                return ""
            else:
                return item

    def getGithubURL(self):
        for results in soup.findAll("i",{"class":"fa fa-github fa-fw"}):
            if "available" in results.parent.text:
                return ""

            item = results.parent["href"]
            if item is None:
                return ""
            else:
                return item