import tfidf
# import unittest


# class TestTfIdf(unittest.TestCase):
def test_similarity():
    table = tfidf.TfIdf()
    table.add_document("foo", ["a", "b", "c", "d", "e", "f", "g", "h"])
    table.add_document("bar", ["a", "b", "c", "i", "j", "k"])
    table.add_document("baz", ["k", "l", "m", "n"])

    # self.assertEqual(
    print table.similarities(["a", "b", "c"])
    #     [["foo", 0.6875], ["bar", 0.75], ["baz", 0.0]])

test_similarity()
# if __name__ == "__main__":
#     unittest.main()
