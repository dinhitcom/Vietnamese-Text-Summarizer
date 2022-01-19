from pyvi import ViTokenizer
from tqdm import tqdm
import gensim
import os
import pickle


HOME = os.path.dirname(__file__)

train_path = os.path.join(HOME, 'dataset\\Train_Full\\')

def get_data(dir_path):
    data = []

    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)

        with open(file_path, 'r', encoding="utf-16") as f:

            lines = f.readlines()

            for line in lines:
                sentences = line.split('.')

                for sentence in sentences:
                    if len(sentence) > 10:
                        sentence = gensim.utils.simple_preprocess(sentence)
                        sentence = ' '.join(sentence)
                        sentence = ViTokenizer.tokenize(sentence)
                        data.append(sentence)

    return data

sentences = []

directories = []

for path in os.listdir(train_path):
    directories.append(os.path.join(train_path, path))

for directory in tqdm(directories):
    sens = get_data(directory)
    sentences = sentences + sens

print(len(sentences))
pickle.dump(sentences, open('./sentences.pickle', 'wb'))
