# add_executive_summary (function)

**Code:**
```python
def add_executive_summary(self, stats: dict):
        """Add executive summary with key metrics."""
        self.chapter_title("Executive Summary")
        
        # Key metrics in boxes
        metrics = [
            ("Total Questions Analyzed", stats['total_questions']),
            ("Questions Successfully Harmonised", stats['harmonised_questions']),
            ("Harmonisation Success Rate", f"{stats['success_rate']:.1f}%"),
            ("Average Match Score", f"{stats['avg_match_score']:.1f}%"),
        ]
        
        box_width = 90
        box_height = 25
        x_start = 15
        y_start = self.get_y()
        
        for i, (label, value) in enumerate(metrics):
            x = x_start + (i % 2) * (box_width + 10)
            y = y_start + (i // 2) * (box_height + 5)
            
            self.set_xy(x, y)
            
            # Box border
            self.set_fill_color(240, 248, 255)
            self.rect(x, y, box_width, box_height, 'F')
            self.rect(x, y, box_width, box_height, 'D')
            
            # Label
            self.set_xy(x + 2, y + 3)
            self.set_font("Arial", "", 9)
            self.set_text_color(100, 100, 100)
            self.cell(box_width - 4, 8, sanitize(label), align="C")
            
            # Value
            self.set_xy(x + 2, y + 12)
            self.set_font("Arial", "B", 14)
            self.set_text_color(31, 81, 155)
            self.cell(box_width - 4, 10, sanitize(str(value)), align="C")
            self.set_text_color(0, 0, 0)
        
        self.set_y(y_start + 60)
```

**Explanation:**
**Function Explanation: `add_executive_summary`**

This function generates an executive summary section in a report, displaying key metrics in a visually appealing format.

**Key Features:**

1. **Chapter Title**: Sets the title of the executive summary section.
2. **Key Metrics**: Displays four key metrics in boxes:
	* Total Questions Analyzed
	* Questions Successfully Harmonised
	* Harmonisation Success Rate
	* Average Match Score
3. **Box Layout**: Each metric is displayed in a box with a label and value, aligned horizontally and vertically.
4. **Customization**: The function uses various settings to customize the appearance of the boxes, such as font, color, and alignment.

**Example Use Case:**

This function can be used in a report generation system to provide a concise and informative summary of key metrics, making it easier for users to understand the results of a harmonization process.

**Imports:**
```
import os, import io, from datetime import datetime, from typing import List, Optional, Tuple, import tempfile, from fpdf import FPDF, from harmony.schemas.requests.text import Instrument, from harmony.schemas.responses.text import MatchResponse
```
