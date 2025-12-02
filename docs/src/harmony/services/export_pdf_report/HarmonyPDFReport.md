# HarmonyPDFReport (class)

**Code:**
```python
class HarmonyPDFReport(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        self.set_font("Arial", "B", 16)
        self.set_text_color(31, 81, 155) 
        self.cell(0, 12, sanitize("Harmony Harmonisation Report"), ln=True, align="C")
        self.set_text_color(0, 0, 0) 
        self.set_font("Arial", "", 10)
        self.cell(
            0, 8,
            sanitize(f"Generated on {datetime.now():%Y-%m-%d %H:%M:%S}"),
            ln=True, align="C"
        )
        self.ln(8)

    def footer(self):
        """Add page footer with page numbers."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
        self.set_text_color(0, 0, 0)
    
    def chapter_title(self, title: str, color: Tuple[int, int, int] = (31, 81, 155)):
        """Add a chapter title with colored background."""
        self.set_font("Arial", "B", 14)
        self.set_fill_color(*color)
        self.set_text_color(255, 255, 255)
        self.cell(0, 12, sanitize(title), ln=True, fill=True, align="L")
        self.set_text_color(0, 0, 0)
        self.ln(5)

    def add_image_from_matplotlib(self, fig, x=None, y=None, w=0, h=0):
        """Add matplotlib figure to PDF."""
        if not GRAPHICS_AVAILABLE:
            return
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
            fig.savefig(tmp_file.name, format="png", dpi=150, bbox_inches="tight")
            temp_filename = tmp_file.name

        try:
            # Add to PDF
            if x is None:
                x = self.get_x()
            if y is None:
                y = self.get_y()
                
            self.image(temp_filename, x, y, w, h)
        finally:
            # Clean up
            try:
                os.remove(temp_filename)
            except:
                pass
            plt.close(fig)

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

    def add_instruments_overview(self, instruments: List[Instrument], match_stats: dict):
        """Enhanced instruments overview with statistics."""
        self.chapter_title("Instruments Overview")
        
        # Table header
        self.set_font("Arial", "B", 10)
        self.set_fill_color(230, 230, 230)
        
        col_widths = [60, 30, 40, 60]
        headers = ["Instrument Name", "Questions", "Matches Found", "Avg Match Score"]
        
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, sanitize(header), border=1, fill=True)
        self.ln()
        
        # Table rows
        self.set_font("Arial", "", 9)
        self.set_fill_color(255, 255, 255)
        
        for inst in instruments:
            name = inst.instrument_name or "Unnamed Instrument"
            q_count = len(inst.questions) if inst.questions else 0
            
            # Get stats for this instrument
            inst_matches = match_stats.get('by_instrument', {}).get(name, {})
            matches_found = inst_matches.get('matches', 0)
            avg_score = inst_matches.get('avg_score', 0)
            
            # Truncate long names
            display_name = name[:22] + "..." if len(name) > 25 else name
            
            self.cell(col_widths[0], 8, sanitize(display_name), border=1)
            self.cell(col_widths[1], 8, sanitize(str(q_count)), border=1, align="C")
            self.cell(col_widths[2], 8, sanitize(str(matches_found)), border=1, align="C")
            self.cell(col_widths[3], 8, sanitize(f"{avg_score:.1f}%"), border=1, align="C")
            self.ln()
        
        self.ln(5)
```

**Explanation:**
**HarmonyPDFReport Class Explanation**

The `HarmonyPDFReport` class is a custom PDF report generator built on top of the `FPDF` library. It provides a set of methods to create a professional-looking report with various sections, including:

1. **Header**: Displays the report title, date, and time.
2. **Footer**: Shows the page numbers.
3. **Chapter Titles**: Adds colored background to chapter titles.
4. **Executive Summary**: Displays key metrics in boxes.
5. **Instruments Overview**: Presents a table with instrument statistics.
6. **Image Integration**: Allows adding matplotlib figures to the report.

The class is designed to be flexible and extensible, making it easy to add new sections or customize existing ones.

**Key Features**

* Customizable header and footer
* Colored chapter titles
* Executive summary with key metrics
* Instruments overview with statistics
* Image integration with matplotlib
* Flexible and extensible design

**Usage**

To use the `HarmonyPDFReport` class, create an instance and call the desired methods to generate the report. For example:
```python
report = HarmonyPDFReport()
report.add_executive_summary(stats={'total_questions': 100, 'harmonised_questions': 50, 'success_rate': 0.8, 'avg_match_score': 0.7})
report.add_instruments_overview(instruments=[{'instrument_name': 'Instrument 1', 'questions': ['q1', 'q2']}, {'instrument_name': 'Instrument 2', 'questions': ['q3', 'q4']}])
report.output('report.pdf')
```
This will generate a PDF report with the executive summary and instruments overview sections.

**Imports:**
```
import os, import io, from datetime import datetime, from typing import List, Optional, Tuple, import tempfile, from fpdf import FPDF, from harmony.schemas.requests.text import Instrument, from harmony.schemas.responses.text import MatchResponse
```
