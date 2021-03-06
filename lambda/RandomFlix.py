from bs4 import BeautifulSoup
import datetime
import requests

from random import seed
from random import randint

class RandomFlix:
    def __init__(self):
        now = datetime.datetime.now()
        self.base_url = "https://fr.flixable.com"
        self.url = ""
        self.min_year = 1920
        self.max_year = now.year
        self.min_rating = 1
        self.array_cat = ['action', 'anime', 'comédie', 'documentaire', 'drame', 'français', 'horreur', 'indépendant', 'international', 'jeunesse', 'comédies musicales', 'policier', 'primés', 'romance', 'science-fiction et fantastique', 'stand up', 'thriller']
        self.array_id = [1365, 3063, 6548, 2243108, 5763, 58807, 8711, 7077, 78367, 783, 52852, 5824, 89844, 8883, 1492, 11559, 8933 ]
        self.genre = -1

    def print_url(self):
        print(self.url)

    def get_url(self):
        return self.url

    def url_generator(self):
        url = self.base_url
        print(self.genre)
        if self.genre != -1:
            url += "/genre/" + str(self.genre) + "/"
        url += "?min-rating=" + str(self.min_rating)
        url += "&min_year" + str(self.min_year)
        url += "&max-year" + str(self.max_year)
        url += "&order=title"
        self.url = url

    def set_categories(self, search):
        found = False
        for c in self.array_cat:
            if c == search:
                found = True
                self.genre = self.array_id[self.array_cat.index(c)]
        if not found:
            self.genre = -1

    def get_categories(self):
        return self.array_cat

    def process(self, categorie):
        self.set_categories(categorie)
        self.url_generator()
        self.print_url()

        req = requests.get(self.get_url())
        soup = BeautifulSoup(req.content, 'html.parser')
        movie_containers = soup.find_all('div', class_='card-body')
        movies = []
        first = True
        seed()
        value = randint(1, len(movie_containers) - 2)
        # for movie in movie_containers:
        #     print
        #     if not first:
        m = Movie()
        m.parse_movie(movie_containers[value])
        m.set_description(self.base_url)
        m.set_image(self.base_url)
        movies.append(m)
        # else:
        #     first = False
        print(str(value) +  '/' +  str(len(movie_containers)))
        for movie in movies:
            return movie

class Movie:
    def __init__(self):
        self.title = ""
        self.link = ""
        self.description = ""
        self.image = ""

    def parse_movie(self, html):
        self.title = html.h5.text
        self.link = html.a['href']
        self.image = html.img['src']

    def set_description(self, url):
        req = requests.get(url + self.link)
        soup = BeautifulSoup(req.content, 'html.parser')
        movie_containers = soup.find_all('div', class_='card card-plain information')
        self.description = movie_containers[0].p.text
        
    def set_image(self, url):
        req = requests.get(url + self.link)
        soup = BeautifulSoup(req.content, 'html.parser')
        movie_containers = soup.find_all('div', class_='card card-plain information')
        self.image = movie_containers[0].img['data-src']


    def to_string(self):
        return self.title + ". " + self.description

