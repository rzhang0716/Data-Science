import PyPDF2

# Open the pdf file and read the binary file "rb"
with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    # Rotate the pdf
    page.rotate(180)
    page.rotateConterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)


# Combine pdf aka pdf merger
import sys

inputs = sys.argv[1:] # create a pdf list of grab all inputs except the first one


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')


# Watermarker
template = PyPDF2.PdfFileReader(open("super.pdf", "rb"))
watermark = PyPDF2.PdfFileReader(open("wtr.pdf", "rf"))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open("watermarked_output.pdf") as file:
        output.write(file)
