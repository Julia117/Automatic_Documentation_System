# create_match_distribution_chart (function)

**Code:**
```python
def create_match_distribution_chart(raw_matches: List[Tuple], threshold: float):
    """Create a histogram of match score distribution."""
    if not GRAPHICS_AVAILABLE:
        return None
        
    scores = [abs(score) for _, _, score in raw_matches]
    
    if not scores:
        return None
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    try:
        # Create histogram
        n, bins, patches = ax.hist(scores, bins=min(20, len(set(scores))), 
                                  alpha=0.7, color='skyblue', edgecolor='black')
        
        # Color bars based on threshold
        for i, patch in enumerate(patches):
            if bins[i] >= threshold:
                patch.set_facecolor('lightgreen')
            else:
                patch.set_facecolor('lightcoral')
        
        # Add threshold line
        ax.axvline(threshold, color='red', linestyle='--', linewidth=2, 
                   label=f'Threshold ({threshold:.0%})')
        
        ax.set_xlabel('Match Score')
        ax.set_ylabel('Number of Question Pairs')
        ax.set_title('Distribution of Match Scores')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        return fig
    except Exception:
        plt.close(fig)
        return None
```

**Explanation:**
This function, `create_match_distribution_chart`, generates a histogram to visualize the distribution of match scores from a list of question pairs. 

Here's a step-by-step breakdown:

1. It first checks if graphics are available. If not, it returns `None`.
2. It extracts the absolute values of the match scores from the input list of question pairs.
3. If there are no scores, it returns `None`.
4. It creates a new figure and axis using matplotlib's `plt.subplots`.
5. It attempts to create a histogram of the match scores with a specified number of bins (minimum 20 or the number of unique scores).
6. It colors the histogram bars based on whether their corresponding bin value is above or below the specified threshold.
7. It adds a vertical line to the plot at the threshold value.
8. It sets labels, title, and legend for the plot.
9. If any exception occurs during this process, it closes the figure and returns `None`.

In essence, this function helps visualize the distribution of match scores, making it easier to identify patterns or outliers in the data.

**Imports:**
```
import os, import io, from datetime import datetime, from typing import List, Optional, Tuple, import tempfile, from fpdf import FPDF, from harmony.schemas.requests.text import Instrument, from harmony.schemas.responses.text import MatchResponse
```
