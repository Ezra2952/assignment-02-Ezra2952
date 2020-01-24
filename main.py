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



MoviesToWatchApp().run()
