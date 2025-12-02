# test_single_instrument_simple (function)

**Code:**
```python
def test_single_instrument_simple(self):
        match_response = match_instruments([instrument_en],
                                           mhc_questions=mhc_questions,
                                           mhc_embeddings=mhc_embeddings,
                                           mhc_all_metadatas=mhc_metadata)
        self.assertEqual(2, len(match_response.questions))

        topics = match_response.questions[0].topics_strengths
        top_topic = list(topics)[0]
        self.assertEqual("alcohol use", top_topic)
        self.assertLess(0.1, topics[top_topic])
```

**Explanation:**
**Function Explanation: `test_single_instrument_simple`**

This function is a unit test case written in Python using the `unittest` framework. It tests the functionality of the `match_instruments` function, which is not shown in this code snippet.

**What it does:**

1. It calls the `match_instruments` function with a single instrument (`instrument_en`) and some metadata (`mhc_questions`, `mhc_embeddings`, `mhc_all_metadatas`).
2. It asserts that the response from `match_instruments` contains exactly 2 questions.
3. It extracts the topics and their strengths from the first question.
4. It asserts that the top topic is "alcohol use" and its strength is greater than 0.1.

**In simple terms:**

This test case checks if the `match_instruments` function can correctly match a single instrument to a set of metadata and return the expected results. It verifies that the output contains the correct number of questions and that the topics and their strengths are as expected.

**Imports:**
```
import sys, import unittest, import numpy as np, from sentence_transformers import SentenceTransformer, from harmony import match_instruments, from harmony.schemas.requests.text import Instrument, Question
```
