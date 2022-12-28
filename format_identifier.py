import PyPDF2
import re


from PyPDF2 import PdfFileReader, PdfFileWriter

ls=['Triglycerides',['Cholesterol Total','Total Cholesterol','Cholesterol-Total','Total-Cholesterol'],'HDL Cholesterol','Non-HDL Cholesterol','LDL Cholestero','VLDL Cholesterol','LDL/HDL Ratio','TC/HDL Ratio',]

ls1=['Report-220081000043045_Mr_VINODMEHTA_29Jul2022_073446 (1) (1)','Medibuddy','1322020088_DHFS1304 (1)']

ptr1 = r"Reference:\n[A-Za-z0-9: ,\n\.-]+|VID:\n[\d]+"
ptr2 = r"ID[\s]*:[\s]*[\d]+\nName[\s]*:[\s]*[A-Za-z ]+\nDOB/Age[\s]*:[\s]*[\d]+[A-Za-z ]*\nGender[\s]*:[\s]*[A-Za-z ]+\n"
ptr3 = r"Registration[\s]*Id[\s]*Referred[\s]*By[\s]*Patient[\s]*Name[\s]*Registration[\s]*Date[\s]*\nCollection[\s]*Date[\s]*\nReporting[\s*]Date[\s]*"

pdf_patterns =[ptr1,ptr2,ptr3] 

# data_pattern1 = fr'\n{ls[i]}[\s]*\n[0-9.]+|\n{ls[i][]}[\s]*\n[0-9.]+'

data_pattern1 = r'[\n]*Cholesterol[- ]*Total[\s]*\n[0-9.]+|[\n]*Triglycerides [A-Za-z]*[\s]*\n[0-9.]+|[\n]*HDL Cholesterol[\s]*\n[0-9.]+|[\n]*Non HDL Cholesterol[\s]*\n[0-9.]+|[\n]*LDL Cholesterol[\s]*\n[0-9.]+|[\n]*VLDL Cholesterol[\s]*\n[0-9.]+|[\n]*LDL/HDL RATIO[\s]*\n[0-9/]+|[\n]*CHOL/HDL RATIO[\s]*\n[0-9/]+'
data_pattern2 = r'Cholesterol[- ]*Total[\*]*[\s]*[A-Za-z(,) ]*\n[\d.]+|Triglycerides[- ]*[\*]*[\s]*[A-Za-z(,) ]*\n[\d.]+'
data_pattern3 = r' [\d.]+[\s\*]*[A-Za-z/]*[\s]*LDL/HDL Ratio[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*TC/HDL Ratio[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*VLDL Cholesterol[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*S. Triglycerides[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*LDL Cholesterol[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*Total Cholesterol[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*HDL Cholesterol[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*Non-HDL Cholesterol[A-Za-z]*'
data_patterns = [data_pattern1,data_pattern2,data_pattern3]

final_data = {}

with open('./Pdfs/Report-220081000043045_Mr_VINODMEHTA_29Jul2022_073446 (1) (1).pdf', 'rb') as f:
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


for pattern in pdf_patterns:
    all_matches = re.findall(pattern,text)
    if all_matches:
        pattern_index = pdf_patterns.index(pattern)

        all_matches = re.findall(data_patterns[pattern_index],text)
        for index,data in enumerate(all_matches):
            all_matches[index] = data.replace('SERUM','')
        for index,data in enumerate(all_matches):
            all_matches[index] = data.replace('mg/dl','')
        for index,data in enumerate(all_matches):
            all_matches[index] = data.replace('*','')

        all_matches = set(all_matches)
        all_matches = list(all_matches)
        all_matches.sort()
        print(all_matches)

        all_matches = [data.strip() for data in all_matches if data]

        all_matches = [data.replace('S. Triglycerides','Triglycerides') for data in all_matches if data]

        for data in all_matches:
            # key = re.findall(r'[A-Za-z/ ]+',data)
            key = re.findall(r'[A-Za-z/ -]+',data)
            key = [data.strip() for data in key if data]

            print('key is : ',key[0])  
            value = re.findall(r'[0-9.]+',data)
            value = [data.strip() for data in value if data]

            print('value is : ',value[0])
            final_data[key[0]]=value[0]
            
print(final_data)
    
    # all_matches = set(all_matches)
    # all_matches = list(all_matches)
    # all_matches.sort()
    # print(all_matches)





# all_matches = re.findall(ptr,text)
# print(all_matches)


# all_matches = re.findall(ptr,text)
# print(all_matches)
# all_matches = set(all_matches)
# all_matches = list(all_matches)
# all_matches.sort()
# print(all_matches)


'''
ID[\s]*:[\s]*[\d]+\n
Name[\s]*:[\s]*[A-Za-z ]+\n
DOB/Age[\s]*:[\s]*[\d]+\n
Gender[\s]*:[\s]*[A-Za-z ]+\n
Collection     : 04/06/2022, 04:03 PM
Received      : 04/06/2022, 07:04 PM
Reported      : 04/06/2022, 10:25 PM
Ref. Doctor   : SELF
Passport No. : -
Client Name     : PHASORZ
TECHNOLOGIES PRIVATE
LIMITED - LB2024
Client Address : MUMBAI
4222060356
'''

ptr = r"Registration[\s]*Id[\s]\nReferred[\s]*By[\s]*Patient[\s]*Name[\s]*"

'''
Registration Id
Referred By        Patient Name       Registration Date
Collection Date
Reporting Date
Age /Sex:

'''

'''
Referred By        Patient Name       Registration Date
Collection Date
Reporting Date
Age /Sex:
'''