# generate_pdf_report (function)

**Code:**
```python
def generate_pdf_report(
        match_response: MatchResponse,
        instruments: List[Instrument],
        filename: str = "harmony_report.pdf",
        threshold: float = 0.5
) -> str:
    """
    ORIGINAL FUNCTION - Maintains backward compatibility with existing tests.
    Generate a PDF of matched questions (basic version).
    
    :param match_response: the MatchResponse from match_instruments(...)
    :param instruments: the list of Instrument objects you passed in
    :param filename: output path
    :param threshold: only show matches with |score| >= threshold
    :return: absolute path to the generated PDF file
    """
    if not instruments or not match_response:
        raise ValueError("Instruments and match_response cannot be empty")
    
    pdf = FPDF()
    pdf.add_page()

    # Header
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, sanitize("Harmony Match Report"), ln=True, align="C")
    pdf.set_font("Arial", "", 10)
    pdf.cell(
        0, 10,
        sanitize(f"Generated on {datetime.now():%Y-%m-%d %H:%M:%S}"),
        ln=True, align="C"
    )
    pdf.ln(5)

    # 1) Map question-index → (instrument_name, question_no)
    question_meta = {}
    idx = 0
    for inst in instruments:
        inst_name = inst.instrument_name or f"Instrument {idx + 1}"
        for q_num, q in enumerate(inst.questions or []):
            question_meta[idx] = (inst_name, getattr(q, 'question_no', q_num + 1))
            idx += 1

    # 2) Collect & sort all pairs
    raw_matches = []
    questions = match_response.questions
    sim = match_response.similarity_with_polarity
    
    if sim is None or questions is None:
        raise ValueError("Invalid match response: missing similarity matrix or questions")
    
    for i in range(sim.shape[0]):
        for j in range(sim.shape[1]):
            if i != j and sim[i][j] > 0:
                raw_matches.append((i, j, sim[i][j]))
    
    raw_matches.sort(key=lambda x: abs(x[2]), reverse=True)

    # 3) Count how many pass the threshold
    displayed = sum(1 for (_, _, s) in raw_matches if abs(s) >= threshold)

    # 4) Chapter title with count and threshold
    pct = int(threshold * 100)
    pdf.set_font("Arial", "B", 11)
    pdf.set_fill_color(230, 230, 230)
    pdf.cell(0, 8, sanitize(f"Matched Questions ({displayed}) with Threshold: {pct}%"), 
             ln=True, fill=True)
    pdf.ln(2)

    if displayed == 0:
        pdf.set_font("Arial", "I", 10)
        pdf.cell(0, 10, sanitize(f"No matches found above {pct}% threshold."), ln=True)
    else:
        # 5) Table header
        w1, w2, w3 = 60, 20, 110
        pdf.set_font("Arial", "B", 10)
        pdf.cell(w1, 8, sanitize("Instrument"), border=1)
        pdf.cell(w2, 8, sanitize("Nr."), border=1)
        pdf.cell(w3, 8, sanitize("Question"), border=1)
        pdf.ln()

        # 6) Render each passing match
        total_w = w1 + w2 + w3
        for i, j, score in raw_matches:
            if abs(score) >= threshold:
                inst1, q1_no = question_meta.get(i, ("Unknown", "?"))
                inst2, q2_no = question_meta.get(j, ("Unknown", "?"))
                
                if i < len(questions) and j < len(questions):
                    q1 = questions[i]
                    q2 = questions[j]

                    # Row 1: Question 1
                    pdf.set_font("Arial", "", 9)
                    pdf.cell(w1, 6, sanitize(str(inst1)[:25]), border='TLR')
                    pdf.cell(w2, 6, sanitize(str(q1_no)), border='TR')
                    
                    # Handle multi-line text
                    q1_text = sanitize(q1.question_text or "No text available")
                    if len(q1_text) > 50:
                        q1_text = q1_text[:47] + "..."
                    
                    pdf.multi_cell(w3, 6, q1_text, border='TR')

                    # Row 2: Question 2
                    pdf.set_x(pdf.l_margin)
                    pdf.cell(w1, 6, sanitize(str(inst2)[:25]), border='LRB')
                    pdf.cell(w2, 6, sanitize(str(q2_no)), border='RB')
                    
                    q2_text = sanitize(q2.question_text or "No text available")
                    if len(q2_text) > 50:
                        q2_text = q2_text[:47] + "..."
                    
                    pdf.multi_cell(w3, 6, q2_text, border='RB')

                    # Score row
                    pdf.set_x(pdf.l_margin)
                    pdf.set_font("Arial", "I", 8)
                    pdf.cell(
                        total_w, 6,
                        sanitize(f"Match Score: {round(score * 100)}%"),
                        border='LRB',
                        ln=True
                    )

                    pdf.ln(4)

    # 7) Save
    try:
        out = os.path.abspath(filename)
        pdf.output(out)
        return out
    except Exception as e:
        raise IOError(f"Failed to save PDF report: {str(e)}")
```

**Explanation:**
**Function Explanation: `generate_pdf_report`**

This function generates a PDF report of matched questions between multiple instruments. It takes in the following parameters:

* `match_response`: The result of a matching process between instruments.
* `instruments`: A list of instrument objects.
* `filename`: The output path for the generated PDF file (default: "harmony_report.pdf").
* `threshold`: The minimum match score threshold (default: 0.5).

Here's a step-by-step breakdown of what the function does:

1. **Header**: Creates a header with the report title and timestamp.
2. **Map question-index to instrument and question number**: Creates a dictionary mapping question indices to their corresponding instrument names and question numbers.
3. **Collect and sort matches**: Retrieves all matching pairs from the `match_response` and sorts them by their match scores in descending order.
4. **Count matches above threshold**: Counts the number of matches that meet the specified threshold.
5. **Create chapter title**: Creates a chapter title with the count of matches and the threshold value.
6. **Render matches**: Iterates through the sorted matches and renders each one in a table format, including the instrument names, question numbers, and match scores.
7. **Save PDF**: Saves the generated PDF report to the specified output path.

The function raises a `ValueError` if either the `instruments` or `match_response` is empty.

**Imports:**
```
import os, import io, from datetime import datetime, from typing import List, Optional, Tuple, import tempfile, from fpdf import FPDF, from harmony.schemas.requests.text import Instrument, from harmony.schemas.responses.text import MatchResponse
```
