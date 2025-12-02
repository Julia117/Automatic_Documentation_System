# calculate_harmonisation_statistics (function)

**Code:**
```python
def calculate_harmonisation_statistics(
    match_response: MatchResponse,
    instruments: List[Instrument],
    raw_matches: List[Tuple],
    threshold: float
) -> dict:
    """Calculate comprehensive statistics about the harmonisation."""
    
    # Basic counts
    total_questions = sum(len(inst.questions or []) for inst in instruments)
    total_possible_matches = len(raw_matches)
    successful_matches = sum(1 for _, _, score in raw_matches if abs(score) >= threshold)
    
    # Questions that have at least one match above threshold
    questions_with_matches = set()
    for i, j, score in raw_matches:
        if abs(score) >= threshold:
            questions_with_matches.add(i)
            questions_with_matches.add(j)
    
    harmonised_questions = len(questions_with_matches)
    
    # Average scores
    successful_scores = [abs(score) for _, _, score in raw_matches if abs(score) >= threshold]
    
    avg_match_score = (sum(successful_scores) / len(successful_scores) * 100) if successful_scores else 0
    success_rate = (harmonised_questions / total_questions * 100) if total_questions > 0 else 0
    
    # Per-instrument statistics
    by_instrument = {}
    question_meta = {}
    idx = 0
    
    for inst_num, inst in enumerate(instruments):
        inst_name = inst.instrument_name or f"Instrument {inst_num + 1}"
        inst_questions = set(range(idx, idx + len(inst.questions or [])))
        
        # Count matches for this instrument
        inst_matches = sum(1 for i, j, score in raw_matches 
                          if abs(score) >= threshold and (i in inst_questions or j in inst_questions))
        
        # Average score for this instrument
        inst_scores = [abs(score) for i, j, score in raw_matches 
                      if abs(score) >= threshold and (i in inst_questions or j in inst_questions)]
        inst_avg_score = (sum(inst_scores) / len(inst_scores) * 100) if inst_scores else 0
        
        by_instrument[inst_name] = {
            'matches': inst_matches,
            'avg_score': inst_avg_score
        }
        
        for q_num, q in enumerate(inst.questions or []):
            question_meta[idx] = (inst_name, getattr(q, 'question_no', q_num + 1))
            idx += 1
    
    return {
        'total_questions': total_questions,
        'total_possible_matches': total_possible_matches,
        'successful_matches': successful_matches,
        'harmonised_questions': harmonised_questions,
        'success_rate': success_rate,
        'avg_match_score': avg_match_score,
        'by_instrument': by_instrument,
        'question_meta': question_meta
    }
```

**Explanation:**
This function calculates comprehensive statistics about the harmonisation of multiple instruments. 

Here's a simplified explanation:

1. It takes in four parameters:
   - `match_response`: The response from a matching algorithm.
   - `instruments`: A list of instruments being matched.
   - `raw_matches`: A list of raw matches between questions.
   - `threshold`: A score threshold to determine successful matches.

2. It calculates basic counts:
   - `total_questions`: The total number of questions across all instruments.
   - `total_possible_matches`: The total number of possible matches.
   - `successful_matches`: The number of matches with scores above the threshold.

3. It identifies questions with at least one match above the threshold and calculates the `harmonised_questions` count.

4. It calculates average scores:
   - `avg_match_score`: The average score of successful matches.
   - `success_rate`: The percentage of harmonised questions.

5. It calculates per-instrument statistics:
   - `by_instrument`: A dictionary with instrument names as keys and dictionaries containing the number of matches and average score for each instrument.
   - `question_meta`: A dictionary mapping question indices to instrument names and question numbers.

6. It returns a dictionary containing all the calculated statistics.

**Imports:**
```
import os, import io, from datetime import datetime, from typing import List, Optional, Tuple, import tempfile, from fpdf import FPDF, from harmony.schemas.requests.text import Instrument, from harmony.schemas.responses.text import MatchResponse
```
