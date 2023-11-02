import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

directory_path = r'C:\Users\Usuario\Documents\YT-WHISPER_SUMMARIZATION\transcribed-audio'#Cambia el path a donde tengas la carpeta con los CSV guardados

text_folder = os.path.join(directory_path, 'podcasts_text')
if not os.path.exists(text_folder):
    os.makedirs(text_folder)

files = os.listdir(directory_path)

podcasts = []
file_names = []

for file in files:
    if file.endswith(".csv"):
        file_path = os.path.join(directory_path, file)
        output_file = os.path.join(text_folder, file.replace('.csv', '.txt'))

        try:
            data = pd.read_csv(file_path)

            with open(output_file, 'w', encoding='utf-8') as text_file:
                text_column = data['text']
                concatenated_text = '. '.join(text_column)
                text_file.write(concatenated_text)

            with open(output_file, 'r') as text_file:
                podcast = text_file.read()
                podcasts.append(podcast)
                file_names.append(file)

        except FileNotFoundError:
            print(f"File '{file}' was not found. Skipping...")


corpus = podcasts
vectorizer = TfidfVectorizer(
    min_df=1,
    stop_words='english',
    lowercase=True,
    ngram_range=(1, 2),  
    #sublinear_tf=True,  
    #max_features=5000,  
)
model = vectorizer.fit_transform(corpus)
similarities = cosine_similarity(model)

#Similiarity between Podcasts
similarities_between_podcast = [(similarity, file_names[i], file_names[j]) for i, row in enumerate(similarities) for j, similarity in enumerate(row) if j > i]

similarities_between_podcast = sorted(similarities_between_podcast, reverse=True)
for similarity, podcast_a, podcast_b in similarities_between_podcast:
    print(f"Similarity between {podcast_a} and {podcast_b}: {similarity:.2f}")

#Top10 words in each podcast
tfidf_array = model.toarray()
feature_names = vectorizer.get_feature_names_out()

def get_top_words(tfidf_vector, feature_names, top_n=10):
    sorted_nzs = np.argsort(tfidf_vector)[-top_n:][::-1]
    return [(feature_names[i], tfidf_vector[i]) for i in sorted_nzs]

for idx, doc in enumerate(corpus):
    print(f"Top words in {file_names[idx]}")
    top_words = get_top_words(tfidf_array[idx], feature_names)
    for word, score in top_words:
        print(f"{word}: {score:.4f}")
    print("--------")

#Know in what podcast would this query fit better
query="what language do you prefer, python or javascript?"
query_vec = vectorizer.transform([query])

for idx, doc_name in enumerate(corpus):
    print(f"Cosine similarity between {file_names[idx]} and query: {cosine_similarity(model[idx],query_vec )}")
