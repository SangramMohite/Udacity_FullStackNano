import webbrowser


class Movie():
    """This class provides a way to store the movie related data"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # constructor for creating an instance of the movie obkect.
    def __init__(self, movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # function to open a browser to show the trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
