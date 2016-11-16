import fresh_tomatoes
import media

# Define all movies using media class
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "http://www.youtube.com/watch?v=-9ceBgWV8io"
                     )

last_samurai = media.Movie("The Last Samurai",
                          "Nathan Algren is an American hired to instruct the "
                          "Japanese army in the ways of modern warfare -- in "
                          "this lush epic set in the 1870s, which finds Algren"
                          " learning to respect the samurai and the honorable "
                          "principles that rule them. Pressed to destroy the "
                          "samurai's way of life in the name of modernization "
                          "and open trade, Algren decides to become an "
                          "ultimate warrior himself and to fight for their "
                          "right to exist.",
                          "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Last_Samurai.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=T50_qHEOahQ"
                          )

major_payne = media.Movie("Major Payne",
                          "Major Benson Winifred Payne is being discharged "
                          "from the Marines. Payne is a killin' machine, but "
                          "the wars of the world are no longer fought on the "
                          "battlefield. A career Marine, he has no idea what "
                          "to do as a civilian, so his commander finds him a "
                          "job - commanding officer of a local school's JROTC "
                          "program, a bunch of ragtag losers with no hope.",
                          "https://upload.wikimedia.org/wikipedia/en/8/85/Major_Payne.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=6Vvlw7uPdn8"
                          )

saving_ryan = media.Movie("Saving Private Ryan",
                         "As U.S. troops storm the beaches of Normandy, three "
                         "brothers lie dead on the battlefield, with a fourth "
                         "trapped behind enemy lines. Ranger captain John "
                         "Miller and seven men are tasked with penetrating "
                         "German-held territory and bringing the boy home.",
                         "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=vwAxi4A2YcY"
                         )

van_wilder = media.Movie("National Lampoon's Van Wilder",
                         "Van Wilder is an outgoing, and extremely popular "
                         "student who has been at Coolidge College for seven "
                         "years. For the past three years he has made no "
                         "effort to graduate, instead spending his time "
                         "organizing parties, helping other students, and "
                         "posing for figure drawing classes. But after seven "
                         "years, with no return on his investment, Van's "
                         "father decides it is time to stop paying Van's "
                         "tuition.",
                         "https://upload.wikimedia.org/wikipedia/en/e/e1/National_Lampoon%27s_Van_Wilder_Poster.png",  # NOQA
                         "https://www.youtube.com/watch?v=qShNioFXXwM"
                         )

# Set all defined movies into movies array
movies = [avatar, last_samurai, major_payne, saving_ryan, van_wilder]

# use fresh_tomatoes class to launch webpage
fresh_tomatoes.open_movies_page(movies)
