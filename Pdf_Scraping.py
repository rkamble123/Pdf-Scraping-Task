
import PyPDF2
import re

from PyPDF2 import PdfFileReader, PdfFileWriter


with open('./Pdfs/Report-220081000043045_Mr_VINODMEHTA_29Jul2022_073446 (1) (1).pdf', 'rb') as f:
    # Create a PDF object
    reader = PyPDF2.PdfFileReader(f)

    # Try to decrypt the PDF with the password
    try:
        reader.decrypt('9820136548')
    except PyPDF2.utils.PdfReadError:
        print('Incorrect password')
        exit(1)

    text = ''
    for page in range(reader.getNumPages()):
        text += reader.getPage(page).extractText()

print(text)

# text = text

print(text)
# text_data = text[0].replace('\n','#')
# text_data = text_data.replace(' ','')

print(text)
# ptr = r'\nReported On:\n[0-9/]+'
# date_matches = re.findall(ptr,text)
# print(date_matches)

# reported_date = re.findall(r'[\d/]+',date_matches[0])
# print(reported_date)



# ptr = r'[\nReported On:\n|\nCholesterol-Total\n|\nTriglycerides level\n|\nHDL Cholesterol\n|\nNon HDL Cholesterol\n|\nLDL Cholesterol\n|\nVLDL Cholesterol\n][0-9/]+'

ptr = r'\nReported On:\n[0-9/]+|\nCholesterol-Total[\s]*\n[0-9]+|\nTriglycerides level[\s]*\n[0-9/]+|\nHDL Cholesterol[\s]*\n[0-9/]+|\nNon HDL Cholesterol[\s]*\n[0-9/]+|\nLDL Cholesterol[\s]*\n[0-9/]+|\nVLDL Cholesterol[\s]*\n[0-9/]+'


all_matches = re.findall(ptr,text)
print(all_matches)



    # # print(text)

    # base_data = ' '.join(text)

    # print(base_data)

    # [\nA-Za-z -]+[\d ]+[\nmg/dL]
# ptr = r'[\nA-Za-z -/]+[\d.]+[\nmg/dL]'
    # ptr=r'([0-9]*[.])?'
    # ptr = r'[\d.]+'

# matches = re.findall(ptr,text)
# print(matches)


    # matches = '\n'.join(matches)
    # matches.split('\n')
    # print(matches)

    # mach1 = ''.join(matches)
    # mach1.replace(" ",'')
    # mach1.replace("\n",'')

    # print(mach1)

    # ptr = r'[\nA-Za-z -/]+[\d.]+'
    # matches = re.findall(ptr,mach1)
    # print(matches)

# matches_new = []
# for i in matches:
#     print(type(i))
    # j=i.replace('\n','')
    # j=i.replace('\n',' ')

    # print(j)
    # matches_new.append(j)

# matches_new = ''.join(matches_new)

# print(matches_new)



# for i in matches:
#     j=i.replace('\n','#')
#     print(j)
#     ptr = r'#[A-Za-z -]+#[\d]+.{1}[\d]'
#     main_data = re.findall(ptr,j)
#     print(main_data)





