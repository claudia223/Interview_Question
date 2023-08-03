import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

"""

This approach wasn't tested. For name to vector, we are using a file glove.6B.100d.txt (could have also used Word2Vec), however I wasn't able to download
the file because of my internet connection :(

However, I do have other examples of vectorization in ML section.

"""

class Cosine_sim_alg:
    def __init__(self, embeddings_file, threshold=0.7):
        self.word_embeddings = self.load_word_embeddings(embeddings_file)
        self.threshold = threshold

    def load_word_embeddings(self, embeddings_file):
        word_embeddings = {}
        with open(embeddings_file, "r", encoding="utf-8") as f:
            for line in f:
                values = line.strip().split()
                word = values[0]
                embedding = np.array(values[1:], dtype=np.float32)
                word_embeddings[word] = embedding
        return word_embeddings

    def name_to_vector(self, name):
        words = name.lower().split()
        name_vector = np.mean([self.word_embeddings.get(word, np.zeros(100)) for word in words], axis=0)
        return name_vector

    def is_similar_name(self, name1, name2):
        vector1 = self.name_to_vector(name1)
        vector2 = self.name_to_vector(name2)
        distance = cosine_similarity([vector1], [vector2])[0][0]
        return distance <= self.threshold