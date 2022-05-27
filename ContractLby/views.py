# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth.models import User, auth
# from django.contrib import messages
# from django.shortcuts import render, redirect
# #
# #
# #
# # import os
# # import re
# # import docx
# # # import numpy
# # import PyPDF4
# # # import PyPDF2
# # import easygui
# # # import textract
# # import pandas as pd
# # from itertools import compress
# # from zipfile import ZipFile
# # import win32com.client
# #
# # # Create your views here.
# # # IMPORT PACKAGES
# # print("If `flg` not specified as 'lower', search algorithm will be case sensitive\n")
# # flg = "lower1"
# # FileCount = 0
# #
# # '''  TEST DIRECTORIES BELOW   '''
# # x = [os.path.join(r, file) for r, d, f in
# #      os.walk(r"C:\\Users\RNALAB\Concentrix Corporation\Contract Lists - Contract Library") for file in f]
# # ''' Obtain list of files '''
# # files = [f for f in os.listdir('.') if os.path.isfile(f)]
# # files = filter(lambda f: f.endswith(('.pdf', '.PDF')), x)
# #
# # '''   EXTRACTING ALL FILES IN DIRECTORY TO LISTS   '''
# # ypdf = [k for k in x if k.endswith('.pdf')]  # pdf Alone
# # yPDF = [k for k in x if k.endswith('.PDF')]  # PDF Alone
# # ydoc = [k for k in x if k.endswith('.doc')]  # doc Alone
# # yDOC = [k for k in x if k.endswith('.DOC')]  # DOC Alone
# # ymsg = [k for k in x if k.endswith('.msg')]  # msg Alone
# # yMSG = [k for k in x if k.endswith('.MSG')]  # MSG Alone
# # ydocx = [k for k in x if k.endswith('.docx')]  # docx Alone
# # yDOCX = [k for k in x if k.endswith('.DOCX')]  # DOCX Alone
# # y2 = ypdf + yPDF
# # yDo = yDOCX + ydocx
# # yDox = ydoc + yDOC
# # '''##################### DICTIONARY FILES #####################'''
# # Dictionary = pd.read_excel(r"C:\\Users\RNALAB\Concentrix Corporation\Keywords\Keyword File June 24_2021.xlsx",
# #                            sheet_name=0)
# # ################################
# # '''     INITIALIZATIONS     '''
# # dec = re.compile('\d+\.\d+')
# # dig = re.compile('\d+')
# # alphabets = "([A-Za-z])"
# # prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
# # suffixes = "(Inc|Ltd|Jr|Sr|Co)"
# # starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
# # acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
# # websites = "[.](com|net|org|io|gov)"
# #
# #
# # def split_into_sentences(text):
# #     text = " " + text + "  "
# #     R = dec.findall(text)
# #     S = [j[0] + '<decimal>' + j[1] for j in [dig.findall(i) for i in R]]
# #     for i in range(len(R)):
# #         text = text.replace(R[i], S[i])
# #     text = text.replace("\n", " ")
# #     text = text.replace("Œ", "<stop>")
# #     text = re.sub(prefixes, "\\1<prd>", text)
# #     text = re.sub(websites, "<prd>\\1", text)
# #     if "Ph.D" in text: text = text.replace("Ph.D.", "Ph<prd>D<prd>")
# #     text = re.sub("\s" + alphabets + "[.] ", " \\1<prd> ", text)
# #     text = re.sub(acronyms + " " + starters, "\\1<stop> \\2", text)
# #     text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
# #     text = re.sub(alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>", text)
# #     text = re.sub(" " + suffixes + "[.] " + starters, " \\1<stop> \\2", text)
# #     text = re.sub(" " + suffixes + "[.]", " \\1<prd>", text)
# #     text = re.sub(" " + alphabets + "[.]", " \\1<prd>", text)
# #     if "”" in text: text = text.replace(".”", "”.")
# #     if "\"" in text: text = text.replace(".\"", "\".")
# #     if "!" in text: text = text.replace("!\"", "\"!")
# #     if "?" in text: text = text.replace("?\"", "\"?")
# #     text = text.replace(".", ".<stop>")
# #     text = text.replace("?", "?<stop>")
# #     text = text.replace("!", "!<stop>")
# #     text = text.replace("<prd>", ".")
# #     sentences = text.split("<stop>")
# #     # sentences = sentences[:-1]
# #     sentences = [s.strip() for s in sentences]
# #     return sentences
# #
# #
# # def readtxt(filename):
# #     doc = docx.Document(filename)
# #     fullText = []
# #     for para in doc.paragraphs:
# #         fullText.append(para.text)
# #     return '\n'.join(fullText)
# #
# #
# # # _______________________________________________
# # #     WordSearch / PATTERN SEARCH FROM SENTENCES
# # def search(word, sentences):
# #     return [i for i in sentences if re.search(r'\b%s\b' % word, i)]
# #
# #
# # # _______________________________________________
# # #
# # # This function is taking Key and dataframe and returning all the rows and columns with matched Keywords
# # def xsearch(regex: str, df, case=False):
# #     """Search all the text columns of `df`, return rows with any matches."""
# #     textlikes = df.select_dtypes(include=[object, "string"])
# #     return df[
# #         textlikes.apply(
# #             lambda column: column.str.contains(regex, regex=True, case=case, na=False)
# #         ).any(axis=1)]
# #
# #
# # # _______________________________________________
# # # This function is searching the Key inside the filtered list
# # def indexHaveSubstring(lst, substring):
# #     ls = list()
# #     for i in range(len(lst)):
# #         subs = re.compile(Ke).search(str(lst[i]))
# #         if subs != None:
# #             ls.append(i)
# #     return ls
# #
# #
# # # _______________________________________________
# # #####     DATE SEARCH PATTERNS
# # import calendar
# #
# # dat = re.compile(
# #     r'(?:\d{1,2}(?:(?:-|/)|(?:th|st|nd|rd)?\s))?(?:(?:(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)(?:(?:-|/)|(?:,|\.)?\s)?)?(?:\d{1,2}(?:(?:-|/)|(?:th|st|nd|rd)?\s))?)(?:\d{2,4})')
# # dat = r'(?:\d{1,2}[-/th|st|nd|rd\s]*)?(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)|jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)[a-z\s,.]*(?:\d{1,2}[-/th|st|nd|rd)\s,]*)+(?:\d{3})+'
# # dat = r'(?:\d{1,2}[-/th|st|nd|rd\s]*|[-/-])?(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)|jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)|\d{1,2}?)[a-z\s,.]*(?:\d{1,2}[-/th|st|nd|rd)\s,]*)+(?:\d{3})+'
# # full_months = [month for month in calendar.month_name if month]
# # short_months = [d[:3] for d in full_months]
# # months = '|'.join(short_months + full_months)
# # sep = r'[.,]?\s+'  # seperators
# # day = r'\d+'
# # year = r'\d+'
# # day_or_year = r'\d+(?:\w+)?'
# # ################################
# # TEST = list()
# # # OldList = read_excel('RawData/RawData.xlsx')
# # OldList = ["a.pdf", "b.pdf",
# #            "c.pdf",
# #            "C:/Users/joshua.john/Concentrix Corporation/Account Management Operations (AMO) - Documents\Contracts for Legal Team\\0 CIS programs\\Catholic Financial Life\\Transaction Documents\\Work Orders\\WO017\\Catholic Financial Life-CNX US-CIS(Work Order 017)10-23-17exe.pdf"]
# # c0 = "character(0)"
# # OutPut = pd.DataFrame(columns=['Sentences', 'Keywords', 'TotalCount', 'FileName', 'ImagePDF', 'Word'])
# # y2 = ypdf + yPDF  # Combine PDF files later once all the list of pdfs in the library
# # # OpTion = int(input("Enter your inputs in numeric format for the below options:\n1, Keyword Search - Dictionary\n2, Paragraph search\n3, Padding search\n4, Single Keyword Search\n5, FMEA\n\n"))
# # ImagePDF = ""
# # a = ypdf + yPDF
# # DF = pd.DataFrame(
# #     columns=["FileName/DirName", "ImagePDF", "Word", "Theme/Topic", "Sentence", "SentenceNo", "TotalCount",
# #              "PageNo"])
# # FileTrack = pd.DataFrame(columns=["FileName", "Page", "Status", "CharCount"])
# # df1 = pd.DataFrame()
# # df2 = pd.DataFrame()
# # print(len(a))
# # #return y2
# # # %%
# # '''   CODE FOR SEARCHING   '''
# # import time
# #
# #
# #
# #     global DF
# #     start_time = time.time()
# #     CAP = len(y2) + 1
# #     zzz = 0
# #     y2 = ypdf + yPDF
# #
# #     # Word will change, for each word see for all combinations and apply conditions for multiple words
# #     # _____________________________________________________________________________
# #
# #     # '''   SINGLE KEYWORD SEARCH   '''
# #     # if (OpTion==4):
# #     print("*** Keyword Search - Single Keyword***")
# #     KW = input("Enter the keyword :\n\n")
# #     flg = "lower"
# #     fl = input(
# #         "Do you want to change the case of the keyword?\n\nRespond with '1' if you want to lower case the keyword\nRespond with '0' if you dont want to change\n\n")
# #     if fl == 0:
# #         flg = "Upper"
# #     ###     First n files
# #     # for i in range(0,((len(ypdf))-CAP)):
# #     # print(i)
# #     g = a[zzz:CAP]
# #     y2 = y2[zzz:CAP]
# #     ImagePDF = ""
# #     if not (g in OldList):
# #         for p in y2[zzz:CAP]:
# #             plen = 0
# #             if p != "C:/Users/joshua.john/Concentrix Corporation/Account Management Operations (AMO) - Documents\\Contracts for Legal Team\\0 CIS programs\\Catholic Financial Life\\Transaction Documents\\Work Orders\\WO017\\Catholic Financial Life-CNX US-CIS(Work Order 017)10-23-17exe.pdf":
# #                 try:
# #                     FileCount = FileCount + 1
# #                     # print("\033[H\033[J")
# #                     print(FileCount)
# #                     # print('\n\n\n'+p+'\n')
# #                     try:
# #                         pdfFileObj = open(p, 'rb')
# #                         p1 = p
# #                     except:
# #                         df2 = pd.Series([p, "File", "Access Denied", plen],
# #                                         index=["FileName", "Page", "Status", "CharCount"])
# #                         FileTrack = FileTrack.append(df2, ignore_index=True)
# #                         print("File added as Access Denied")
# #                         pdfFileObj = open("C:/Users/joshua.john/Desktop/ROT Out/Blank/Blank.pdf", 'rb')
# #                         p1 = p + "BLANK FILE"
# #                         pdfReader = PyPDF4.PdfFileReader(pdfFileObj,
# #                                                          strict=False)  ###   STRICT + FALSE ADDED TO REMOVE THE ERROR CHECK FOR ACCURACY
# #                     #         ###   PASSWORD HANDLING
# #                     if not pdfReader.isEncrypted:
# #
# #                         #          if pdfReader.isEncrypted:
# #                         #              pdfReader.decrypt(passwordFile['password'])
# #                         #           print(pdfReader.numPages)
# #                         tXt = ""
# #                         PGtXt = ""
# #                         for PG in range(pdfReader.numPages):
# #                             PGNo = PG
# #                             pageObj = pdfReader.getPage(PG)
# #                             try:
# #                                 PGtXt = pageObj.extractText()
# #                             except:
# #                                 PGtXt = ""
# #                                 df2 = pd.Series([p1, PG, "Unreadable", plen],
# #                                                 index=["FileName", "Page", "Status", "CharCount"])
# #                                 FileTrack = FileTrack.append(df2, ignore_index=True)
# #                                 print("File added to exception list")
# #
# #                             PGtXt = PGtXt.replace(
# #                                 ' !"#$%&\'()*+,-./012-345627\n3,&"8%))9"#:;3<%&$9=%)35\'&%%>%#?\n3,:\'%\n3@3',
# #                                 '').replace('!%3', '').replace('!&3', '').replace('!$3', '').replace('!#3', '').replace(
# #                                 '!"3', '').replace('!!3', '').replace('!*3', '').replace('!$3',
# #                                                                                          '').replace('!*3', '').replace(
# #                                 '!3', '').replace('#3', '').replace('$3', '').replace('%3', '').replace("'3",
# #                                                                                                         '').replace(
# #                                 '(3', '').replace(')3', '').replace('&3', '')
# #                             tXt = tXt + '\n-\r-\n' + PGtXt
# #                             q = KW
# #                             PGtXt = PGtXt.strip('\n')
# #                             PGtXt = PGtXt.replace('\n', '')
# #                             PGtXt = PGtXt.strip('\t')
# #                             PGtXt = PGtXt.replace('\t', ' ')
# #                             PGtXt = re.sub("\s+", ' ', PGtXt)
# #                             plen = plen + len(PGtXt)
# #                             PGt = split_into_sentences(PGtXt)
# #                             if (flg == "lower"):
# #                                 patt = q.lower()
# #                                 PGt = [x.lower() for x in PGt]
# #                             else:
# #                                 patt = q
# #                             word = patt
# #                             # print(q) #                    Test
# #                             if '+DATE' in q:
# #                                 word = q.replace('+DATE', '')
# #                                 word = word.lower()
# #                                 PG1 = [[(word in x), PGt.index(x)] for x in PGt]
# #                                 PG2 = list(compress(PGt, [item[0] for item in PG1]))
# #                                 PG3 = [item[1] for item in PG1 if item[0] == True]
# #                                 PP1 = [[bool(re.search(dat, x)), PG2.index(x)] for x in PG2]
# #                                 PP2 = list(compress(PP1, [item[0] for item in PP1]))
# #                                 PP3 = [item[1] for item in PP1 if item[0] == True]
# #                                 PP4 = [PG2[item] for item in PP3]
# #                             elif '+' in patt:
# #                                 word = word.split(sep='+')
# #                                 dat = word[1]
# #                                 PG1 = [[(word[0] in x), PGt.index(x)] for x in PGt]
# #                                 PG2 = list(compress(PGt, [item[0] for item in PG1]))
# #                                 PG3 = [item[1] for item in PG1 if item[0] == True]
# #                                 PP1 = [[bool(dat in x), PG2.index(x)] for x in PG2]
# #                                 PP2 = list(compress(PP1, [item[0] for item in PP1]))
# #                                 PP3 = [item[1] for item in PP1 if item[0] == True]
# #                                 PP4 = [PG2[item] for item in PP3]
# #                             else:
# #                                 PG1 = [
# #                                     [((' ' + word + ' ' in x) or (word + ' ' in x) or (word + '.' in x)), PGt.index(x)]
# #                                     for x in PGt]
# #                                 PG2 = list(compress(PGt, [item[0] for item in PG1]))
# #                                 PG3 = [item[1] for item in PG1 if item[0] == True]
# #                                 PP3 = PG3
# #                                 PP4 = PG2
# #                                 # print(word)
# #                             if len(PP4) != 0 and str(KW) != 'nan':
# #                                 df = pd.DataFrame(list(zip(PP4, PP3)), columns=["Sentence", "SentenceNo"])
# #                                 if (".pdf" in p and len(tXt) < 150):
# #                                     ImagePDF = "Image PDF"
# #                                 else:
# #                                     ImagePDF = 'Proper PDF File'
# #                                 df['FileName/DirName'] = p1
# #                                 df["ImagePDF"] = ImagePDF
# #                                 df["Word"] = q
# #                                 df["Theme/Topic"] = KW
# #                                 df["TotalCount"] = 0
# #                                 df["PageNo"] = PG + 1
# #                                 print(q)
# #                                 df1 = df1.append(df)
# #                                 df1 = df1.reset_index();
# #                                 del (df1['index'])
# #
# #                         DF = DF.append(df1)
# #                         df1 = pd.DataFrame()
# #                         df2 = pd.Series([p1, "File", "Read", plen], index=["FileName", "Page", "Status", "CharCount"])
# #                         FileTrack = FileTrack.append(df2, ignore_index=True)
# #                     else:
# #                         df2 = pd.Series([p1, "File", "Encrypted", plen],
# #                                         index=["FileName", "Page", "Status", "CharCount"])
# #                         FileTrack = FileTrack.append(df2, ignore_index=True)
# #                         print("File added as Encrypted file")
# #                 except:
# #                     PGtXt = ""
# #                     df2 = pd.Series([p1, PG + 1, "ReadError", plen], index=["FileName", "Page", "Status", "CharCount"])
# #                     FileTrack = FileTrack.append(df2, ignore_index=True)
# #                     print("File added to exception list")
# #                     pdfFileObj.close()
# #     ###################################################################
# #     #     DOCX FILES
# #     for p in yDo:
# #         try:
# #             DoTxt = readtxt(p)
# #             p1 = p
# #         except:
# #             df2 = pd.Series([p, "File", "Cant' be read", "-"], index=["FileName", "Page", "Status", "CharCount"])
# #             FileTrack = FileTrack.append(df2, ignore_index=True)
# #             print("File can't be read")
# #             DoTxt = ""
# #             p1 = p + "BLANK FILE ADDED"
# #         PGtXt = DoTxt
# #         PGtXt = PGtXt.replace(' !"#$%&\'()*+,-./012-345627\n3,&"8%))9"#:;3<%&$9=%)35\'&%%>%#?\n3,:\'%\n3@3',
# #                               '').replace('!%3', '').replace('!&3', '').replace('!$3', '').replace('!#3', '').replace(
# #             '!"3', '').replace('!!3', '').replace('!*3', '').replace('!$3', '').replace('!*3', '').replace('!3',
# #                                                                                                            '').replace(
# #             '#3', '').replace('$3', '').replace('%3', '').replace("'3", '').replace('(3', '').replace(')3', '').replace(
# #             '&3', '')
# #         tXt = tXt + '\n-\r-\n' + PGtXt
# #         q = KW
# #         PGtXt = PGtXt.strip('\n');
# #         PGtXt = PGtXt.replace('\n', '');
# #         PGtXt = PGtXt.strip('\t');
# #         PGtXt = PGtXt.replace('\t', ' ');
# #         PGtXt = re.sub("\s+", ' ', PGtXt)
# #         plen = plen + len(PGtXt)
# #         PGt = split_into_sentences(PGtXt)
# #         if flg == "lower":
# #             patt = q.lower()
# #             PGt = [x.lower() for x in PGt]
# #         else:
# #             patt = q
# #         word = patt
# #         # print(q) #                    Test
# #         if '+DATE' in q:
# #             word = q.replace('+DATE', '')
# #             word = word.lower()
# #             PG1 = [[(word in x), PGt.index(x)] for x in PGt]
# #             PG2 = list(compress(PGt, [item[0] for item in PG1]))
# #             PG3 = [item[1] for item in PG1 if item[0] == True]
# #             PP1 = [[bool(re.search(dat, x)), PG2.index(x)] for x in PG2]
# #             PP2 = list(compress(PP1, [item[0] for item in PP1]))
# #             PP3 = [item[1] for item in PP1 if item[0] == True]
# #             PP4 = [PG2[item] for item in PP3]
# #         elif '+' in patt:
# #             word = word.split(sep='+')
# #             dat = word[1]
# #             PG1 = [[(word[0] in x), PGt.index(x)] for x in PGt]
# #             PG2 = list(compress(PGt, [item[0] for item in PG1]))
# #             PG3 = [item[1] for item in PG1 if item[0] == True]
# #             PP1 = [[bool(dat in x), PG2.index(x)] for x in PG2]
# #             PP2 = list(compress(PP1, [item[0] for item in PP1]))
# #             PP3 = [item[1] for item in PP1 if item[0] == True]
# #             PP4 = [PG2[item] for item in PP3]
# #         else:
# #             PG1 = [[((' ' + word + ' ' in x) or (word + ' ' in x) or (word + '.' in x)), PGt.index(x)] for x in PGt]
# #             PG2 = list(compress(PGt, [item[0] for item in PG1]))
# #             PG3 = [item[1] for item in PG1 if item[0] == True]
# #             PP3 = PG3
# #             PP4 = PG2
# #             # print(word)
# #         if len(PP4) != 0 and str(KW) != 'nan':
# #             df = pd.DataFrame(list(zip(PP4, PP3)), columns=["Sentence", "SentenceNo"])
# #
# #             df['FileName/DirName'] = p1
# #             df["ImagePDF"] = 'DOCX'
# #             df["Word"] = q
# #             df["Theme/Topic"] = KW
# #             df["TotalCount"] = 0
# #             df["PageNo"] = PG + 1
# #             print(q)
# #             df1 = df1.append(df)
# #             df1 = df1.reset_index()
# #             del (df1['index'])
# #
# #     DF = DF.append(df1)
# #     df1 = pd.DataFrame()
# #     df2 = pd.Series([p1, "File", "Read", plen], index=["FileName", "Page", "Status", "CharCount"])
# #     FileTrack = FileTrack.append(df2, ignore_index=True)
# #     ##############################################################################
# #     print("--- %s minutes ---" % round((time.time() - start_time) / 60, 4))
# #     ##############################################################################
# #     ##############################################################################
# #     return (FileTrack)
#
#
# # -*- coding: utf-8 -*-
# """
# Created on Wed Aug 11 10:31:59 2021
#
# @author: RNALAB
# """
# import pandas as pd
# import os
# import re
# import docx
# # import numpy
# import PyPDF4
# # import PyPDF2
# import easygui
# # import textract
# import pandas as pd
# from itertools import compress
# from zipfile import ZipFile
# import win32com.client
# import time
#
# start_time = time.time()
#
# '''     INITIALIZATIONS     '''
# dec = re.compile('\d+\.\d+')
# dig = re.compile('\d+')
# alphabets = "([A-Za-z])"
# prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
# suffixes = "(Inc|Ltd|Jr|Sr|Co)"
# starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
# acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
# websites = "[.](com|net|org|io|gov)"
#
#
# def split_into_sentences(text):
#     text = " " + text + "  "
#     R = dec.findall(text)
#     S = [j[0] + '<decimal>' + j[1] for j in [dig.findall(i) for i in R]]
#     for i in range(len(R)):
#         text = text.replace(R[i], S[i])
#     text = text.replace("\n", " ")
#     text = text.replace("Œ", "<stop>")
#     text = re.sub(prefixes, "\\1<prd>", text)
#     text = re.sub(websites, "<prd>\\1", text)
#     if "Ph.D" in text: text = text.replace("Ph.D.", "Ph<prd>D<prd>")
#     text = re.sub("\s" + alphabets + "[.] ", " \\1<prd> ", text)
#     text = re.sub(acronyms + " " + starters, "\\1<stop> \\2", text)
#     text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
#     text = re.sub(alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>", text)
#     text = re.sub(" " + suffixes + "[.] " + starters, " \\1<stop> \\2", text)
#     text = re.sub(" " + suffixes + "[.]", " \\1<prd>", text)
#     text = re.sub(" " + alphabets + "[.]", " \\1<prd>", text)
#     if "”" in text: text = text.replace(".”", "”.")
#     if "\"" in text: text = text.replace(".\"", "\".")
#     if "!" in text: text = text.replace("!\"", "\"!")
#     if "?" in text: text = text.replace("?\"", "\"?")
#     text = text.replace(".", ".<stop>")
#     text = text.replace("?", "?<stop>")
#     text = text.replace("!", "!<stop>")
#     text = text.replace("<prd>", ".")
#     sentences = text.split("<stop>")
#     # sentences = sentences[:-1]
#     sentences = [s.strip() for s in sentences]
#     return sentences
#
#
# def readtxt(filename):
#     doc = docx.Document(filename)
#     fullText = []
#     for para in doc.paragraphs:
#         fullText.append(para.text)
#     return '\n'.join(fullText)
#
# # _______________________________________________
# #     WordSearch / PATTERN SEARCH FROM SENTENCES
# def search(word, sentences):
#     return [i for i in sentences if re.search(r'\b%s\b' % word, i)]
#
#
# # _______________________________________________
# #
# # This function is taking Key and dataframe and returning all the rows and columns with matched Keywords
# def xsearch(regex: str, df, case=False):
#     """Search all the text columns of `df`, return rows with any matches."""
#     textlikes = df.select_dtypes(include=[object, "string"])
#     return df[
#         textlikes.apply(
#             lambda column: column.str.contains(regex, regex=True, case=case, na=False)
#         ).any(axis=1)]
#
#
# # _______________________________________________
# # This function is searching the Key inside the filtered list
# def indexHaveSubstring(lst, substring):
#     ls = list()
#     for i in range(len(lst)):
#         subs = re.compile(Ke).search(str(lst[i]))
#         if subs != None:
#             ls.append(i)
#     return ls
#
#
# # _______________________________________________
# #####     DATE SEARCH PATTERNS
# import calendar
#
# dat = re.compile(
#     r'(?:\d{1,2}(?:(?:-|/)|(?:th|st|nd|rd)?\s))?(?:(?:(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)(?:(?:-|/)|(?:,|\.)?\s)?)?(?:\d{1,2}(?:(?:-|/)|(?:th|st|nd|rd)?\s))?)(?:\d{2,4})')
# dat = r'(?:\d{1,2}[-/th|st|nd|rd\s]*)?(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)|jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)[a-z\s,.]*(?:\d{1,2}[-/th|st|nd|rd)\s,]*)+(?:\d{3})+'
# dat = r'(?:\d{1,2}[-/th|st|nd|rd\s]*|[-/-])?(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)|jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)|\d{1,2}?)[a-z\s,.]*(?:\d{1,2}[-/th|st|nd|rd)\s,]*)+(?:\d{3})+'
# full_months = [month for month in calendar.month_name if month]
# short_months = [d[:3] for d in full_months]
# months = '|'.join(short_months + full_months)
# sep = r'[.,]?\s+'  # seperators
# day = r'\d+'
# year = r'\d+'
# day_or_year = r'\d+(?:\w+)?'
# # dat = re.compile(rf'(?:{day}{sep})?(?:{months}){sep}{day_or_year}(?:{sep}{year})?')
#
#
# def cl_files(request):
#     global df
#     KW = "solutions"  # input("Enter the keyword :\n\n")
#     flg = "lower"
#     DF = pd.DataFrame(
#         columns=["FileName/DirName", "ImagePDF", "Word", "Theme/Topic", "Sentence", "SentenceNo", "TotalCount", "PageNo"])
#     df1 = pd.DataFrame()
#     FileTrack = pd.DataFrame(columns=["FileName", "Page", "Status", "CharCount"])
#     p = "C:\\Users\RNALAB\Concentrix Corporation\Contract Lists - Contract Library\ARS-CNX US(CCA-SOW 1-CO 1)03-24-2021exe.pdf"
#     pdfFileObj = open(p, 'rb')
#     p1 = p
#     plen = 0
#     pdfReader = PyPDF4.PdfFileReader(pdfFileObj,
#                                      strict=False)  ###   STRICT + FALSE ADDED TO REMOVE THE ERROR CHECK FOR ACCURACY
#     tXt = "";
#     PGtXt = ""
#     for PG in range(pdfReader.numPages):
#         PGNo = PG
#         pageObj = pdfReader.getPage(PG)
#         PGtXt = pageObj.extractText()
#         PGtXt = PGtXt.replace(' !"#$%&\'()*+,-./012-345627\n3,&"8%))9"#:;3<%&$9=%)35\'&%%>%#?\n3,:\'%\n3@3',
#                           '').replace('!%3', '').replace('!&3', '').replace('!$3', '').replace('!#3', '').replace('!"3',
#                                                                                                                   '').replace(
#             '!!3', '').replace('!*3', '').replace('!$3',
#                                               '').replace('!*3', '').replace('!3', '').replace('#3', '').replace('$3',
#                                                                                                                  '').replace(
#             '%3', '').replace("'3", '').replace('(3', '').replace(')3', '').replace('&3', '')
#         tXt = tXt + '\n-\r-\n' + PGtXt
#         q = KW
#         PGtXt = PGtXt.strip('\n');
#         PGtXt = PGtXt.replace('\n', '');
#         PGtXt = PGtXt.strip('\t');
#         PGtXt = PGtXt.replace('\t', ' ');
#         PGtXt = re.sub("\s+", ' ', PGtXt)
#         plen = plen + len(PGtXt)
#         PGt = split_into_sentences(PGtXt)
#         if (flg == "lower"):
#             patt = q.lower()
#             PGt = [x.lower() for x in PGt]
#         else:
#             patt = q;
#         word = patt
#         # print(q) #                    Test
#         if '+DATE' in q:
#             word = q.replace('+DATE', '')
#             word = word.lower()
#             PG1 = [[(word in x), PGt.index(x)] for x in PGt]
#             PG2 = list(compress(PGt, [item[0] for item in PG1]))
#             PG3 = [item[1] for item in PG1 if item[0] == True]
#             PP1 = [[bool(re.search(dat, x)), PG2.index(x)] for x in PG2]
#             PP2 = list(compress(PP1, [item[0] for item in PP1]))
#             PP3 = [item[1] for item in PP1 if item[0] == True]
#             PP4 = [PG2[item] for item in PP3]
#         elif '+' in patt:
#             word = word.split(sep='+')
#             dat = word[1]
#             PG1 = [[(word[0] in x), PGt.index(x)] for x in PGt]
#             PG2 = list(compress(PGt, [item[0] for item in PG1]))
#             PG3 = [item[1] for item in PG1 if item[0] == True]
#             PP1 = [[bool(dat in x), PG2.index(x)] for x in PG2]
#             PP2 = list(compress(PP1, [item[0] for item in PP1]))
#             PP3 = [item[1] for item in PP1 if item[0] == True]
#             PP4 = [PG2[item] for item in PP3]
#         else:
#             PG1 = [[((' ' + word + ' ' in x) or (word + ' ' in x) or (word + '.' in x)), PGt.index(x)] for x in PGt]
#             PG2 = list(compress(PGt, [item[0] for item in PG1]))
#             PG3 = [item[1] for item in PG1 if item[0] == True]
#             PP3 = PG3
#             PP4 = PG2
#             # print(word)
#         if len(PP4) != 0 and str(KW) != 'nan':
#             df = pd.DataFrame(list(zip(PP4, PP3)), columns=["Sentence", "SentenceNo"])
#             if (".pdf" in p and len(tXt) < 150):
#                 ImagePDF = "Image PDF"
#             else:
#                 ImagePDF = 'Proper PDF File'
#
#             df['FileName/DirName'] = p1
#             df["ImagePDF"] = ImagePDF
#             df["Word"] = q
#             df["Theme/Topic"] = KW
#             df["TotalCount"] = 0
#             df["PageNo"] = PG + 1
#             print(q)
#             df1 = df1.append(df)
#             df1 = df1.reset_index();
#             del (df1['index'])
#     DF = DF.append(df1)
#     df1 = pd.DataFrame()
#     df2 = pd.Series([p1, "File", "Read", plen], index=["FileName", "Page", "Status", "CharCount"])
#     FileTrack = FileTrack.append(df2, ignore_index=True)
#     print(FileTrack)
#     # return render(request, 'CNXProtect_Utl/cl_files.html', print({'result': DF}))
#     #return render(request, 'CNXProtect_Utl/cl_files.html', {'DF': DF})
#     return render(request, 'CNXProtect_Utl/login_page.html', {'DF': DF})
#
#
#
#     #return render(request, 'CNXProtect_Utl/cl_files.html', request.POST[DF])
#     #return ()#print("--- %s minutes ---" % round((time.time() - start_time) / 60, 4))
#
