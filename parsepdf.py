import datetime
import os
import re

import xlwings as xw
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal


def from_pdf_to_txt(read_file):
    results = ''
    for page_layout in extract_pages(read_file):
        for element in page_layout:
            # print(element)
            if isinstance(element, LTTextBoxHorizontal):
                string = element.get_text()
                string = string.replace(":", '')
                string = string.replace("：", '')
                results = results + string.replace(' ', '')
    # print(results)
    return results


def re_text(bt, text):
    m1 = re.search(bt, text)
    if not m1 is None:
        reText = m1[0]
        return reText
    else:
        return ''


def save_excel(invoice_codes, invoice_nums, invoice_dates, invoice_valid_codes, invoice_tax_codes, invoice_totals):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(r"template.xlsx")

    ws = wb.sheets('Sheet1')
    ws.range('D3').options(transpose=True).value = invoice_codes
    ws.range('E3').options(transpose=True).value = invoice_nums
    ws.range('G3').options(transpose=True).value = invoice_dates
    ws.range('H3').options(transpose=True).value = invoice_valid_codes
    ws.range('I3').options(transpose=True).value = invoice_tax_codes
    ws.range('L3').options(transpose=True).value = invoice_totals
    wb.save("result" + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".xlsx")
    wb.close()
    app.quit()


def parse_pdf_2_excel():
    invoice_filenames = []
    invoice_codes = []
    invoice_nums = []
    invoice_dates = []
    invoice_valid_codes = []
    invoice_tax_codes = []
    invoice_totals = []

    receiptsCount = 0
    for root, subdirs, filenames in os.walk('.'):
        for filename in filenames:
            if filename.endswith('.pdf'):
                filepath = os.path.join(root, filename)
                receiptsCount += 1
                print(filepath + ' is extracting')
                pdftext = from_pdf_to_txt(filepath)

                if pdftext.find('滴滴') > -1:
                    invoice_codes.append(re_text('(?<=发票代码\n)\d+', pdftext))
                    invoice_nums.append(re_text('(?<=开票日期\n)\d+', pdftext))
                    invoice_dates.append(datetime.datetime.strptime(re_text('\d+年\d+月\d+日', pdftext), "%Y年%m月%d日"))
                    invoice_valid_codes.append(re_text('(?<=校验码\n)\d+', pdftext)[-6:])
                    invoice_tax_codes.append(re_text('(?<=纳税人识别号\n)\w+', pdftext))
                    invoice_totals.append(re_text('(?<=\（小写\）\n￥)\d+\.\d+', pdftext))

                if pdftext.find('成品油') > -1:
                    invoice_codes.append(re_text('(?<=发票代码\n)\d+', pdftext))
                    invoice_nums.append(re_text('(?<=发票号码\n)\d+', pdftext))
                    invoice_dates.append(datetime.datetime.strptime(re_text('(?<=开票日期\n年\n)\d+', pdftext), "%Y%m%d"))
                    invoice_valid_codes.append(re_text('(?<=校验码\n)\d+', pdftext)[-6:])
                    invoice_tax_codes.append(re_text('(?<=公司\n)\w+', pdftext))
                    invoice_totals.append(re_text('(?<=\(小写\)\n¥)\d+\.\d+', pdftext))

                invoice_filenames.append(filename)

                    # res = re.search('¥(?P<cost>\d+\.\d+)\n¥(?P<tax>\d+\.\d+)\n\(小写\)\n¥(?P<total>\d+\.\d+)', pdftext)
                    # if not res is None:
                    #     invoice_totals.append(res.groupdict()['total'])

    print(invoice_codes, invoice_nums, invoice_dates, invoice_valid_codes, invoice_tax_codes, invoice_totals)

    save_excel(invoice_codes, invoice_nums, invoice_dates, invoice_valid_codes, invoice_tax_codes, invoice_totals)

    return invoice_filenames, invoice_codes, invoice_nums, invoice_dates, invoice_valid_codes, invoice_tax_codes, invoice_totals
