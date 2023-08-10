# Sentiment Analysis of Scraped Quotes
Perform sentiment analysis on a collection of scraped quotes using Natural Language Processing (NLP) techniques and the NLTK library.

---

## Introduction
This project demonstrates how to perform sentiment analysis on a set of quotes that have been scraped from a website. The sentiment analysis is based on the sentiment intensity provided by the NLTK library's Sentiment Intensity Analyzer. The quotes are preprocessed by tokenization, removing punctuation, stopwords, and lemmatization before performing sentiment analysis.

In addition to sentiment analysis, this project includes an example of how to scrape quotes from a target website. The scraping process involves fetching HTML content, parsing it using the BeautifulSoup library, and extracting relevant information such as quotes, authors, and tags.

# Dependancies

```bash
pip install nltk 
```

```bash
pip install beautifulsoup4
```

```bash
pip install requests
```

```bash
pip install pandas
```

## Output 
The "main.py" script will create a CSV file named "quotes.csv", which will contain the following information for each quote:
* Quote
* Author
* Tags

The "SentimentAnalysis.py" script will analyze the quotes and give them a score based on the language used, based on the score it will either be classified as "Positive", "Neutral", or "Negative". Then a new CSV file will be added named "quotes_with_sentiment.csv" adding the "Sentiment" column.

## Note
This script is provided for educational purposes only and is meant to demonstrate basic web scraping techniques. Before scraping any website, please review the website's Terms of Service and Robots.txt file to ensure you are not violating any rules or policies.
