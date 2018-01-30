import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A movie about a boy whose toys come alive.",
                        "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://mrmoviefiend.files.wordpress.com/2010/06/avatar-poster-10.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie("School of Rock",
                             "A man pretends to be a substitute teacher and starts a rock band with the class",
                             "https://i.ytimg.com/vi/eAry-ZV_gfs/movieposter.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                             "A rat attempts to become a chef at a fancy French restaurant",
                             "https://images-na.ssl-images-amazon.com/images/I/51MJQKcJVFL._SY450_.jpg",
                             "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                             "An aspiring novelist vacationing in Paris encounters revelers who take him back in time to the Jazz Age and incite dissatisfaction of the present in him.",
                             "http://t3.gstatic.com/images?q=tbn:ANd9GcTk3ssys2bKM5-U6XMgvoD8yVoS5Io2YKg_1xA6x6GA8mKuuqID",
                             "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                             "In a future dystopia a young girl must fight to the death in place of her sister, in a grueling free for all survival challenge.",
                             "https://2982-presscdn-29-70-pagely.netdna-ssl.com/wp-content/uploads/2015/11/The-Hunger-Games-Poster1.jpg",
                             "https://www.youtube.com/watch?v=4S9a5V9ODuY")

## Creating array of movies for input of open_movie_page()
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)
