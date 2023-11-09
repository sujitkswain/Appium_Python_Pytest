from pathlib import Path
import xlrd


def get_data(file_path, sheet_name):
    data_list = []
    wb = xlrd.open_workbook(str(Path(__file__).parent) + "\\" + file_path)
    sheet = wb[sheet_name]
    for i in range(1, sheet.nrows):
        data = {}
        for j in range(0, sheet.ncols):
            data[sheet.cell_value(0, j)] = sheet.cell_value(i, j)
        data_list.append(data)
    return data_list
