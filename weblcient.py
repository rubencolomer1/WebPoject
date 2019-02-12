#from urllib.request import urlopen
from urllib2 import urlopen

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

        def run(self):
            # download a web page
            page = self.download_page()
            # search activities in web page
            # print the activities
            print(page)



if __name__ == "__main__":
    c = WebClient()
    c.run()