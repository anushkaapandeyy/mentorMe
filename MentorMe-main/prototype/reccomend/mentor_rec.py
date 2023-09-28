import numpy as np 
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("prototype\\reccomend\mentor_recom_c.csv")

vectorizer = TfidfVectorizer(stop_words='english')
vectors = vectorizer.fit_transform(df.Skills)

def mentor_recom(skills, recomm_count=5) : 
    title_vector = vectorizer.transform([skills])
    cosine_sim = cosine_similarity(vectors, title_vector)
    idx = np.argsort(np.array(cosine_sim[:,0]))[-recomm_count:]
    ans = df.iloc[idx].sort_values(by='Rating', ascending=False)
    print(ans.Mentor_name)
    return ans

mentor_recom('What to learn for machine learning?')