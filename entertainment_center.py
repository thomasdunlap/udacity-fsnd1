import fresh_tomatoes
import media

# Movie class instances
donnie_darko = media.Movie("Donnie Darko", "A troubled teenager is plagued by visions of a man in a large rabbit suit who manipulates him to commit a series of crimes, after he narrowly escapes a bizarre accident.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BZjZlZDlkYTktMmU1My00ZDBiLWFlNjEtYTBhNjVhOTM4ZjJjXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
                            "https://www.youtube.com/watch?v=ZZyBaFYFySk")

# Movie instances to convert to HTML elements
movies = [donnie_darko]

fresh_tomatoes.open_movies_page(movies)
