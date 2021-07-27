class Movies:
    def __init__(self, movies):
        self.movies = movies

    def display_movies(self):
        print(self.movies)


m1 = Movies(["movie1", "movie2", "movie3"])
m1.display_movies()

m2 = Movies(["movie4", "movie5", "movie6"])
m2.display_movies()

m3 = Movies(["movie7", "movie8", "movie9"])
m3.display_movies()