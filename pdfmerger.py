from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["asset/pdf1.pdf", "asset/pdf2.pdf"]:
    merger.append(pdf)

merger.write("asset/merged-pdf.pdf")
merger.close()