import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest

stopwords = list(STOP_WORDS)

nlp = spacy.load('en_core_web_sm')

def summarize(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    # print('Decrypted tokens are :: ', tokens)

    from string import punctuation
    punctuation = punctuation + '\n'
    # print('Punctuations ::', punctuation)

    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    # print('Word frequencies :: ', word_frequencies)
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

    sentence_tokens = [sent for sent in doc.sents]
    # print('Sentence token :: ', sentence_tokens)

    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    # print('Sentence Scores ::', sentence_scores)
    select_length = int(len(sentence_tokens)*0.3)
    summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
    # print('Raw ::', summary)
    final_summary = [word.text for word in summary]
    # print('Final Summary :: ', final_summary)
    summary = ' '.join(final_summary)
    # print('Summary ::', summary)
    return summary