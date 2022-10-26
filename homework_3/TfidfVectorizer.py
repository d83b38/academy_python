import CountVectorizer as countvec
import TfidfTransformer as tfidftrnas


class TfidfVectorizer(countvec.CountVectorizer):
    """ df sdf """
    def __init__(self):
        self._transformer = tfidftrnas.TfidfTransformer()
        super()
        self._vocabulary = {}

    def fit_transform(self, data):
        matrix = super().fit_transform(data)
        return self._transformer.fit_transform(matrix)
