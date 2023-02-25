# This is example of Python program.
# It uses Python natural language processing library spaCy


import spacy

def get_similar_movie(description):
    nlp = spacy.load("en_core_web_md")

    with open("movies.txt", "r") as f:
        movie_data = f.readlines()

    max_score = 0
    similar_movie = ""

    for movie in movie_data:
        movie_title, movie_description = movie.split(":")
        movie_description = movie_description.strip()

        score = nlp(description).similarity(nlp(movie_description))
        

        if score > max_score:
            max_score = score
            similar_movie = movie_title.strip()

    return similar_movie



description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
similar_movie = get_similar_movie(description)
print(similar_movie)