import pdfplumber
import pandas as pd

# Open the PDF file
with pdfplumber.open('k-receipt.pdf') as pdf:
    # Extract the first page
    first_page = pdf.pages[0]
    # Extract table(s) from the page
    table = first_page.extract_table()

# Convert to DataFrame
df = pd.DataFrame(table[1:], columns=table[0])

print(df)
