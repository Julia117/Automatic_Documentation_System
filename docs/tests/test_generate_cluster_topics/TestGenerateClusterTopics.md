# TestGenerateClusterTopics (class)

**Code:**
```python
class TestGenerateClusterTopics(unittest.TestCase):
    def setUp(self):
        self.gad_en = example_instruments["GAD-7 English"]
        self.gad_pt = example_instruments["GAD-7 Portuguese"]

    def test_topics_english(self):
        match_response = match_instruments([self.gad_en])
        clusters = cluster_questions_affinity_propagation(match_response.questions,
                                                          match_response.similarity_with_polarity)

        self.assertLess(1, len(clusters[0].keywords))
        self.assertLess(1, len(clusters[1].keywords))
        self.assertLess(1, len(clusters[2].keywords))
        self.assertLess(1, len(clusters[3].keywords))

        self.assertGreater(6, len(clusters[0].keywords))
        self.assertGreater(6, len(clusters[1].keywords))
        self.assertGreater(6, len(clusters[2].keywords))
        self.assertGreater(6, len(clusters[3].keywords))
        #
        # self.assertEqual(set(clusters[0].keywords), set(['feeling', 'annoyed', 'easily', 'becoming', 'irritable']))
        # self.assertEqual(set(clusters[1].keywords), set(['worrying', 'much', 'different']))
        # self.assertEqual(set(clusters[2].keywords), set(['trouble', 'relaxing', 'hard', 'restless']))
        # self.assertEqual(set(clusters[3].keywords), set(['along', 'care', 'checked']))

    def test_topics_portuguese(self):
        match_response = match_instruments([self.gad_pt])
        clusters = cluster_questions_affinity_propagation(match_response.questions,
                                                          match_response.similarity_with_polarity)

        self.assertLess(1, len(clusters[0].keywords))
        self.assertLess(1, len(clusters[1].keywords))

        self.assertGreater(6, len(clusters[0].keywords))
        self.assertGreater(6, len(clusters[1].keywords))
        #
        # self.assertEqual(set(clusters[0].keywords), set(['preocupar', 'diversas', 'coisas']))
        # self.assertEqual(set(clusters[1].keywords), set(['ficar', 'relaxar', 'dificuldade', 'aborrecido']))

    def test_topics_english_portuguese(self):
        match_response = match_instruments([self.gad_en, self.gad_pt])
        clusters = cluster_questions_affinity_propagation(match_response.questions,
                                                          match_response.similarity_with_polarity)

        self.assertLess(1, len(clusters[0].keywords))
        self.assertLess(1, len(clusters[1].keywords))
        self.assertLess(1, len(clusters[2].keywords))
        self.assertLess(1, len(clusters[3].keywords))

        self.assertGreater(6, len(clusters[0].keywords))
        self.assertGreater(6, len(clusters[1].keywords))
        self.assertGreater(6, len(clusters[2].keywords))
        self.assertGreater(6, len(clusters[3].keywords))
        #
        # self.assertEqual(set(clusters[0].keywords), set(['anxious', 'nervous', 'edge', 'nervoso']))
        # self.assertEqual(set(clusters[1].keywords), set(['worrying', 'coisas', 'preocupar']))
        # self.assertEqual(set(clusters[2].keywords), set(['trouble', 'relaxing', 'dificuldade', 'relaxar']))
        # self.assertEqual(set(clusters[3].keywords), set(['aborrecido', 'facilmente', 'irritado', 'annoyed', 'becoming']))
        # self.assertEqual(set(clusters[4].keywords), set(['acontecer', 'algo', 'medo']))
        # self.assertEqual(set(clusters[5].keywords), set(['along', 'difficult']))

    def test_langdetect_english_portuguese(self):
        for question in self.gad_en.questions:
            try:
                lang = detect(question.question_text)
            except:
                pass

            self.assertEqual(lang, "en")

        for question in self.gad_pt.questions:
            try:
                lang = detect(question.question_text)
            except:
                pass

            self.assertEqual(lang, "pt")
```

**Explanation:**
**TestGenerateClusterTopics Class Explanation**

This class is a unit test case for generating cluster topics. It contains four test methods:

1. `test_topics_english`: Tests the generation of cluster topics for English language instruments.
2. `test_topics_portuguese`: Tests the generation of cluster topics for Portuguese language instruments.
3. `test_topics_english_portuguese`: Tests the generation of cluster topics for both English and Portuguese language instruments.
4. `test_langdetect_english_portuguese`: Tests the language detection for English and Portuguese language instruments.

The class uses the `match_instruments` function to match the instruments and then uses the `cluster_questions_affinity_propagation` function to generate cluster topics. The test methods assert that the generated cluster topics have a minimum and maximum number of keywords.

The `setUp` method initializes the English and Portuguese language instruments from the `example_instruments` dictionary.

The `detect` function is used to detect the language of the question text in the `test_langdetect_english_portuguese` method.

Overall, this class is designed to test the functionality of generating cluster topics for different language instruments.

**Imports:**
```
import sys, import unittest, from harmony import match_instruments, example_instruments, from harmony.matching.generate_cluster_topics import generate_cluster_topics, from harmony.matching.affinity_propagation_clustering import cluster_questions_affinity_propagation, from langdetect import detect, DetectorFactory
```
