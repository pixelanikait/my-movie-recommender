## Overview:
Spam classifier:
An ML mini project that recommends similar movies based on genre, cast, director, overview, etc.
Uses python, scikit-learn, pandas, rapidfuzz
uses TF-IDF vectorization and cosine similarity


## Installation:

`git clone https://github.com/pixelanikait/my-movie-recommender.git`

`cd my-movie-recommender`

`pip install -r requirements.txt`

## Usage:
1. Train model: `python train.py`
2. Run classifier: `python main.py`

## Example Output:
```text
Enter a movie name: Interstellar
Closest match:  Interstellar
Recommended movies: 
Contact
Apollo 13
The Martian
Space Cowboys
Space Pirate Captain Harlock
```


## Data from:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Unzip and add to:
```text
data/
    tmbd_5000_movies.csv
    tmdb_5000_credits.csv
```
