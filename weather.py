from urllib.request import urlopen
import bs4
import xmltodict
import pprint
import json

class WebClient(object):
    """WebClient class"""
    def __init__(self):
        super(WebClient, self).__init__()

    def download_page(self):
        # connect to the web site
        f = urlopen("https://api.openweathermap.org/data/2.5/weather?q=LLeida,es&appid=7de50c11e01dc42f66131cb4c8c0dc10&mode=json&unit=metric")
        # get the download_page
        page = f.read()
        # close the connection
        f.close()
        return page

    def search_activities(self, page):
        dicc = json.loads(page)
        pprint.pprint(dicc)
        temp = dicc['main']['temp']
        weather = dicc['weather'][0]['description']
        return str(temp)+" and "+weather

    #def search_activities(self, page):
    #    xml = xmltodict.parse(page)
    #    pprint.pprint(xml)
        #temp = xml ['current']['temperature']['@value']
        #weather = xml ['current']['weather']['@value']

    def run(self):
        # download a web page
        page = self.download_page()
        # search activities in web page
        data = self.search_activities(page)
        # print the activities
        print(data)

if __name__ == "__main__":
    c = WebClient()
    c.run()
