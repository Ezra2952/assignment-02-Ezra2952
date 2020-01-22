"""..."""


# TODO: Create your Movie class in this file


class Movie:
    """..."""

    def __init__(self, title="", year=0, category="", is_watched=False):
        """Initialise a Movie instance."""
        self.title = title
        self.category = category
        self.year = year
        self.is_watched = is_watched

    def __str__(self):
        """Return string"""
        if self.is_watched:
            status = "watched"
        else:
            status = ""
        text_str = "{} ({} from {}) {}".format(self.title, self.category, int(self.year), status)
        return text_str

    def mark_watched(self):
        """Mark to watched"""
        self.is_watched = True
        return self.is_watched

    def mark_unwatched(self):
        """Mark to unwatched"""
        self.is_watched = False
        return self.is_watched

