"""
Name:Kyaw Soe Naing
Date: 24 Jan 2020
Brief Project Description:
GitHub URL:
"""
# TODO: Create your main program in this file, using the MoviesToWatchApp class
from kivy.app import StringProperty
from kivy.properties import ListProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from movie import Movie
from moviecollection import MovieCollection

SORTING_KEY = {"Category": "category", "Title": "title", "Year": "year", "Watched": "is_watched"}
CATEGORY_LIST = ["Action", "Comedy", "Documentary", "Drama", "Fantasy", "Thriller"]


class MoviesToWatchApp(App):
    """MoviesToWatchApp(App) with Kivy APP following movies """
    current_spinner = StringProperty()
    message = StringProperty()
    watched_status = StringProperty()
    sorting_keys = ListProperty()

    # Construct the main app.
    def __init__(self, **kwargs):
        super(MoviesToWatchApp, self).__init__(**kwargs)
        self.movies = MovieCollection()

    # Create the main app
    def build(self):
        Window.size = (800, 500)
        self.title = "Movies Watch system 3.1 by Kyaw Soe Naing "
        self.root = Builder.load_file('app.kv')
        self.sorting_keys = SORTING_KEY.keys()
        self.current_spinner = self.sorting_keys[0]
        self.movies.load_movies("movies.csv")
        self.show_movie()
        return self.root

    # Show the movie list
    def show_movie(self):
        count = 0
        print(self.current_spinner)
        self.movies.sort(SORTING_KEY[self.current_spinner])
        self.root.ids.movies_box.clear_widgets()
        for movie in self.movies.movies:
            if movie.is_watched:
                color = [0.3, 0.7, 0.9, 0.5]
                mark = "watched"
            else:
                color = [0.8, 0.3, 1.0, 1]
                mark = ""
            movie_text = "{} ({} from {:d}) {}".format(movie.title, movie.category, movie.year, mark)
            movie_button = Button(text=movie_text, id=str(count), background_color=color)
            movie_button.bind(on_release=self.press_movie)
            self.root.ids.movies_box.add_widget(movie_button)
            count += 1
        unwatched_number = self.movies.get_unwatched()
        watched_number = self.movies.get_watched()
        self.watched_status = "To watch: {:d}. Watched: {:d}".format(unwatched_number, watched_number)

    # check watch and unwatch
    def press_movie(self, instance):
        """   """
        movie_id = int(instance.id)
        movie_data = self.movies.movies[movie_id]
        movie_title = movie_data.title

        if movie_data.is_watched:
            movie_data.mark_unwatched()
            self.message = "You need to watch {:s}".format(movie_title)
        else:
            movie_data.mark_watched()
            self.message = "You have watched {:s}".format(movie_title)
        self.movies.sort(SORTING_KEY[self.current_spinner])
        self.show_movie()


MoviesToWatchApp().run()
