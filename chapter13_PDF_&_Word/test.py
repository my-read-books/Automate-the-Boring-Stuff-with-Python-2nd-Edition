import PyPDF2

pdgFileObj = open("../automate_online-materials/meetingminutes.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdgFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())