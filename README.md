# Quotes Sentiment Analysis Project

This project provides a comprehensive pipeline for scraping quotes, analyzing their sentiment, and performing exploratory data analysis (EDA). It consists of three main components:
1. **`main.py`**: Scrapes quotes, authors, and tags from the website http://quotes.toscrape.com and saves them in a CSV file.
2. **`SentimentAnalysis.py`**: Analyzes the sentiment of the scraped quotes and appends the results to the dataset.
3. **`QuotesExampleEDA.ipynb`**: Performs EDA on the processed data to uncover insights using visualizations.

---

## Features

- **Web Scraping**: Scrape quotes, authors, and tags from multiple pages of a website.
- **Text Preprocessing**: Tokenize, remove stopwords, and lemmatize quotes for clean analysis.
- **Sentiment Analysis**: Classify quotes as Positive, Negative, or Neutral using VADER sentiment analysis.
- **Exploratory Data Analysis (EDA)**:
  - Visualize sentiment distribution.
  - Analyze the frequency of tags, authors, and common words.

---

## Installation

### Prerequisites
- Python 3.x
- Jupyter Notebook (optional for `.ipynb` files)

### Clone the Repository
```bash
git clone https://github.com/your-repository-link.git
cd your-project-directory
```

### Install Required Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Step 1: Scrape Quotes
Run the `main.py` script to scrape quotes, authors, and tags from the website.

```bash
python main.py
```

The scraped data will be saved in a file named `quotes.csv`.

### Step 2: Perform Sentiment Analysis
Run the `SentimentAnalysis.py` script to analyze the sentiment of the quotes.

```bash
python SentimentAnalysis.py
```

The processed data with sentiment analysis will be saved in a file named `quotes_with_sentiment.csv`.

### Step 3: Perform Exploratory Data Analysis (Optional)
Open the `QuotesExampleEDA.ipynb` file in Jupyter Notebook to visualize the data.

```bash
jupyter notebook QuotesExampleEDA.ipynb
```

---

## Project Structure

- **`main.py`**: Scrapes data from the website and saves it in a CSV file.
- **`SentimentAnalysis.py`**: Performs sentiment analysis on the scraped data.
- **`QuotesExampleEDA.ipynb`**: Explores and visualizes the processed data.
- **`quotes.csv`**: Contains scraped quotes, authors, and tags.
- **`quotes_with_sentiment.csv`**: Contains quotes with sentiment analysis results.

---

## Requirements

### Python Libraries
- nltk
- pandas
- requests
- bs4 (BeautifulSoup)
- plotly

---

## Example Outputs

### Sentiment Distribution
Displays the count of Positive, Negative, and Neutral quotes.

### Tag Distribution
Bar chart showing the most common tags associated with the quotes.

### Author Distribution
Bar chart showing the most quoted authors.

### Word Frequency Distribution
Scatterplot showing the most common words in the quotes.

---

## Contribution

Contributions are welcome! Feel free to fork the repository and submit pull requests for bug fixes or new features.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

