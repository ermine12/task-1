import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def extract_keywords(text_series, top_n=10):
    """
    Identifies common keywords (unigrams and bigrams).
    """
    # Stop words removes common English words like "the", "is", "at"
    vectorizer = CountVectorizer(stop_words='english', max_features=1000, ngram_range=(1, 2))
    X = vectorizer.fit_transform(text_series.dropna())
    
    # Sum word counts
    word_counts = X.sum(axis=0)
    words_freq = [(word, word_counts[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    
    return words_freq[:top_n]

def perform_topic_modeling(text_series, n_topics=3):
    """
    Uses LDA (Latent Dirichlet Allocation) to find topics.
    """
    vectorizer = CountVectorizer(stop_words='english', max_features=500)
    dtm = vectorizer.fit_transform(text_series.dropna())
    
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(dtm)
    
    topics = {}
    for index, topic in enumerate(lda.components_):
        # Get top 10 words for each topic
        topic_words = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]]
        topics[f"Topic {index+1}"] = topic_words
        
    return topics