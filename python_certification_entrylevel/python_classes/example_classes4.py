class Movie:
    def __init__(self, movies):
        self.movies = movies
    def print_movies(self):
        print(self.movies)


movies1 = Movie({'action': 'fast & furions', 'thriller': 'superman', 'romance': 'titanic'})
movies1.print_movies()