from xlrd import open_workbook


def read_locators(sheet_name):
    wb=open_workbook("C:/Users/Megha R/PycharmProjects/DemoWebShop_FrameWork/DATA/demowebshop_locators.xls")
    ws=wb.sheet_by_name(sheet_name)
    used_rows=ws.nrows
    data={}
    for i in range (2,used_rows):
        rows=ws.row_values(i)
        data[rows[0]]=(rows[1],rows[2])
    return data

