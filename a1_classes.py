"""..."""
# TODO: Copy your first assignment to this file, then update it to use Movie class
# Optionally, you may also use MovieCollection class

from movie import Movie
from moviecollection import MovieCollection

print("Movies To Watch 1.0 - by Kyaw Soe Naing")
MENU = """Menu:
L - List movies
A - Add new movies
W - Watch a movie
Q - Quit
"""
# Read all data from movies.csv file
DATAFILE = "movies.csv"
moviecollection = MovieCollection()
moviecollection.load_movies(DATAFILE)
# all data from csv file is stored in movies = [] as nested list
movies = []


# Main Function including other many functions
def main():
    user_input = menu()
    while user_input != "q":
        if user_input == "l":
            all_movies()
            user_input = menu()
        elif user_input == "a":
            add_movies()
            user_input = menu()
        elif user_input == "w":
            watch_list()
            user_input = menu()
        else:
            print("Invalid menu choice")
            user_input = menu()
    # Write all changes data to csv file
    moviecollection.save_movies(DATAFILE)

    print("{} movies saved to {}".format(len(moviecollection.movies), DATAFILE))
    print("Have a nice day :)")


# ask for the user to input and print menu
def menu():
    print(MENU)
    user_input = input(">>>").lower()
    return user_input


# Show all movies from list of movies.csv file
def all_movies():
    count = 0
    for movie in moviecollection.movies:
        if movie.is_watched == False:
            print("{}. *  {:<35} - {:>4} ({}).".format(count + 1, movie.title, movie.category, movie.year))
        else:
            print("{}.    {:<35} - {:>4} ({}).".format(count + 1, movie.title, movie.category, movie.year))
        count += 1
    # Show how many video left to watch
    still_to_watch = moviecollection.get_unwatched()
    watch_movies = moviecollection.get_watched()
    if still_to_watch > 0:
        print(" {} movies watched, {} movies still to watch.".format(watch_movies, still_to_watch))
    else:
        print(" {} movies watched, No more movies to watch!".format(watch_movies))
    print("")


# Add new movies to list of movies.csv file
# Check user input for blank and invalid input
def add_movies():
    new_name = input("Title :")
    while not new_name:  # Check user input for blank
        print("Input can not be blank")
        new_name = input("Title :")
    # Check user input for blank, valid number and input 0
    valid = False
    while not valid:
        try:
            new_year = int(input("Year: "))
            while new_year <= 0:
                print("Number must be more than 0.")
                new_year = int(input("Year: "))
                valid = True
            valid = True
        except ValueError:
            print("Invalid input, please enter a valid number.")

    new_category = input("Category :")
    category_filter = ["Action", "Comedy", "Documentary", "Drama", "Fanstay", "Thriller"]
    while not new_category:  # Check user input for blank
        print("Input can not be blank")
        new_category = input("Category :")

    # store user input of new data as nested list
    moviecollection.add_movie(Movie(new_name, new_year, new_category, False))
    moviecollection.sort("category")
    print("{:s} ({:s} from {:d}) added to movie ".format(new_name, new_category, new_year))
    print("")


# select user watched movies to list of movies.csv file
# exception handling for user input
def watch_list():
    try:
        valid = False
        while not valid:
            still_to_watch = moviecollection.get_unwatched()
            if still_to_watch > 0:
                select = int(input("Enter the number of a movie to mark as watched :"))
                while select <= 0:
                    print("Nulmber must be greater than zero")
                    select = int(input("Enter the number of a movie to mark as watched :"))
                if select <= len(moviecollection.movies):
                    select -= 1
                    movie = [movie for movie in moviecollection.movies]
                    if movie[select].is_watched == False:
                        movie[select].mark_watched()
                        print("{:s} from {:s} watched!".format(movie[select].title, movie[select].category))
                        valid = True
                    else:
                        print("You have already watched {}".format(movie[select].title))
                        valid = True
                else:
                    print("Invalid movies number")
            else:
                print("No More movies to watch! Please add more.")
                valid = True
    # excepting for Invalid string input
    except ValueError:
        print("Invalid input; enter a valid number!")
        watch_list()


main()
