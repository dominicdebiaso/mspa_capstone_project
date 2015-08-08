import xlrd

def GetInput(input):
    workbook = xlrd.open_workbook(input)
    worksheet = workbook.sheet_by_name('MainDatafile')
    
    result = []
    num_rows = worksheet.nrows - 1
    curr_row = 0
    
    
    while curr_row < num_rows:
        curr_row += 1
        cell_value = worksheet.cell_value(curr_row, 16)
        result.append(cell_value)
    
    return result

