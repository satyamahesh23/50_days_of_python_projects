from pypdf import PdfReader,PdfWriter
reader=PdfReader("Dear Hiring Manager.pdf")
writer=PdfWriter()

writer.append(reader)
writer.encrypt("12345678")
with open("protected.pdf", "wb") as file:
    writer.write(file)