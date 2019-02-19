from urllib.request import urlopen
import bs4

class AliExpress(object):
        """aliexpress Class"""
        def __init__(self):
            super(AliExpress, self).__init__()

        def download_page(arg):
            # connect to the web page
            f = urlopen("https://www.banggood.com/es/Flashdeals.html")
            # get the download_page
            page = f.read()
            # close the connection
            f.close()
            return page

        def flash_offers(self, page):
            tree = bs4.BeautifulSoup(page, "lxml")
            ul = tree.find("ul", "goodlist_1")
            li = ul.find_all("li")
            title_list = []
            for item in li:
                price = item.find("span", "price").text
                title = item.find("span", "title").text
                title_list.append((title, price))
            return title_list

        def run(self):
            # download a web page
            page = self.download_page()
            # search activities in web page
            data = self.flash_offers(page)
            # print the activities
            print(data)



if __name__ == "__main__":
    c = AliExpress()
    c.run()
