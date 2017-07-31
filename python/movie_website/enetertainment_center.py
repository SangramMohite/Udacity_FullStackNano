import movie
import fresh_tomatoes


# create instance of movie Toy Story
toystory = movie.Movie("Toy Story",
                       "A cowboy doll is profoundly threatened and jealous " +
                       "when a new spaceman figure supplants him as top toy" +
                       " in a boy's room.",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/" +
                       "Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# create instance of movie Avatar
avatar = movie.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on" +
                     " a unique mission becomes torn between following his " +
                     "orders and protecting the world he feels is his home.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/" +
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# create instance of movie My Neighbor Totoro
my_neighbor_totoro = movie.Movie("My Neighbor Totoro",
                                 "When two girls move to the country to be " +
                                 "near their ailing mother, they have " +
                                 "adventures with the wondrous forest " +
                                 "spirits who live nearby.",
                                 "https://upload.wikimedia.org/wikipedia/en" +
                                 "/0/02/My_Neighbor_Totoro_-_Tonari_" +
                                 "no_Totoro_%28Movie_Poster%29.jpg",
                                 "https://www.youtube.com/watch?v=TuLX50_5UAI")

# create instance of movie Spirited Away
spirited_away = movie.Movie("Spirited Away",
                            "During her family's move to the suburbs, a " +
                            "sullen 10-year-old girl wanders into a world " +
                            "ruled by gods, witches, and spirits, and where " +
                            "humans are changed into beasts.",
                            "https://upload.wikimedia.org/wikipedia/en/3" +
                            "/30/Spirited_Away_poster.JPG",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

# create instance of movie Howl's Moving Castle
howls_moving_castle = movie.Movie("Howl's Moving Castle",
                                  "When an unconfident young woman is " +
                                  "cursed with an old body by a spiteful " +
                                  "witch, her only chance of breaking the " +
                                  "spell lies with a self-indulgent yet " +
                                  "insecure young wizard and his " +
                                  "companions in his legged, walking castle.",
                                  "https://upload.wikimedia.org/wikipedia/en" +
                                  "/a/a0/Howls-moving-castleposter.jpg",
                                  "https://www.youtube.com/watch?" +
                                  "v=iwROgK94zcM")

# create instance of movie Princess Mononoke
princess_mononoke = movie.Movie("Princess Mononoke",
                                "On a journey to find the cure for a " +
                                "Tatarigami's curse, Ashitaka finds himself " +
                                "in the middle of a war between the forest " +
                                "gods and Tatara, a mining colony. In this " +
                                "quest he also meets San, the Mononoke Hime.",
                                "https://upload.wikimedia.org/wikipedia/en" +
                                "/2/24/Princess_Mononoke_Japanese_Poster_" +
                                "%28Movie%29.jpg",
                                "https://www.youtube.com/watch?v=4OiMOHRDs14")

# add all the movie instances to an array.
movies = [spirited_away,
          toystory,
          princess_mononoke,
          avatar,
          my_neighbor_totoro,
          howls_moving_castle]

# Call the method ope_movies from fresh_tomatoes.py to generate a html page
# containing all the movies instances created above.
fresh_tomatoes.open_movies_page(movies)
