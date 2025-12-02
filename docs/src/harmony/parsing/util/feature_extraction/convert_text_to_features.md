# convert_text_to_features (function)

**Code:**
```python
def convert_text_to_features(text):
    token_texts = []
    token_start_char_indices = []
    token_end_char_indices = []
    token_properties = []

    char_indices_of_newlines = set()
    for idx, c in enumerate(text):
        if c == "\n":
            char_indices_of_newlines.add(idx)

    char_indices_of_question_marks = set()
    for idx, c in enumerate(text):
        if c == "?":
            char_indices_of_question_marks.add(idx)

    tokens = list(re_word.finditer(text))

    this_token_properties = {}

    for token in tokens:
        is_number = len(re_initial_num.findall(token.group()))
        is_number_dot = len(re_initial_num_dot.findall(token.group()))
        num_nums = len(re_contains_num.findall(token.group()))
        is_alpha = len(re_alpha.findall(token.group()))
        is_bracket = len(re_bracket.findall(token.group()))

        dist_to_prev_newline = token.start()
        for c in range(token.start(), 1, -1):
            if c in char_indices_of_newlines:
                dist_to_prev_newline = token.start() - c
                break

        dist_to_next_question_mark = len(text) - token.start()
        for c in range(token.start(), len(text)):
            if c in char_indices_of_question_marks:
                dist_to_next_question_mark = c - token.start()
                break

        is_capital = int(token.group()[0] != token.group()[0].lower())

        is_letters_and_numbers = int(is_alpha and num_nums > 0)

        this_token_properties = {"length": len(token.group()), "is_number": is_number,
                                 "is_alpha": is_alpha,
                                 "is_capital": is_capital,
                                 "is_letters_and_numbers": is_letters_and_numbers,
                                 "is_bracket": is_bracket,
                                 "is_number_dot": is_number_dot,
                                 "num_nums": num_nums,
                                 "dist_to_prev_newline": dist_to_prev_newline,
                                 "dist_to_next_question_mark": dist_to_next_question_mark,
                                 "char_index": token.start()}

        token_texts.append(token.group())
        token_start_char_indices.append(token.start())
        token_end_char_indices.append(token.end())
        token_properties.append(this_token_properties)

    all_property_names = list(sorted(this_token_properties))

    for idx in range(len(token_properties)):
        focus_dict = token_properties[idx]
        # Generate features including prev and next token.
        # There was no increase in performance associated with increasing this window. (TW 19/07/2024)
        for offset in range(-1, 2):
            if offset == 0:
                continue
            j = idx + offset
            if j >= 0 and j < len(token_properties):
                offset_dict = token_properties[j]
            else:
                offset_dict = {}

            for property_name in all_property_names:
                focus_dict[f"{property_name}_{offset}"] = offset_dict.get(property_name, 0)

    return token_texts, token_start_char_indices, token_end_char_indices, token_properties
```

**Explanation:**
**Function Explanation: `convert_text_to_features(text)`**

This function takes a text input and converts it into a set of features that can be used for machine learning or natural language processing tasks.

Here's a step-by-step breakdown:

1. **Tokenization**: The function splits the input text into individual tokens (words or characters) using regular expressions.
2. **Feature Extraction**: For each token, the function extracts various features such as:
	* Token length
	* Whether the token is a number, letter, or bracket
	* Whether the token is capitalized
	* Whether the token contains letters and numbers
	* Distance to the previous newline character
	* Distance to the next question mark
3. **Feature Aggregation**: The function aggregates the features for each token and its neighboring tokens (up to 1 token before and 1 token after).
4. **Output**: The function returns four lists:
	* `token_texts`: The original tokens
	* `token_start_char_indices`: The starting character indices of each token
	* `token_end_char_indices`: The ending character indices of each token
	* `token_properties`: The aggregated features for each token

This function is likely used as a preprocessing step for text classification, sentiment analysis, or other NLP tasks.

**Imports:**
```
import json, import re
```
