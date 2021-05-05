class movie:
    def __init__(self, movies):
        self.movies = movies
    def print_movie(self):
        print(self.movies)

movies1 = movie(['sci-fi', 'fantasy', 'autobiography'])
movies1.print_movie()

movies2 = movie(['mass', 'class', 'romantic'])
movies2.print_movie()

movies3 = movie(['novel-based', 'reality', 'horror'])
movies3.print_movie()



