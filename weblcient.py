from urllib.request import urlopen
import bs4

class WebClient(object):
        """WebClient Class"""
        def __init__(self):
            super(WebClient, self).__init__()

        def download_page(arg):
            # connect to the web page
            f = urlopen("http://www.eps.udl.cat/ca/")
            # get the download_page
            page = f.read()
            # close the connection
            f.close()
            return page

        def search_activities(self, page):
            tree = bs4.BeautifulSoup(page, "lxml")
            activities = tree.find_all("div", "featured-links-item")
            act_list = []
            for activity in activities:
                title = activity.find("span", "flink-title")
                link = activity.find("a")
                act_list.append((title.text, link["href"]))
            return act_list

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
