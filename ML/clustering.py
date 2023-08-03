import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from itertools import combinations
from sklearn.cluster import AgglomerativeClustering
import json

def preprocess_text(text):
    # Preprocess text by removing special characters and lowercasing
    return text.lower() #.replace(".", "").replace(",", "").replace("limited", "").replace("ltd", "").strip()

def find_related_pairs(company_names, threshold=0.35):
    # Preprocess company names
    preprocessed_names = [preprocess_text(name) for name in company_names]

    # Use TF-IDF to convert text data into numerical vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(preprocessed_names)

    # Compute cosine similarity matrix
    similarity_matrix = cosine_similarity(tfidf_matrix)


    # Apply hierarchical clustering
    clusters = AgglomerativeClustering(n_clusters=None, distance_threshold=1 - threshold, linkage='average', affinity='precomputed')
    clusters.fit_predict(1 - similarity_matrix)

    # Generate related pairs
    related_pairs = set()
    for cluster_id in np.unique(clusters.labels_):
        cluster_indices = np.where(clusters.labels_ == cluster_id)[0]
        if len(cluster_indices) >= 2:
            for pair in combinations(cluster_indices, 2):
                pair_names = tuple(sorted([company_names[pair[0]], company_names[pair[1]]]))
                related_pairs.add(pair_names)
    print(related_pairs)
    return related_pairs

def main():
    # Load the JSON file containing the list of names
    with open("../org_names.json", "r") as file:
        data = json.load(file)
    
    # Call the function with the sample data
    related_pairs = find_related_pairs(data, threshold=0.8)
    for pair in related_pairs:
        print(pair)




if __name__ == "__main__":
    main()




