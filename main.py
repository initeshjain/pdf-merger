import PyPDF2
import os

def merge_pdfs(input_pdfs, output_pdf):
  pdf_merger = PyPDF2.PdfMerger()
    
  for pdf_file in input_pdfs:
    pdf_file = "./input/" + pdf_file 
    with open(pdf_file, 'rb') as pdf:
      pdf_merger.append(pdf)
    
  with open(output_pdf, 'wb') as output:
    pdf_merger.write(output)

if __name__ == "__main__":
  input_pdfs = os.listdir("./input")
  output_pdf = "./output/merged_output.pdf"
    
  merge_pdfs(input_pdfs, output_pdf)
  print("PDFs merged successfully!")
