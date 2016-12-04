import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
#This is what the movie variables consist of. The title, poster, and the youtube trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
#this is how the function that will iniate the the trailer of the movie. 