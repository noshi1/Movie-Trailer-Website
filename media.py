import webbrowser
class Movie():
    """

    This class is going to store information about movies and define
    functions to show the movies info and movies trailers
    
    """

    #constructor of the class is going to initialize the instance variables
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #This functon will be called to play the trailer of the movie
        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)

        
        
    
