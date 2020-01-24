"""
Name:Kyaw Soe Naing
Date: 24 Jan 2020
Brief Project Description:
GitHub URL: https://github.com/Ezra2952/assignment-02-Ezra2952
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

    # sort key for sorting
    def choose_key(self, key):
        self.current_spinner = key
        self.show_movie()

    # add new movie to movies
    def add_movie(self):
        m_title = self.root.ids.input_title.text
        m_year = self.root.ids.input_year.text
        m_category = self.root.ids.input_cate.text

        m_title = m_title.strip()
        m_year = m_year.strip()
        m_category = m_category.strip().upper()

        if (m_title == "") or (m_year == "") or (m_category == ""):
            self.message = "All fields must be completed"
            return

        if not m_year.isdigit():
            self.message = "Please enter a valid number"
            return

        m_year = int(m_year)
        if m_year < 0:
            self.message = "Year must be more than 0"
        found = False
        count = 0
        for i in range(len(CATEGORY_LIST)):
            if m_category == CATEGORY_LIST[i].upper():
                found = True
                count = i
                break
        if not found:
            self.message = "The category must be one of Action, Comedy, Documentary, Drama, Fantasy, Thriller"
            return
        else:
            m_category = CATEGORY_LIST[count]

        new_movie = Movie(m_title, m_year, m_category)
        self.movies.add_movie(new_movie)
        self.all_clear()
        self.show_movie()

    # clear all the fill box
    def all_clear(self):
        self.root.ids.input_title.text = ""
        self.root.ids.input_cate.text = ""
        self.root.ids.input_year.text = ""
        self.message = ""

    def stop_now(self):
        self.movies.save_movies("movies.csv")


MoviesToWatchApp().run()
