import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

# download resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')


# instantiate the sentiment analyzer
sia = SentimentIntensityAnalyzer()


def preprocess_text(text):
    # tokenize text
    tokens = word_tokenize(text)

    # remove stop words
    tokens = [token.strip() for token in tokens if token not in stopwords.words('english')]

    # lemmatize text
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return ' '.join(tokens)


def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'


data = pd.read_csv('quotes.csv')

# add sentiment of each quote to the dataframe
data['Sentiment'] = data['Quote'].apply(lambda x: analyze_sentiment(preprocess_text(x)))

# save the dataframe to a csv file
data.to_csv('quotes_with_sentiment.csv', index=False)