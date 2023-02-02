import streamlit as st


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from string import punctuation
from heapq import nlargest

import spacy




def NLTK_Summarization(doc):
    
    stopword = stopwords.words("english")
    words = word_tokenize(doc)
    for word in words:
        word = word.lower()
        if word in stopword:
            words.remove(word)
    
    

    '''
    Here we have created 2 list each having two separate number of entities.
    First list contains list of words which is then filtered by removing all the stopwords and then removing all the punctuation which are predefined in the given strings
    '''


    FreqDist = dict() #This is the dictionary which is created using the constructor called as dict. It is empty at this point of time.
    for word in words:
        if word not in FreqDist:
            FreqDist[word] = 1
        else:
            FreqDist[word] += 1

    '''
    Here we have created dictionary with the key and value pairs called as dict
    As we will be iterating through the list of words in the word list if that word is not present in the dictionary then we it will be added in the dictionary with initial value of 1 and after every occurence of the word in the FreqDist its value will be increamented by 1. i.e its value in the dictionary
    '''

    sentences = sent_tokenize(doc)
    max_freq = max(FreqDist.values())
    for word in FreqDist.keys():
        FreqDist[word] = (FreqDist[word] / max_freq)

    '''
    This block of code is used for purpose of making each value in the FreqDist dictionary on the range of 0-1 so that it can be easy to calculate the Frequency calculations 
    '''

    sentence_score = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in FreqDist.keys():
                if len(sent.split(" ")) < 30:
                    if sent not in sentence_score.keys():
                        sentence_score[sent] = FreqDist[word]
                    else:
                        sentence_score[sent] += FreqDist[word]

    '''
    Here we have got the dictionary of the words with their frequency distribution 
    Now new dictionary is created where we each sentence will be given the ranking based on the occurence of the word in the sentence from the frequency distribution dictionary
    Whole sentence will be splitted on the basis of the blank spaces and then this can result in separate words in the dictionary and hence if number of words in the given dictionary is less than 30 then algorithm will proceed.
    For every occurence of sentence it will be assigned value if any word is present in the FreqDist dictionary.
    Hence its value will be increased by value of word in freqDist dictionary
    '''

    Summary_sentence = nlargest(8, sentence_score, key=sentence_score.get)
    summary = " ".join(Summary_sentence)
    return summary

    '''
    This nlargest function takes three arguements
    8 is the number of sentence that we want to have in the summary
    sentence score is dictionary having each of the sentence having assigned rank
    and key has assigned value from dictionary after getting value using method get
    '''

def Spacy_Summarization(doc):
    stopword = spacy.lang.en.stop_words
    words = word_tokenize(doc)

    for word in words:
        if word in stopword:
            words.remove(word)
        else:
            word = word.lower()
    
    FreqDist = dict()
    for word in words:
        if word in FreqDist:
            FreqDist[word] += 1
        else:
            FreqDist[word] = 1

    sentences = sent_tokenize(doc)
    sentence_score = {}
    for sent in sentences:
        for word in sentences(word_tokenize(sent.lower())):
            if word in FreqDist.keys():
                if len(sent.split(" ")) < 30:
                    if sent not in sentence_score:
                        sentence_score[sent] = FreqDist[word]
                    else:
                        sentence_score[sent] += FreqDist[word]
    
    maxFreq = nlargest(8, sentence_score, key=sentence_score.get)
    final_summary = " ".join(maxFreq)
    return final_summary

def main():
    st.title("Text Summarization using NLP")
    activites = ["Summarize via text"]
    choices = st.sidebar.selectbox("Select Activities", activites)

    if choices == "Summarize via text":
        st.subheader("Summary using NLP")
        text_input = st.text_area("Enter text here", "Enter text")

        summary_choice = st.selectbox("Your Choice", ["NLTK", "Spacy"])

        if st.button("Summarize via text"):
            if summary_choice == "NLTK":
                result = NLTK_Summarization(text_input)
            elif summary_choice == "Spacy":
                result = Spacy_Summarization(text_input)
            
            st.write(result)


if __name__ == "__main__":
    main()







