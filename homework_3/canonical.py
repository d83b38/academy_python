import math


class CountVectorizer:
    """ Ω Docstring  about CountVectorizer na minimalkah Ω """
    def __init__(self):
        self._vocabulary = {}
        self._vocabulary_lenght = 0
        self.data = None

    def _create_vocabulary(self, data):
        key_index = 0
        modified_corpus = []
        for sent in data:
            modified_sent = [x.lower() for x in sent.split()]
            modified_corpus.append(modified_sent)
            for word in modified_sent:
                if word not in self._vocabulary:
                    self._vocabulary[word] = key_index
                    key_index += 1

        self._vocabulary_lenght = key_index
        self.data = modified_corpus

    def fit_transform(self, data):
        matrix = []
        self._create_vocabulary(data)
        for sent in self.data:
            counters_vector = [0 for x in range(0, self._vocabulary_lenght)]
            unique_words_sent = set()
            for word in sent:
                unique_words_sent.add(word)
                if word in unique_words_sent:
                    counters_vector[self._vocabulary[word]] = counters_vector[self._vocabulary[word]] + 1
            matrix.append(counters_vector)
        return matrix

    def get_feature_names(self):
        if not self._vocabulary:
            print('Warning: vocabulary is empty, use fit_transfrom() first')
            return []
        feature_names = [" " for x in range(0, self._vocabulary_lenght)]
        for k, v in self._vocabulary.items():
            feature_names[v] = k
        return feature_names


class TfidfTransformer:

    def _tf_transform(self, matrix):
        """ dfd """
        tf_matrix = []
        for vector in matrix:
            all_count = sum(vector)
            tf_matrix.append([round(x / all_count, 3) for x in vector])
        return tf_matrix

    def _idf_transform(self, matrix):
        """ dfds """
        doc_count = len(matrix)
        vector_len = len(matrix[0])
        idf_vector = []
        for i in range(0, vector_len):
            doc_sum = 0
            for vector in matrix:
                if vector[i] > 0:
                    doc_sum += 1
            idf_vector.append(round(math.log((doc_count + 1) / (doc_sum + 1)) + 1, 3))
        return idf_vector

    def fit_transform(self, matrix):
        tf_matrix = self._tf_transform(matrix)
        idf = self._idf_transform(matrix)
        tf_idf_matrix = []

        for tf_vector in tf_matrix:
            tf_idf_vector = []
            zipped = zip(tf_vector, idf)
            for k, m in zipped:
                tf_idf_vector.append(round(k * m, 3))
            tf_idf_matrix.append(tf_idf_vector)
        return tf_idf_matrix


class TfidVectorizer(CountVectorizer):
    """ df sdf """
    def __init__(self):
        self._transformer = TfidfTransformer()
        self._vocabulary = {}
        super().__init__()

    def fit_transform(self, data):
        matrix = super().fit_transform(data)
        return self._transformer.fit_transform(matrix)


if __name__ == '__main__':
    corpus = ['Crock Pot Pasta Never boil pasta again', 'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    vectorizer = TfidVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
