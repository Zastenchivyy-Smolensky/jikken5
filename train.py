from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from preprocessing import clean_html,tokenize
from utils import load_dataset, train_and_eval