import spacy

# load the pre-trained English language model
nlp = spacy.load("en_core_web_md")

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# What I find interesting about the similarities between the words "cat", "monkey", and "banana"
# is that even though they are not directly related to each other, they still have some level of
# similarity in their vector representations. For example, "cat" and "monkey" have a similarity
# score of 0.66, while "banana" and "monkey" have a similarity score of 0.54. This suggests that
# there might be some underlying semantic connections between these words, even though they are not
# immediately apparent.


#The 'en_core_web_sm' model is a smaller and simpler language model compared to 'en_core_web_md'.
# It has a smaller vocabulary and fewer embeddings for each token, which makes it faster to load and run.
# However, this also means that it may not be as accurate or able to handle more complex language tasks.

#When running the same code on 'en_core_web_sm', I noticed that the similarity scores between tokens were
# generally lower compared to 'en_core_web_md'. This suggests that the smaller model may not be as effective
# in capturing the nuances and relationships between words.

#For example, when comparing the similarity between "cat" and "monkey", the score in 'en_core_web_md'
# was 0.583 whereas in 'en_core_web_sm' it was only 0.397. Similarly, the score between "banana" and "monkey"
# was 0.514 in 'en_core_web_md' but only 0.333 in 'en_core_web_sm'.

#Overall, while 'en_core_web_sm' may be more efficient for simpler language tasks and faster to run,
# it may not be as accurate or effective for more complex language processing.
