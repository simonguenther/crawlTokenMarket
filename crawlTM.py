import urllib
import sys
import json
import cfscrape
import codecs
import db_sql
from bs4 import BeautifulSoup
from analyzeProjectPage import ProjectPage

baseURL = "https://tokenmarket.net/ico-calendar/upcoming"

def get_html(url):
    try:
        scraper = cfscrape.create_scraper()
        return scraper.get(url).content
    except:
        print("Error", sys.exc_info()[0])
        raise

def get_Links_From_Upcoming_List(content):
    soup = BeautifulSoup(content, "lxml")
    coming = []
    for results in soup.findAll("td", {"class":"col-asset-name"}):
         coming.append(results.a["href"])
    return coming

def saveJSONtoFile(path, jsonDump):
	with codecs.open(path,'w','utf-8') as f:
		f.write(json.dumps(jsonDump, indent=3))

def process_Upcoming_List(coming):
        i = 0
        upReady = {}
        conn = db_sql.open_connection()
        for x in coming:
            single = {}
            i += 1
            #print "Analyzing: " + x
            overview = get_html(x)
            page = ProjectPage()
            page.setContent(overview)

            print "ID:\t\t"+ str(i)
            print "Name:\t\t"+ page.getProjectName()
            print "Symbol:\t\t"+ page.getSymbol()
            print "Crowdsale start:" + page.getCrowdsaleOpeningDate()
            print "Crowdsale end:\t" + page.getCrowdsaleClosingDate()
            print "Concept:\t" + page.getConcept()
            print "YouTube:\t"+ page.getYoutubeChannel()
            print "Website:\t"+ page.getWebsiteURL()
            print "Blog:\t\t"+ page.getBlogURL()
            print "Whitepaper:\t"+ page.getWhitepaperURL()
            print "Facebook:\t"+ page.getFacebookURL()
            print "Twitter:\t"+ page.getTwitterURL()
            print "LinkedIn:\t" + page.getLinkedInURL()
            print "Slack:\t\t" + page.getSlackInviteURL()
            print "Telegram:\t" + page.getTelegramInviteURL()
            print "Github:\t\t" + page.getGithubURL()
            print "\n\n\n"
            
            single["Name"] = page.getProjectName()
            single["Symbol"] = page.getSymbol()
            single["Sale_Start"] = page.getCrowdsaleOpeningDate()
            single["Sale_End"] = page.getCrowdsaleClosingDate()
            single["Concept"] = page.getConcept()
            single["YouTube"] = page.getYoutubeChannel()
            single["Website"] = page.getWebsiteURL()
            single["Blog"] = page.getBlogURL()
            single["Whitepaper"] = page.getWhitepaperURL()
            single["Facebook"] = page.getFacebookURL()
            single["Twitter"] = page.getTwitterURL()
            single["LinkedIn"] = page.getLinkedInURL()
            single["Slack"] = page.getSlackInviteURL()
            single["Discord"] = page.getDiscordInviteURL()
            single["Telegram"] = page.getTelegramInviteURL()
            single["Github"] = page.getGithubURL()
            db_sql.insert_in_main(conn, single)
            upReady[single["Symbol"]] = single
        saveJSONtoFile("upcoming_ICOs.json", upReady)
        conn.close()

html = get_html(baseURL)
upcoming = get_Links_From_Upcoming_List(html)
process_Upcoming_List(upcoming)

