import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
#from nltk.tokenize import word_tokenize 
#from nltk.stem import PorterStemmer

def clean_text(text):
    ## Remove puncuation
    try:
        ## Convert words to lower case and split them
        ## Clean the text
        lemmatizer = WordNetLemmatizer()
        #stemmer = PorterStemmer()
        text_stem=""
    
        #Added by Ramakant
        text = re.sub(r'<.*?>+', '', text)
        text = re.sub(r'\W+', ' ', text)
        text = re.sub(r'[0-9+]', '', text)
        text = re.sub(r'\s+', ' ', text)
        ## Remove stop words
        stops = set(stopwords.words("english"))

        #tops = ['own', "haven't", 'through', "wasn't", 'those', 'his', 'that', 'they', 'same', 'hers', 'y', 'mustn', 'my', 'doing', 'again', "don't", 'below', 'between', 'during', 'by', "weren't", 'is', 'all', 'some', 'over', 'about', 'shan', 'until', 'only', 'will', 's', 'was', 't', 'has', 'did', 'at', 'any', 'don', "aren't", 'mightn', 'needn', 'out', 'our', 'couldn', 'what', "you'll", 'up', 'very', 'now', 'll', "mightn't", 'ain', 'just', 'or', 'how', 'ourselves', 'down', 'these', 'didn', 'it', 'are', 'more', "wouldn't", 'from', 'had', 'and', 'against', 'we', 'under', "isn't", 'theirs', 've', 'herself', 'hasn', 'where', 'you', 'i', "won't", 'why', 'won', 'off', 'd', 'doesn', 'weren', 'can', "shan't", 'further', "mustn't", 'when', 'aren', 'here', 'if', 'have', 'ma', 'an', 'were', 'this', 'each', 'does', 'yourselves', 'its', 'of', 'for', "she's", 'while', 'themselves', 'most', 'no', 'nor', 'being', 'to', 'himself', 'myself', "it's", 'shouldn', 'as', 'other', 'itself', 'do', 'your', 'above', "doesn't", 'because', 'yours', 'been', 'both', 'a', 'be', 'in', 'then', 'isn', 'm', "that'll", 'hadn', "you're", "needn't", 'should', 'the', 'into', 'their', "should've", 'am', "hadn't", 'there', 'so', 'than', 'with', "hasn't", 'after', 'who', 'before', 'haven', "you've", "couldn't", 'which', "didn't", "you'd", 'but', 'too', 'she', 'whom', 'me', 're', 'wasn', 'them', 'such', 'ours', 'o', 'her', 'few', 'him', 'yourself', "shouldn't", 'once', 'wouldn', 'he', 'having', 'on']
        #ext = str([w for w in text if not w in stops and len(w) >= 2])
        text = text.split()
        #text = " ".join(text)
       # text = ' '.join(text.split())
        #apply lemmatizer
        for w in text:
            text_stem=text_stem+" "+lemmatizer.lemmatize(w)
    except:
        pass
    return text_stem