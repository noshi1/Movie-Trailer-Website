import fresh_tomatoes
import media

"""
Here in this file we are going to create multiple instances
of Movie class and make a list of these instances to pass to
open_movie_page function of fresh_tomatoes module

"""
frozen = media.Movie("Frozen",
                     "When their kingdom becomes trapped in perpetual winter, fearless Anna "+
                     "(Kristen Bell) joins forces with mountaineer Kristoff (Jonathan Groff) "+
                     "and his reindeer sidekick to find Anna's sister, Snow Queen Elsa",
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

pursuit_of_happiness = media.Movie("Pursuit of Happiness",
                           "Life is a struggle for single father Chris Gardner (Will Smith)",
                           "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                           "https://www.youtube.com/watch?v=89Kq8SDyvfg")

fate_furios = media.Movie("Fate and Furious",
                          "The Fate of the Furious (alternatively known as Fast & Furious 8"+
                          "and Fast 8, and often stylized as F8) is a 2017 American action "+
                          "film directed by F. Gary Gray and written by Chris Morgan.",
                          "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",
                          "https://www.youtube.com/watch?v=Skpu5HaVkOc")

guardian2 = media.Movie("Guardians of the Galaxy 2",
                       "Guardians of the Galaxy Vol. 2 is a 2017 American superhero "+
                       "film based on the Marvel Comics superhero team Guardians of "+
                       "the Galaxy, produced by Marvel Studios and distributed by Walt "+
                       "Disney Studios Motion Pictures.",
                       "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
                       "https://www.youtube.com/watch?v=B16Bo47KS2g")

star_trek = media.Movie("Star Trek Beyond",
                        "Star Trek Beyond is a 2016 American science fiction adventure film"+
                        "directed by Justin Lin from a screenplay by Simon Pegg and Doug Jung "+
                        "and based on the series Star Trek created by Gene Roddenberry",
                        "https://upload.wikimedia.org/wikipedia/en/b/ba/Star_Trek_Beyond_poster.jpg",
                        "https://www.youtube.com/watch?v=dCyv5xKIqlw")

spider_man = media.Movie("Spider Man Homecoming",
                         "Homecoming is a 2017 American superhero film based on the"+
                         "Marvel Comics character Spider-Man.",
                         "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                         "https://www.youtube.com/watch?v=DiTECkLZ8HM")

# We are making a list of our Movie class instances 
movies = [frozen, pursuit_of_happiness, fate_furios, guardian2,
          star_trek, spider_man]

# This function takes the list of instances as argument
fresh_tomatoes.open_movies_page(movies)


