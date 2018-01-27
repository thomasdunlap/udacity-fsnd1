import fresh_tomatoes
import media

# Movie class instances
donnie_darko = media.Movie("Donnie Darko", "A troubled teenager is plagued by visions of a man in a large rabbit suit who manipulates him to commit a series of crimes, after he narrowly escapes a bizarre accident.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BZjZlZDlkYTktMmU1My00ZDBiLWFlNjEtYTBhNjVhOTM4ZjJjXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
                            "https://www.youtube.com/watch?v=ZZyBaFYFySk")

adventureland = media.Movie("Adventureland", "In the summer of 1987, a college graduate takes a 'nowhere' job at his local amusement park, only to find it's the perfect course to get him prepared for the real world.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI1NTYyMjA2N15BMl5BanBnXkFtZTcwNjU1OTA0Mg@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=gfPE_MEKipM")

network = media.Movie("Network", "A television network cynically exploits a deranged former anchor's ravings and revelations about the news media for its own profit.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BYTc3NjcyYmYtMTI4OC00OGViLTkwYzQtZWU2MGMwMTI5ZTU4XkEyXkFqcGdeQXVyNTc1NTQxODI@._V1_.jpg",
                            "https://www.youtube.com/watch?v=qnGgsJ26dao")

# Movie instances to convert to HTML elements
movies = [network, donnie_darko, adventureland]

fresh_tomatoes.open_movies_page(movies)
