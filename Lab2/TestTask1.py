import unittest

from Task1 import count_sentences, average_sentence_length, count_of_non_declarative_sentences,\
                  average_word_length, top_ngrams


class TestTextAnalysis(unittest.TestCase):

    def setUp(self):
        self.text = "This is a text. It has multiple sentences. Some of them are declarative, while others are not! "

    def test_count_sentences(self):
        self.assertEqual(count_sentences(self.text), 2)

    def test_count_of_non_declarative_sentences(self):
        self.assertEqual(count_of_non_declarative_sentences(self.text), 1)

    def test_average_sentence_length(self):
        self.assertAlmostEqual(average_sentence_length(self.text), 31.5, delta=0.01)

    def test_average_word_length(self):
        self.assertAlmostEqual(average_word_length(self.text), 4.352941176470588, delta=0.01)

    def test_top_ngrams(self):
        expected_output = [('this is a text', 1), ('is a text it', 1), ('a text it has', 1),
                           ('text it has multiple', 1), ('it has multiple sentences', 1),
                           ('has multiple sentences some', 1), ('multiple sentences some of', 1),
                           ('sentences some of them', 1), ('some of them are', 1), ('of them are declarative', 1)]
        self.assertEqual(top_ngrams(self.text), expected_output)


if __name__ == '__main__':
    unittest.main()
