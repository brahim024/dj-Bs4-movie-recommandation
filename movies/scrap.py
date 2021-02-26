import random
import requests
from bs4 import BeautifulSoup

# crawl IMDB Top 250 and randomly select a movie



def main(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    #soup = BeautifulSoup(response.text, 'lxml') # faster

    # print(soup.prettify())

    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.posterColumn span[name=ir]')
    images=soup.select('td.posterColumn img')

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1] # last item 
        return year

    years = [get_year(tag) for tag in movietags]
    actors_list =[tag['title'] for tag in inner_movietags] # access attribute 'title'
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in ratingtags] # access attribute 'data-value'
    img=[image['src'] for image in images]
    n_movies = len(titles)

    while(True):
        idx = random.randrange(0, n_movies)
        
        return titles[idx],years[idx] , ratings[idx] , actors_list[idx],img[idx]


        
    

