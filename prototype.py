import PyPDF2
import re
import os

from PyPDF2 import PdfFileReader, PdfFileWriter


Main_data = {'user_1':[]}

for i in os.listdir('./Pdfs'):
    print(i)

    with open(fr'./Pdfs/{i}', 'rb') as f:
        # Create a PDF object
        reader = PyPDF2.PdfReader(f)

        # Try to decrypt the PDF with the password
        try:
            reader.decrypt('9820136548')
        except :
            # print('Incorrect password')
            # exit(1)
            pass

        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()

        
        ptr = r'[0-9]+/[0-9]+/[0-9]{4}|Cholesterol-Total[\*]*[\s]*[A-Za-z(,) ]*\n[\d.]+'

        all_matches = re.findall(ptr,text)
        all_matches = set(all_matches)
        all_matches = list(all_matches)
        all_matches.sort()
        print(all_matches)

        date_data = all_matches[0]
        key = re.findall(r'[A-Za-z- /]+',all_matches[1])
        Value = re.findall(r'[\d.]+',all_matches[1])
        print(date_data,key[0],Value[0])

        # Main_data['user_1'] = [{date_data:{key[0]:Value[0]}}]

        ls = {date_data:{key[0]:Value[0]}}

        Main_data['user_1'].append(ls)

print(Main_data)

date=[]
test_dict = []

for i in range(len(Main_data)):
    all_tests = Main_data['user_1'][i]
    print(all_tests)
    for dates,test in all_tests.items():
        print(dates,test)
        date.append(dates)
        test_dict.append(test)
print(date)
print(test_dict)
            
            
                



