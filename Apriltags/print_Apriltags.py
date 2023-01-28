import os
from math import ceil
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import Image, SimpleDocTemplate, Table, TableStyle

# Set the directory containing the Apriltag PNGs
apriltag_dir = "Apriltags_900x900"
# Set the output PDF file name
output_pdf = "apriltags.pdf"
# Get a list of all Apriltag PNGs in the directory
apriltags = [f for f in os.listdir(apriltag_dir) if f.endswith(".png")]
print("Found", len(apriltags), "Apriltag PNGs in", apriltag_dir)

# Create a new PDF document
doc = SimpleDocTemplate(output_pdf, pagesize=letter)

# Create a list to hold the Apriltag images
image_list = []
# Set the number of columns and rows for the grid
num_cols = 5
num_rows = ceil(len(apriltags) / num_cols)
# Set the desired image size
image_size = 16*mm
# Set the spacing size
spacing_size = 4*mm

# Create a table to hold the Apriltag images
table = Table(
    [[Image(os.path.join(apriltag_dir, apriltag), width=image_size, height=image_size) for apriltag in apriltags[i:i+num_cols]] for i in range(0, len(apriltags), num_cols)],
    colWidths=[image_size+spacing_size for _ in range(num_cols)],
    rowHeights=[image_size+spacing_size for _ in range(num_rows)],
)
# Add the table to the list of elements to be included in the PDF
image_list.append(table)

# Add spacing between the Apriltag images and make the grid invisible
table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0, colors.transparent),
                         ('SPACING', (0, 0), (-1, -1), spacing_size)]))

# Build the PDF
doc.build(image_list)
print("Apriltag PDF saved to", output_pdf)