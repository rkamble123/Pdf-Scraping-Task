import PyPDF2
import re

from PyPDF2 import PdfFileReader, PdfFileWriter

# pdf Pattern 1 Data Extraction function

def sample_pattern1(text,test_list):

    # Sample Pattern

    # data_pattern1 = r'[\n]*Cholesterol[- ]*Total[\s]*\n[0-9.]+|[\n]*Triglycerides [A-Za-z]*[\s]*\n[0-9.]+|[\n]*HDL Cholesterol[\s]*\n[0-9.]+|[\n]*Non HDL Cholesterol[\s]*\n[0-9.]+|[\n]*LDL Cholesterol[\s]*\n[0-9.]+|[\n]*VLDL Cholesterol[\s]*\n[0-9.]+|[\n]*LDL/HDL RATIO[\s]*\n[0-9/]+|[\n]*CHOL/HDL RATIO[\s]*\n[0-9/]+'

    all_matches=[]

    for test_name in test_list:
        # print(test_key,test_values)
        # print(test_name)


        # Pattern For Data Extraction

        data_pattern = fr'\n{test_name}[\s]*[A-Za-z]*[\s]*\n[0-9.]+'

        # print('data pattern : ',data_pattern)
        

        # Matching Created Pattern

        match_result = re.findall(data_pattern,text)

        # print('match result : ',match_result)

        # Adding All Results in one list (all_matches)
        if match_result:
            for i in match_result:
                all_matches.append(i)


    # print(all_matches)

    for test_name in test_list:
        for match in all_matches:

            if test_name in match:

                # Assigning test name as Key if test name matched with matched data
                key = test_name

                # pattern for extracting value
                value = re.findall(r'[0-9.]+',match)
                if value:
                    value = [data.strip() for data in value if data]

                    # creating Key value pair of data(ignores record if key already present)
                    final_data[key]=value[0]

    print('\nSample_pattern 1 :\n')

    # Full Data in a dictionary Final_data
    print(final_data)
    print()




# pdf Pattern 2 Data Extraction function

def sample_pattern2(text,test_list):
    
    # sample Pattern

    # data_pattern2 = r'Cholesterol[- ]*Total[\*]*[\s]*[A-Za-z(,) ]*\n[\d.]+|Triglycerides[- ]*[\*]*[\s]*[A-Za-z(,) ]*\n[\d.]+'

    all_matches=[]

    for test_name in test_list:
        # print(test_key,test_values)
        # print(test_name)

        # Matching Pattern For Data Extraction

        data_pattern = fr'{test_name}[- ]*[\*]*[\s]*[A-Za-z(,) ]*\n[\d.]+'

        

        # print('data pattern : ',data_pattern)
        # Matching Created Pattern
        match_result = re.findall(data_pattern,text)
        # print('match result : ',match_result)

        # Adding All Results in one list (all_matches)
        if match_result:
            for i in match_result:
                all_matches.append(i)

    # print(all_matches)

    for test_name in test_list:
        
        for match in all_matches:
            if test_name in match:
                # Assigning test name as Key if test name matched with matched data
                key = test_name
                # pattern for extracting value
                value = re.findall(r'[0-9.]+',match)
                if value:
                    value = [data.strip() for data in value if data]
                    # creating Key value pair of data(ignores record if key already present)
                    final_data[key]=value[0]
    print('\nSample_pattern 2 :/n')
    # Full Data in a dictionary Final_data
    print(final_data)
    print()





# pdf Pattern 3 Data Extraction function

def sample_pattern3(text,test_list):
    
    #Sample Pattern 

    # data_pattern3 = r' [\d.]+[\s\*]*[A-Za-z/]*[\s]*LDL/HDL Ratio[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*TC/HDL Ratio[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*VLDL Cholesterol[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*S. Triglycerides[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*LDL Cholesterol[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*Total Cholesterol[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*HDL Cholesterol[A-Za-z]*|[\d.]+[\s\*]*[A-Za-z/]*[\s]*Non-HDL Cholesterol[A-Za-z]*'


    # Data Record To Catch

    # l = ['LDL/HDL Ratio','TC/HDL Ratio','VLDL Cholesterol','S. Triglycerides','LDL Cholesterol','Total Cholesterol','HDL Cholesterol','Non-HDL Cholesterol']

    all_matches=[]

    for test_name in test_list:
        # print(test_key,test_values)

        # print(test_name)

        # Matching Pattern For Data Extraction

        data_pattern = fr'[\d.]+[\s\*]*[A-Za-z/.]*[\s]*{test_name}[A-Za-z]*'

        

        # print('data pattern : ',data_pattern)
        # Matching Created Pattern
        match_result = re.findall(data_pattern,text)
        # print('match result : ',match_result)
        # Adding All Results in one list (all_matches)
        if match_result:
            for i in match_result:
                all_matches.append(i)

    # print(all_matches)

    for test_name in test_list:
        for match in all_matches:
            if test_name in match:
                # Assigning test name as Key if test name matched with matched data
                key = test_name
                # pattern for extracting value
                value = re.findall(r'[0-9.]+',match)
                if value:
                    value = [data.strip() for data in value if data]
                    # creating Key value pair of data(ignores record if key already present)
                    final_data[key]=value[0]
    print('\nSample_pattern 3 :\n')
    # Full Data in a dictionary Final_data
    print(final_data)
    print()



if __name__=="__main__":

    

    # ls1=['Report-220081000043045_Mr_VINODMEHTA_29Jul2022_073446 (1) (1)','Medibuddy','1322020088_DHFS1304 (1)']


    final_data = {}


    with open('./Pdfs/1322020088_DHFS1304 (1).pdf', 'rb') as f:
        # Create a PDF object
        reader = PyPDF2.PdfReader(f)

        # Try to decrypt the PDF with the password
        try:
            reader.decrypt('9820136548')
        except :
            # print('Incorrect password')
            # exit(1)
            pass
    # reader.getNumPages()
        # print(len(reader.pages))

        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()

    # print(text)

    ptr1 = r"Reference:\n[A-Za-z0-9: ,\n\.-]+|VID:\n[\d]+"
    ptr2 = r"ID[\s]*:[\s]*[\d]+\nName[\s]*:[\s]*[A-Za-z ]+\nDOB/Age[\s]*:[\s]*[\d]+[A-Za-z ]*\nGender[\s]*:[\s]*[A-Za-z ]+\n"
    ptr3 = r"Registration[\s]*Id[\s]*Referred[\s]*By[\s]*Patient[\s]*Name[\s]*Registration[\s]*Date[\s]*\nCollection[\s]*Date[\s]*\nReporting[\s*]Date[\s]*"

    pdf_patterns =[ptr1,ptr2,ptr3] 

    test_list = ['Cholesterol-Total','Triglycerides','Cholesterol Total','Total Cholesterol','Total-Cholesterol','HDL Cholesterol','Non HDL Cholesterol','Non-HDL Cholesterol','LDL Cholestero','VLDL Cholesterol','LDL/HDL RATIO','CHOL/HDL RATIO','LDL/HDL Ratio','TC/HDL Ratio',]

    for pattern in pdf_patterns:
        pattern_match = re.findall(pattern,text)
        if pattern_match:
            pattern_index = pdf_patterns.index(pattern)

            if pattern_index == 0:
                sample_pattern1(text,test_list)

            elif pattern_index == 1:
                sample_pattern2(text,test_list)

            elif pattern_index == 2:
                sample_pattern3(text,test_list)
            else:
                print('Pdf Pattern Does Not Match.')
        

        


