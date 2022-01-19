def sent_tokenize(docs):
    import nltk

    return nltk.sent_tokenize(docs)


def preprocess(content, vocabulary, w2v_model, log=False):
    from pyvi import ViTokenizer
    import numpy as np
    # import nltk
    # print(content)

    contents_parsed = content.lower()
    contents_parsed = contents_parsed.replace('\n', ' ')
    contents_parsed = contents_parsed.strip()
    # print('ctps\n', contents_parsed)
    # sentences = nltk.sent_tokenize(contents_parsed)
    sentences = sent_tokenize(contents_parsed)
    # print('\nabc\n', sentences)
    # print(sentences)
    i = 0
    if log:
        for sentence in sentences:
            print(i, "===", sentence)
            i += 1

    X = []

    for sentence in sentences:
        # sentence = gensim.utils.simple_preprocess(sentence)
        # sentence = ' '.join(sentence)
        sentence_tokenized = ViTokenizer.tokenize(sentence)
        # print(sentence_tokenized)
        words = sentence_tokenized.split(" ")
        # print(words)
        sentence_vec = np.zeros(128)
        for word in words:
            if word in vocabulary:
                sentence_vec += w2v_model[word]
        # print(sentence_vec)
        X.append(sentence_vec)

    return X, sentences

def crawl_content(url):
    from bs4 import BeautifulSoup
    from urllib import request
    from urllib.parse import urlparse

    # url = 'https://vnexpress.net/tp-hai-phong-chuyen-thanh-vung-do-4413905.html'
    print(url)
    html = request.urlopen(url).read().decode('utf8')
    getHTML = BeautifulSoup(html, 'html.parser')
    domain = urlparse(url).netloc
    print(domain)
    if 'vnexpress.net' in domain:
        contents = getHTML.find_all('p', {'class': 'Normal'}, text=True)
        # print(contents)
    elif 'thanhnien.vn' in domain:
        contents = getHTML.find('div', {'id': 'abody'}).find_all('p')
    elif 'tuoitre.vn' in domain:
        contents = getHTML.select('#main-detail-body > p', text=True)
    elif 'nhandan.vn' in domain:
        contents = getHTML.select('.detail-content-body > p', text=True)
    else:
        return 'URL not found or not supported yet'

    return ' '.join([content.get_text(' ', strip=True) for content in contents])



def speak(text, lang='vi'):
    from gtts import gTTS
    import os
    import playsound

    tts = gTTS(text=text, lang=lang, slow=False)
    filename = "temp.mp3"
    # audio_file = os.path.dirname(__file__) + filename
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

    return 0