import webbrowser
import fresh_tomato

class Video():
	def __init__(self,title,duration):
		self.title = title
		self.duration = duration


class Movie(Video):
	"""this class provides a way to store movie info"""
	valid_ratings = ['G','PG','PT-13','R']
	def __init__(self,title,duration,storyline,posterimg,ytb):
		Video.__init__(self,title,duration)
		self.title = title
		self.storyline = storyline
		self.poster_image_url = posterimg
		self.trailer_youtube_url = ytb


	def show_trailer(self):
		webbrowser.open(self.ytb_trailer_url)

class TVshow(Video):
	def __init__(self, )

toy_story = Movie("toy_story","toys play together","https://www.google.com/imgres?imgurl=http://www.1zoom.me/big2/17/200429-YANA.jpg&imgrefurl=http://www.1zoom.me/zh/wallpaper/200429/z232.1/&h=1200&w=1600&tbnid=oHB1AUe1GqqJbM:&q=toy+story&tbnh=150&tbnw=200&usg=AI4_-kR8m08skTBcPJaRrmGd0Uf-IpSOiw&vet=12ahUKEwizmb_ggYTgAhUR97wKHed6DwAQ_B0wE3oECAUQBg..i&docid=_98JQBx_u3FQkM&itg=1&sa=X&ved=2ahUKEwizmb_ggYTgAhUR97wKHed6DwAQ_B0wE3oECAUQBg","https://www.youtube.com/watch?v=vwyZH85NQC4")
# print(toy_story.storyline)
# toy_story.show_trailer()
toy_story2 = Movie("toy_story2","toys play together2","https://www.google.com/imgres?imgurl=http://www.1zoom.me/big2/17/200429-YANA.jpg&imgrefurl=http://www.1zoom.me/zh/wallpaper/200429/z232.1/&h=1200&w=1600&tbnid=oHB1AUe1GqqJbM:&q=toy+story&tbnh=150&tbnw=200&usg=AI4_-kR8m08skTBcPJaRrmGd0Uf-IpSOiw&vet=12ahUKEwizmb_ggYTgAhUR97wKHed6DwAQ_B0wE3oECAUQBg..i&docid=_98JQBx_u3FQkM&itg=1&sa=X&ved=2ahUKEwizmb_ggYTgAhUR97wKHed6DwAQ_B0wE3oECAUQBg","https://www.youtube.com/watch?v=vwyZH85NQC4")
toy_story3 = Movie("toy_story3","toys play together3","https://www.google.com/imgres?imgurl=http://www.1zoom.me/big2/17/200429-YANA.jpg&imgrefurl=http://www.1zoom.me/zh/wallpaper/200429/z232.1/&h=1200&w=1600&tbnid=oHB1AUe1GqqJbM:&q=toy+story&tbnh=150&tbnw=200&usg=AI4_-kR8m08skTBcPJaRrmGd0Uf-IpSOiw&vet=12ahUKEwizmb_ggYTgAhUR97wKHed6DwAQ_B0wE3oECAUQBg..i&docid=_98JQBx_u3FQkM&itg=1&sa=X&ved=2ahUKEwizmb_ggYTgAhUR97wKHed6DwAQ_B0wE3oECAUQBg","https://www.youtube.com/watch?v=vwyZH85NQC4")
toy_story4 = Movie("toy_story4","toys play together4","https://www.google.com/imgres?imgurl=http://www.1zoom.me/big2/17/200429-YANA.jpg&imgrefurl=http://www.1zoom.me/zh/wallpaper/200429/z232.1/&h=1200&w=1600&tbnid=oHB1AUe1GqqJbM:&q=toy+story&tbnh=150&tbnw=200&usg=AI4_-kR8m08skTBcPJaRrmGd0Uf-IpSOiw&vet=12ahUKEwizmb_ggYTgAhUR97wKHed6DwAQ_B0wE3oECAUQBg..i&docid=_98JQBx_u3FQkM&itg=1&sa=X&ved=2ahUKEwizmb_ggYTgAhUR97wKHed6DwAQ_B0wE3oECAUQBg","https://www.youtube.com/watch?v=vwyZH85NQC4")


movies = [toy_story,toy_story2,toy_story3,toy_story4]
# fresh_tomato.open_movies_page(movies)
# print(Movie.valid_ratings)
print(Movie.__doc__)