from urllib.request import urlopen, Request
from json import loads
from html import escape, unescape
from re import compile as re_compile

MERCURY_API = 'https://mercury.postlight.com/parser?url='

def _everseen(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

class ParsedPage:
    """ Parsed article object initializer """
    
    def __init__ (self, parser):
        """ Class initialiser """
        for attr in ["content", "date_published", "dek",
                     "direction", "domain", "excerpt",
                     "lead_image_url", "next_page_url",
                     "rendered_pages", "title",
                     "total_pages", "url", "word_count"]:
            setattr(self, attr, None)
        self.parser = parser
    
    def next(self):
        if self.next_page_url:
            return self.parser.parse(self.next_page_url)
    
    def __repr__(self):
        return "<ParsedPage url=\"{}\">".format(self.url)

class MercuryParser:
    """ Mercury Web Parser python3 wrapper """
    
    def __init__ (self, api_key):
        """ Class initialiser """
        self.api_key = api_key
    
    def __unescape(self, text):
        translate = lambda x: chr(int(x[3:-1], base=16))
        regex = re_compile(r"&#x[0-9A-Fa-f]+?;")
        keymap = {i: translate(i) for i in _everseen(regex.findall(text))}
        for key, value in keymap.items():
            text = text.replace(key, value)
        return text
    
    def parse(self, url):
        """ Parse page via Mercury parser """
        open_url = MERCURY_API + url
        parsed_page = ParsedPage(self)
        with urlopen(Request(open_url, headers={"x-api-key": self.api_key})) as doc:
            data = doc.read().decode("utf8", "xmlcharrefreplace")
            response = loads(data)
            for key, value in response.items():
                if key == "content":
                    parsed_page.content = self.__unescape(value)
                elif value:
                    setattr(parsed_page, key, value)
        return parsed_page
