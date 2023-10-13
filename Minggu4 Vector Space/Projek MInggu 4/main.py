import streamlit as st
import pandas as pd
import numpy as np
import nltk
import re
import contractions
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib
import sys

pd.set_option("display.max_columns", None)
nltk.download('punkt')
nltk.download('stopwords')

data_film = pd.read_csv("Dataset/movies.csv")
data_film.fillna(" ", axis=0, inplace=True)
data_film["konten_film"] = data_film["genres"] + " " + data_film["overview"] + " " + data_film["keywords"] + " " + data_film["tagline"] + " " + data_film["cast"] + " " + data_film["director"]

stop_words = nltk.corpus.stopwords.words('english')

def normalize_document(doc):
    doc = re.sub(r'[^a-zA-Z0-9\s]', '', doc, re.I|re.A)
    doc = doc.lower()
    doc = doc.strip()
    doc = contractions.fix(doc)
    tokens = nltk.word_tokenize(doc)
    filtered_tokens = [token for token in tokens if token not in stop_words]
    doc = ' '.join(filtered_tokens)
    return doc

normalisasi_corpus = np.vectorize(normalize_document)
hasil_normalize_corpus = normalisasi_corpus(list(data_film['konten_film']))

vectorizer = TfidfVectorizer()
fitur_vectors = vectorizer.fit_transform(hasil_normalize_corpus)
kemiripan = cosine_similarity(fitur_vectors)

st.header("Halo")
judul_film = st.text_input("Masukan Judul Film")
judul_film = judul_film.lower()

if judul_film == "off":
    st.write("Program selesai")
    st.stop()

list_judul_film_dari_dataset = data_film["title"].tolist()

pencarian_judul_terdekat_dari_user = difflib.get_close_matches(judul_film, list_judul_film_dari_dataset)

pencarian_judul_terdekat_dari_user_str = "".join(pencarian_judul_terdekat_dari_user[0])

pencarian_judul_terdekat_dari_user_str = pencarian_judul_terdekat_dari_user_str.lower()

if not pencarian_judul_terdekat_dari_user:
    st.write("Tidak ada judul film yang cocok ditemukan untuk " + judul_film)

if judul_film != pencarian_judul_terdekat_dari_user_str:
    yesNo = st.text_input("Maksud anda film: " + pencarian_judul_terdekat_dari_user_str + "? (yes/no)")
    yesNo = yesNo.lower()
    if yesNo == "yes":
        judul_paling_mirip = pencarian_judul_terdekat_dari_user[0]
        index_dari_judul_film = data_film[data_film.title == judul_paling_mirip]['index'].values[0]
        kemiripan_skor = list(enumerate(kemiripan[index_dari_judul_film]))
        urutan_kemiripan_film = sorted(kemiripan_skor, key=lambda x: x[1], reverse=True)
        i = 1
        for film in urutan_kemiripan_film:
            index = film[0]
            judul_dari_index = data_film[data_film.index == index]['title'].values[0]
            if (i < 7):
                if (i == 1):
                    st.write('Film anda ditemukan: ', judul_dari_index)
                    i += 1
                    st.write("=====================================")
                    st.write("5 rekomendasi film yang serupa dengan " + judul_dari_index)
                else:
                    st.write(i - 1, '.', judul_dari_index)
                    i += 1
    else:
        st.write("Tidak ada judul film yang cocok ditemukan untuk " + judul_film)
else:
    judul_paling_mirip = pencarian_judul_terdekat_dari_user[0]
    index_dari_judul_film = data_film[data_film.title == judul_paling_mirip]['index'].values[0]
    kemiripan_skor = list(enumerate(kemiripan[index_dari_judul_film]))
    urutan_kemiripan_film = sorted(kemiripan_skor, key=lambda x: x[1], reverse=True)
    i = 1
    for film in urutan_kemiripan_film:
        index = film[0]
        judul_dari_index = data_film[data_film.index == index]['title'].values[0]
        if (i < 7):
            if (i == 1):
                st.write('Film anda ditemukan: ', judul_dari_index)
                i += 1
                st.write("=====================================")
                st.write("5 rekomendasi film yang serupa dengan " + judul_dari_index)
            else:
                st.write(i - 1, '.', judul_dari_index)
                i += 1
