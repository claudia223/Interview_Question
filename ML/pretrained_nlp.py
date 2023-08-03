import torch
from transformers import DistilBertTokenizer, DistilBertModel
from itertools import combinations
import json

# Time complexity: O(n^2 * D), where D is the vector dimension

def vectorize_sentences(sentences):
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    model = DistilBertModel.from_pretrained('distilbert-base-uncased')
    
    # Move the model to the GPU if available
    if torch.cuda.is_available():
        model.to('cuda')

    vectors = []
    for sentence in sentences:
        tokens = tokenizer(sentence.lower(), return_tensors='pt', padding=True, truncation=True)
        
        # Move the input tensors to the GPU if available
        if torch.cuda.is_available():
            tokens = tokens.to('cuda')

        with torch.no_grad():
            output = model(**tokens)
        
        # Move the output tensors to the CPU for further processing if needed
        if torch.cuda.is_available():
            output = {key: value.cpu() for key, value in output.items()}
        
        sentence_vector = torch.mean(output['last_hidden_state'], dim=1)
        vectors.append(sentence_vector)
    print("finished vectorising")
    return vectors

def is_related(name1_vector, name2_vector, similarity_threshold):
    similarity = torch.cosine_similarity(name1_vector, name2_vector).item()
    print(similarity)
    return similarity >= similarity_threshold

def find_related_pairs(names_list, similarity_threshold=0.85):
    vectors = vectorize_sentences(names_list)
    related_pairs = set()

    for i, j in combinations(range(len(names_list)), 2):
        print((names_list[i], names_list[j]))
        if is_related(vectors[i], vectors[j], similarity_threshold):
            related_pairs.add(tuple(sorted((names_list[i], names_list[j]))))
            # print((names_list[i], names_list[j]))
    return related_pairs

def main():
    with open("../org_names.json", "r") as file:
        data = json.load(file)
    
    related_pairs = find_related_pairs(data)

    print(related_pairs)


if __name__ == "__main__":
    main()
