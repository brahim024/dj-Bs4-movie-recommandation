import random
import requests
from bs4 import BeautifulSoup

# crawl IMDB Top 250 and randomly select a movie



def main(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    #soup = BeautifulSoup(response.text, 'lxml') # faster

    # print(soup.prettify())

    '''movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.posterColumn span[name=ir]')
    images=soup.select('td.posterColumn img')'''
    movietags = soup.find_all("a",{"class":"movie"})
    inner_movietags = soup.find_all('span',{'class':'title'})
    ratingtags = soup.select('span.r i')
    images=soup.select('a.movie img')

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1] # last item 
        return year

    titles = [tag.text for tag in inner_movietags]
    ratings = [tag.text for tag in ratingtags] # access attribute 'data-value'
    img=[image['src'] for image in images]
    n_movies = len(titles)

    while(True):
        idx = random.randrange(0, n_movies)
        
        return titles[idx], ratings[idx] ,img[idx]


def get_siries(url):
	response=requests.get(url)
	soup=BeautifulSoup(response.text,'html.parser')
	sirietag=soup.find_all()
	inner_serietags=soup.find_all()
	rating_tag=soup.find_all()
	image=soup.select()
	def get_years():
		moviesplit=sirietag.txt.split()
		year=moviesplit[-1]
		return year

	titles=[tag.txt for tag in inner_serietags]
	rating=[tag.txt for tag in rating_tag]
	img=[imag['src'] for imag in image]
	n_serie=len(titles)
	


