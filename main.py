import openpyxl

file = openpyxl.load_workbook("inventory.xlsx")
list = file["Sheet1"]

supplier = {}

for row in range(2,list.max_row+1) :
    supplier_name = list.cell(row,4).value
    inventory = list.cell(row,2).value
    price = list.cell(row,3).value
    # print(f"{supplier_name}:{inventory}")

    if supplier_name in supplier :
        supplier[supplier_name] = supplier[supplier_name]+1
    else :
        print("adding supplier")
        supplier[supplier_name] = 1

print(supplier)