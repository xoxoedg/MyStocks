from bs4 import BeautifulSoup


class QuartalszahlenParser:

    def __init__(self, file):
        self.soup = BeautifulSoup(file, 'html.parser')

    def find_quartalszahlen(self):
        all_quartalszahlen = self.soup.find_all(lambda tag: tag.name == "td" and "Quartalszahlen" in tag.text)
        return [list(map(lambda tag:tag.text, quartalszahlen.find_next_siblings())) for quartalszahlen in all_quartalszahlen]

with open("index.html") as fp:
    parser = QuartalszahlenParser(fp)

b = parser.find_quartalszahlen()
print(b)
