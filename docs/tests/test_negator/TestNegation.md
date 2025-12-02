# TestNegation (class)

**Code:**
```python
class TestNegation(unittest.TestCase):

    def test_simple_example(self):
        text = "I never feel depressed"
        print(negate(text, "en"))
        self.assertEqual("I feel depressed", negate(text, "en"))

    def test_simple_example_neg(self):
        text = "I feel depressed"
        print(negate(text, "en"))
        self.assertEqual("never I feel depressed", negate(text, "en"))

    def test_verb_can_negation_en(self):
        text = "I can't feel happy"
        self.assertEqual("I can feel happy", negate(text, "en"))

    def test_verb_will_negation_en(self):
        text = "I won't feel happy"
        self.assertEqual("I will feel happy", negate(text, "en"))

    def test_verb_shall_negation_en(self):
        text = "I shan't feel happy"
        self.assertEqual("I shall feel happy", negate(text, "en"))

    def test_simple_example_pt(self):
        text = "eu me sinto deprimido"
        self.assertEqual("não eu me sinto deprimido", negate(text, "pt"))

    def test_simple_example_pt_neg(self):
        text = "não eu me sinto deprimido"
        self.assertEqual(" eu me sinto deprimido", negate(text, "pt"))

    def test_simple_example_es(self):
        text = "mi siento deprimido"
        self.assertEqual("no mi siento deprimido", negate(text, "es"))

    def test_simple_example_de(self):
        text = "Ich fühle mich nicht deprimiert"
        self.assertEqual("Ich fühle mich deprimiert", negate(text, "de"))

    def test_simple_example_de_neg(self):
        text = "Ich fühle mich deprimiert"
        self.assertEqual("nicht Ich fühle mich deprimiert", negate(text, "de"))

    def test_simple_example_it(self):
        text = "mi sento depresso"
        self.assertEqual("non mi sento depresso", negate(text, "it"))
    #
    # def test_simple_example_fr(self):
    #     text = "je me sens deprimé"
    #     self.assertEqual("ne pas je me sens deprimé", negate(text, "fr"))
    #
    # def test_simple_example_fr(self):
    #     text = "Je suis content"
    #     self.assertEqual("Je ne suis pas content", negate(text, "fr"))
```

**Explanation:**
**Class Explanation:**

This is a unit test class named `TestNegation` that uses the `unittest` framework to test a function called `negate`. The `negate` function is not shown in this code snippet, but it's likely a function that takes a text string and a language code as input, and returns the negation of the input text in the specified language.

**What the class does:**

The class contains several test methods that test the `negate` function with different input texts and languages. Each test method creates a test case by calling the `negate` function with a specific input text and language code, and then asserts that the output is as expected.

**Purpose:**

The purpose of this class is to ensure that the `negate` function works correctly for different languages and input texts. By running these tests, developers can verify that the `negate` function produces the expected output for a wide range of inputs.

**Key Takeaways:**

* The `negate` function is not shown in this code snippet, but it's likely a function that takes a text string and a language code as input.
* The `TestNegation` class contains several test methods that test the `negate` function with different input texts and languages.
* The class uses the `unittest` framework to run the tests and assert that the output is as expected.

**Imports:**
```
import sys, import unittest, from harmony.matching.negator import negate
```
