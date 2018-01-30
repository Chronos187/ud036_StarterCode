import fresh_tomatoes
import media

air_force_one = media.Movie("Air Force One",
                            "The President of the U.S. must covertly fight back against terrorists that hijack his plane.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BYTk5NWE2ZjAtZmRmOS00ZGYzLWI5ZmUtMDcwODI0YWY0MTRlL2ltYWdlXkEyXkFqcGdeQXVyNjQzNDI3NzY@._V1_.jpg",
                            "https://www.youtube.com/watch?v=jPYnVOIfNiU")

rush_hour = media.Movie("Rush Hour",
                        "A Chinese and American detective must work together to rescue the Chinese Consul's daughter after a kidnapping.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BYWM2NDZmYmYtNzlmZC00M2MyLWJmOGUtMjhiYmQ2OGU1YTE1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,678,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=JMiFsFQcFLE")

firewall = media.Movie("Firewall",
                       "A banker must cooperate when a heist and kidnapping threaten his family",
                       "https://resizing.flixster.com/6jKlpvYh9C61B0zOx3bJRmYIo64=/206x305/v1.bTsxMTE3MTQzNztqOzE3Njc5OzEyMDA7ODAwOzEyMDA",
                       "https://www.youtube.com/watch?v=w96aZhrK28w")

robin_hood = media.Movie("Robin Hood",
                         "An outlaw must work against a corrupt king who hypnotizes the previous king into a crusade.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BYjUwMzhkM2ItMTU2OC00OTQ5LWJlMDUtMzRmYjc0NDUyNGVhL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,670,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=c5Qph47c2uE")

movie_list = [air_force_one, rush_hour, firewall, robin_hood]

fresh_tomatoes.open_movies_page(movie_list)
