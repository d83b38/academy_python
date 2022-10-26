import math


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
