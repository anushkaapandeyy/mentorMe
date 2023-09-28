import numpy as np 
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("reccomend\\fourm.csv")

vectorizer = TfidfVectorizer(stop_words='english')
vectors = vectorizer.fit_transform(df.Questions)

def fourm_que (question, recomm_count = 5) : 
    title_vector = vectorizer.transform([question])
    cosine_sim = cosine_similarity(vectors, title_vector)
    idx = np.argsort(np.array(cosine_sim[:,0]))[-recomm_count:]
    ans = df.iloc[idx]
    print(ans)
    return ans

fourm_que('what should I study for machine ')