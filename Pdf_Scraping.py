
import PyPDF2
import re

from PyPDF2 import PdfFileReader, PdfFileWriter




with open('./Pdfs/1322020088_DHFS1304 (1).pdf', 'rb') as f:
    # Create a PDF object
    reader = PyPDF2.PdfReader(f)

    # Try to decrypt the PDF with the password
    try:
        reader.decrypt('9820136548')
    except:
        # print('Incorrect password')
        # exit(1)
        pass

    text = ''
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()

print(text)

# text = text

print(text)
# text_data = text[0].replace('\n','#')
# text_data = text_data.replace(' ','')

print(text)
ptr = r' [\d.]+[\s\*]*[A-Za-z/]*[\s]*LDL/HDL Ratio[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*TC/HDL Ratio[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*VLDL Cholesterol[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*S. Triglycerides[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*LDL Cholesterol[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*Total Cholesterol[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*HDL Cholesterol[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*Non-HDL Cholesterol[A-Za-z]*'
date_matches = re.findall(ptr,text)
print(date_matches)

# reported_date = re.findall(r'[\d/]+',date_matches[0])
# print(reported_date)

['Triglycerides','Total Cholesterol','HDL Cholesterol','Non-HDL Cholesterol','LDL Cholestero','VLDL Cholesterol','LDL/HDL Ratio','TC/HDL Ratio']

'''
LIPID PROFILE
LIPID PROFILE
mg/dl Upto 150    203.08* S. TriglyceridesSERUM
 mg/dl 0 - 200    257.75* Total CholesterolSERUM
43.88 mg/dl 40 - 60 HDL CholesterolSERUM
mg/dl upto 130    213.87* Non-HDL CholesterolSERUM
mg/dl Upto 100    173.25* LDL CholesterolSERUM
mg/dl 7 - 35    40.6* VLDL CholesterolSERUM
0 - 3.50    3.95* LDL/HDL RatioSERUM
3.0 - 5.0    5.87* TC/HDL RatioSERUM
'''



# ptr = r'[\nReported On:\n|\nCholesterol-Total\n|\nTriglycerides level\n|\nHDL Cholesterol\n|\nNon HDL Cholesterol\n|\nLDL Cholesterol\n|\nVLDL Cholesterol\n][0-9/]+'

# ptr = r'Cholesterol[- ]*Total[\*]*[\s]*[A-Za-z(,) ]*\n[\d.]+|Triglycerides[- ]*[\*]*[\s]*[A-Za-z(,) ]*\n[\d.]+|'


# all_matches = re.findall(ptr,text)
# print(all_matches)



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





