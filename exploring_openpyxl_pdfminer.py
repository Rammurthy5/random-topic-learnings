'''
This helps you to read expenses from Bank account statements from your employer salary credits.
Author: RAMMURTY SUBRAHMANIYAN
Date: May 3, 2019
'''

# import PyPDF2 as p
import pdfminer as p
import os
import openpyxl

cwd = os.getcwd()
pdfs = list()
filepath = '../../Documents/Statements'
print(cwd)
os.chdir(filepath)

for i in os.listdir("."):
    if i.endswith(".pdf"):
        pdfs.append(i)
pdfs.sort()


import fitz
import re

A = "NEFT[\d\-\s]+ACCENTURE"
H = "NEFT\S+\W+HCL TECHNOLOGIES LIMITEDTAXE"
L = "CMS\/\s+SALARY"

exp = r"([\d{2,4}\/]+)[\s\-]+"
exp2 = r"\s\d\.\d+\s+(\d+\.\d+)"

hcl, lnt, acc = int(), int(), int()
hclTotal, lntTotal, accTotal = int(), int(), int()

with open("out.txt", "wb") as fw:
    for file in pdfs:
        page = fitz.open(file)
        try:
            for _ in page:
                hcl += len(_.searchFor("HCL"))
                acc += len(_.searchFor("ACCENTURE SALARY"))
                lnt += len(_.searchFor("CMS/ SALARY"))
                k = _.getText("text").replace("\n", " ")

                compiled = map(list, re.findall(exp+A+exp2, k))
                hclcompiler = map(list, re.findall(exp+H+exp2, k))
                lntcompiler = map(list, re.findall(exp+L+exp2, k))

                if compiled:
                    fw.write("\n ACCENTURE SOLUTIONS \n".encode("utf-8"))
                    accTotal += sum(list(map(lambda x: float(x[1]), compiled)))

                    fw.writelines(compiled)
                if hclcompiler:
                    fw.write("\n HCL TECH \n".encode("utf-8"))
                    hclTotal += sum(list(map(lambda x:float(x[1]), hclcompiler)))
                    fw.writelines(hclcompiler)
                    # print("HCL ", hclTotal)
                if lntcompiler:
                    fw.write("\n L & T \n".encode("utf-8"))
                    lntTotal += sum(list(map(lambda x:float(x[1]), lntcompiler)))
                    fw.writelines(lntcompiler)
                    # print("L&T ", lntTotal)

                # for line in _.getText("text").split("\n"):
                #    print(line)
                #    break
                #    if any([x in ["HCL", "ACCENTURE SALARY", "CMS/ SALARY"] for x in line]):
                #        print(line)

        finally:
            page.close()


print("Count of salaries: HCL {}, LNT {}, ACC {}".format(hcl, acc, lnt))
print("Total of salaries: HCL {}, LNT {}, ACC {}".format(hclTotal, lntTotal, accTotal))
print("Total Earnings of all salaries: ", hclTotal+lntTotal+accTotal)
