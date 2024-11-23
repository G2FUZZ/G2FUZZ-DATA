import os
from fpdf import FPDF
from PIL import Image
import pytesseract
from barcode import EAN13
from barcode.writer import ImageWriter
import matplotlib.pyplot as plt
import numpy as np

class EnhancedPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Comprehensive Report with Dynamic Content', 0, 1, 'C')
        else:
            self.set_font('Arial', 'I', 8)
            # Use the new attribute here
            self.cell(0, 10, f'Chapter {self._chapter_title} | Page {self.page_no()}', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()} | Enhanced Report', 0, 0, 'C')

    def chapter_title(self, num, label):
        # Store the chapter title in a different attribute
        self._chapter_title = label
        self.add_page()
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'Chapter {num} : {label}', 0, 1)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    # The rest of your methods remain unchanged
    def add_table(self, data):
        # Assuming data is a list of dicts
        self.add_page()
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Data Table', 0, 1)
        self.set_font('Arial', '', 10)
        col_width = self.w / 4.5
        self.ln(1)
        # Header
        for key in data[0].keys():
            self.cell(col_width, 10, key, border=1)
        self.ln()
        # Data rows
        for row in data:
            for key in row:
                self.cell(col_width, 10, str(row[key]), border=1)
            self.ln()

    def add_chart(self, data):
        # Assuming data is a dict with categories as keys and numbers as values
        categories = list(data.keys())
        values = list(data.values())
        fig, ax = plt.subplots()
        ax.bar(categories, values)
        chart_path = "./tmp/chart.png"
        plt.savefig(chart_path)
        plt.close()
        if os.path.exists(chart_path):
            self.add_page()
            self.image(chart_path, x = 10, y = None, w = 100)
            os.remove(chart_path)

# Example usage
pdf = EnhancedPDF()

# Add a chapter with text
chapter_title = "Introduction"
chapter_body = "This chapter introduces the concepts and the structure of the document."
pdf.chapter_title(1, chapter_title)
pdf.chapter_body(chapter_body)

# Add a chapter with a table
data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "Paris"},
    {"Name": "Charlie", "Age": 35, "City": "London"}
]
pdf.chapter_title(2, "Data Table Example")
pdf.add_table(data)

# Add a chapter with a chart
chart_data = {"Apples": 10, "Oranges": 15, "Bananas": 5, "Strawberries": 20}
pdf.chapter_title(3, "Chart Example")
pdf.add_chart(chart_data)

pdf_output_path = './tmp/comprehensive_report.pdf'
pdf.output(pdf_output_path)