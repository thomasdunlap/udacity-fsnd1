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

big_sick = media.Movie("The Big Sick", "Pakistan-born comedian Kumail Nanjiani and grad student Emily Gardner fall in love but struggle as their cultures clash. When Emily contracts a mysterious illness, Kumail finds himself forced to face her feisty parents, his family's expectations, and his true feelings.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BZWM4YzZjOTEtZmU5ZS00ZTRkLWFiNjAtZTEwNzIzMDM5MjdmXkEyXkFqcGdeQXVyNDg2MjUxNjM@._V1_SY1000_SX675_AL_.jpg",
                            "https://www.youtube.com/watch?v=3Z_o-8pkiVo")

v_for_vendetta = media.Movie("V for Vendetta", "In a future British tyranny, a shadowy freedom fighter, known only by the alias of \"V\", plots to overthrow it with the help of a young woman.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BYzllMjJkODAtYjMwMi00YmNhLWFhYzAtZjZjODg5YzEwOGUwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY999_CR0,0,679,999_AL_.jpg",
                            "https://www.youtube.com/watch?v=k_13fFIrhPk")

lobster = media.Movie("The Lobster", "In a dystopian near future, single people, according to the laws of The City, are taken to The Hotel, where they are obliged to find a romantic partner in forty-five days or are transformed into beasts and sent off into The Woods.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BNDQ1NDE5NzQ1NF5BMl5BanBnXkFtZTgwNzA5OTM2NTE@._V1_SY1000_CR0,0,705,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=LTNZmOJxuAc")


# Movie instances to convert to HTML elements
movies = [network, donnie_darko, big_sick, v_for_vendetta, adventureland, lobster]

fresh_tomatoes.open_movies_page(movies)
