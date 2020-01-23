"""..."""

from operator import attrgetter
from movie import Movie


class MovieCollection:
    """..."""

    def __init__(self, movies=None):
        if movies is None:
            movies = []
        self.movies = movies

    def __str__(self):
        """ """
        movie_list = ""
        counter = 0
        for movie in self.movies:
            movie_list += str(counter) + "    " + str(movie) + "\n"
            counter += 1
        return movie_list

    def __len__(self):
        return len(self.movies)

    def load_movies(self, filename):
        """  """
        open_file = open(filename, "r")
        datas = open_file.readlines()
        for line in datas:
            line = line.strip()
            attribute = line.split(",")
            attribute[1] = int(attribute[1])
            if attribute[3] != "w":
                attribute[3] = False
            else:
                attribute[3] = True

            movie = Movie(attribute[0], attribute[1], attribute[2], attribute[3])
            self.movies.append(movie)

    def add_movie(self, movie):
        self.movies.append(movie)

    def sort(self, sort_key):
        """ """
        self.movies.sort(key=attrgetter("{:s}".format(sort_key), "title"))

    def get_watched(self):
        """ """
        count_watched = 0
        for movie in self.movies:
            status = movie.is_watched
            if status:
                count_watched += 1
        return count_watched

    def get_unwatched(self):
        """ """
        count_unwatched = 0
        for movie in self.movies:
            status = movie.is_watched
            if not status:
                count_unwatched += 1
        return count_unwatched

    def save_movies(self, database):
        file = open(database, "w")
        for movie in self.movies:
            title = movie.title
            year = str(movie.year)
            category = movie.category
            if movie.is_watched:
                status = "w"
            else:
                status = "u"
            data_line = title + "," + year + "," + category + "," + status
            data_line = data_line + "\n"
            file.write(data_line)
        file.close()
        print("{:d} movies saved to {}".format(len(self.movies), database))
