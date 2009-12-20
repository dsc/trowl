import pyres
from trowl.util import pquery 

BASE_HEADERS = {
    'User-Agent'      : 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5',
    'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'en-us,en;q=0.5',
    'Accept-Charset'  : 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'
}


class Scraper(object):
    """ Base scraper, which merely fetches the page and invokes process.
    """
    queue = 'trowl'
    url = None
    opener = None
    request = None
    cookies = None
    response = None
    
    
    def __init__(self, url, **env):
        self.url = url
        self.env = env
        self.fetch()
        self.process()
    
    def fetch(self):
        "Fetches the url (but does not read from the response)."
        
        import urllib2, cookielib
        from urllib2 import build_opener, HTTPCookieProcessor, HTTPRedirectHandler
        
        self.cookies = cookielib.CookieJar()
        self.opener = build_opener( HTTPCookieProcessor(self.cookies), HTTPRedirectHandler )
        self.opener.addheaders = BASE_HEADERS.copy().items()
        
        print "Fetching %s..." % self.url
        self.request = self.opener.open(self.url)
        return self.request
    
    def process(self):
        "Abstract method for processing the response."
        print "Processing %s..." % self.url
    
    @classmethod
    def perform(Cls, url, env={}):
        Cls(url, **env)
    
    def __str__(self):
        return "{self.__class__.__name__}(url={self.url})".format(self=self)
    


class ParsingScraper(Scraper):
    """ Scraper which parses the content with lxml.
    """
    
    def __init__(self, url, **env):
        super(ParsingScraper, self).__init__(url, **env)
    
    def process(self):
        self.dom = pquery.parse(self.request)
        print self.dom
        super(ParsingScraper, self).process()
    

class Spider(ParsingScraper):
    """ A Spider walks the DOM looking for links, 
        and then queues each that passes the filter.
    """
    
    def __init__(self, url, filter=None, **env):
        self.filter = filter
        super(Spider, self).__init__(url, filter=None, **env)
    
    def process(self):
        pass




