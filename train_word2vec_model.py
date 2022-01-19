from gensim.models import Word2Vec
import pickle

sentences = pickle.load(open('./sentences.pickle', 'rb'))
print(len(sentences))
input_gensim = []

for sen in sentences:
    input_gensim.append(sen.split())

model = Word2Vec(input_gensim, vector_size=128, window=5, min_count=0, workers=4, sg=1)
model.wv.save("w2v.model")