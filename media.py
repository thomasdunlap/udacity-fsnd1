import webbrowser

# a class that show basic info for a movie
class Movie():
	def __init__(self, movie_title, movie_storyline,
				poster, trailer_youtube):
		self.title = movie_title
		self.stroy_line = movie_storyline
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer)
