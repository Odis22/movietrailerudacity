import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that can talk",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
# This file stores the movie information. (Title, Image URL, Youtube URL)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_departed = media.Movie("The Departed",
               "A rat and a mole",
               "https://en.wikipedia.org/wiki/File:Departed234.jpg",
               "https://www.youtube.com/watch?v=iQpb1LoeVUc")

school_of_rock = media.Movie("School of rock",
               "a teacher starting a rock band",
               "https://en.wikipedia.org/wiki/File:School_of_Rock_Poster.jpg",
               "https://www.youtube.com/watch?v=3PsUJFEBC74")
love_and_basketball = media.Movie("love_and_basketball",
                      "a boy and girl fall in love and play basketball",
                      "https://en.wikipedia.org/wiki/File:LBmoviePoster.jpg",
                      "https://www.youtube.com/watch?v=Ur83i6_BjbE")
                                    
movies = [toy_story,avatar,school_of_rock,love_and_basketball]
#these are the movies that my website will be showing.
# Calling open_movies_page definition from fresh_tomatoes library.
# This definition will create a static webpage for the list of movies 
fresh_tomatoes.open_movies_page


