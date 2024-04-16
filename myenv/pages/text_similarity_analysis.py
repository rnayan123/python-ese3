import streamlit as st
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    # Tokenization
    tokens = nltk.word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    
    # Remove non-alphabetic characters
    cleaned_tokens = [word for word in lemmatized_tokens if word.isalpha()]
    
    return cleaned_tokens

def main():
    st.title('Text Preprocessing')
    
    # Load the dataset
    df = pd.read_csv("WomensClothingE-CommerceReviews.csv")
    
    # Preprocess text
    df['cleaned_text'] = df['Review Text'].apply(preprocess_text)
    
    # Display the results
    st.write("Original Text:")
    st.write(df['Review Text'].head())
    
    st.write("Preprocessed Text:")
    st.write(df['cleaned_text'].head())

if __name__ == "__main__":
    main()
