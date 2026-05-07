📘 Zipf’s Law of Abbreviation in Malayalam Digital Text

🧠 Overview

This project investigates the applicability of Zipf's law and the Law of Abbreviation in Malayalam digital text corpora.

The study analyzes:

1) word frequency distribution

2) word length patterns

3) statistical relationships between frequency and word length using Malayalam textual data collected from online sources.

The project follows a computational pipeline consisting of:

Web scraping,
Text cleaning, 
Frequency analysis, 
Linear regression and visualization

🎯 Objectives

1) Extract Malayalam text from digital sources
2) Clean and normalize Malayalam Unicode text
3) Compute word frequency distributions
4) Analyze word length patterns
5) Examine the relationship between:
    word frequency
    and word length
6) Visualize statistical trends using linear regression

⚙️ Workflow Pipeline

Web Scraping
 →
Text Cleaning 
 →
Frequency Analysis
 →
Word Length Calculation
 →
Linear Regression Plotting

 
📂 Project Structure

<pre>
zipfs-law-identification-malayalam/
├── data/
│   ├── corpus.txt
│   └── cleaned_corpus.txt
├── src/
│   ├── corpus_creation/
│   │   └── corpus_creation.py
│   ├── corpus_cleaning/
│   │   └── cleaning_corpus.py
│   └── corpus_analysis/
│       └── corpus_analysis.py
├── model/
│   └── linear_regression_model/
│       └── linear_regression_plotting.py
├── outputs/
│   ├── image.png
│   └── word_frequency.csv
├── LICENSE
└── README.md
</pre>

🔹 1. Corpus creation

Malayalam text data is collected from online news and digital text sources using:

BeautifulSoup and 
requests

The extracted text is stored in:

data/corpus.txt

🔹 2. Corpus Cleaning

The raw text is cleaned using Python regular expressions (re).

Cleaning includes:

removal of punctuation
removal of non-Malayalam characters
whitespace normalization

Malayalam Unicode range retained:

\u0D00 – \u0D7F

🔹 3. Frequency and Word Length Analysis

Word frequencies are calculated using:

collections.Counter

The analysis computes:

word frequency
word length

Processed results are stored as:
CSV frequency tables

🔹 4. Linear Regression and Visualization

The project uses:

NumPy
Scikit-learn
Matplotlib

to analyze the statistical relationship between:
word length and 
logarithmic word frequency

Regression plots are generated and saved as PNG files.

Example outputs:

Zipf distribution plots

regression line visualizations

🛠️ Technologies Used

Python, 
BeautifulSoup,
Regular Expressions (re),
NumPy,
Pandas,
Matplotlib,
Scikit-learn

🚀 How to Run

Run the pipeline
1. Scrape text
python src/corpus_creation/corpus_creation.py
2. Clean text
python src/corpus_cleaning/cleaning_corpus.py
3. Frequency analysis
python src/corpus_analysis/corpus_analysis.py
4. Generate regression plot
python src/model/linear_regression_plotting.py

⚠️ Dataset Note

The Malayalam corpus used in this project is collected from publicly available digital text sources.

Due to copyright and licensing considerations, the full dataset is not included in this repository.

📖 Research Relevance

This project contributes to:

Malayalam Computational Linguistics

Quantitative Linguistics

Corpus Linguistics

Statistical NLP for low-resource languages

🔮 Future Work

Expand corpus size
Analyze multiple Malayalam domains
Compare Zipf distributions across genres
Apply advanced statistical modeling

📬 Contact

Author: Ajin Jacob

Field: Computational Linguistics / Natural Language Processing
