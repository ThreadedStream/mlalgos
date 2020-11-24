import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from bookapp.models import *


'''
    Content-based recommender,tailored to books,using
    TF-IDF algorithm in form of two primary classes: TfidfTransformer and CountVectorizer
    
    The main idea is in representing input data(titles of books) in form of matrix. 
    
'''
class ContentBasedBookRecommender:
    def __init__(self):
        self._execute_preparation_stage()

    def _execute_preparation_stage(self):
        books  = Book.objects.all()
        titles = []
        ids    = []
        for book in books:
            titles.append(book.title)
            ids.append(book.id)

        df_data = {'id' : ids, 'title': titles}
        self.df = pd.DataFrame(data=df_data)

        self.df['content'] = self.df[['id', 'title']].astype(str).apply(lambda x: ' // '.join(x),axis=1)

        self.tf = TfidfVectorizer(analyzer='word', ngram_range = (1,2), min_df = 0,
        stop_words = 'english')
        
        self.tfidf_matrix = self.tf.fit_transform(self.df['content'])
        self.cos_similarities = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
        
        self.results = {}
        for idx, row in self.df.iterrows():
            similar_indices = self.cos_similarities[idx].argsort()[:-100:-1]
            similar_items   = [(self.cos_similarities[idx][i], self.df['id'][i]) for i in similar_indices]
            self.results[row['id']] = similar_items[1:]

    def _item(self,id):
        title = self.df.loc[self.df['id'] == id]['content'].tolist()[0].split(' // ')[0]
        return title

    def recommend(self,item_id, num):
        recs = self.results[item_id][:num]
        for rec in recs:
            yield self._item(rec[1])
