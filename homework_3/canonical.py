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


if __name__ == '__main__':
    corpus = ['Crock Pot Pasta Never boil pasta again', 'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(count_matrix)
    print(vectorizer.get_feature_names())
