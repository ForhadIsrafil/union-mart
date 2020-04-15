import gspread
from oauth2client.service_account import ServiceAccountCredentials


# =================== send data to spreadsheet start ==================
def send_to_spreadsheet(product_ins):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('order_data_list.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("order_data_list").sheet1

    '''
    product_ins.name,
    product_ins.description,
    product_ins.price,
    product_ins.stock,
    product_ins.category,
    product_ins.sub_category,
    product_ins.offer,
    product_ins.delevery_charge,
    product_ins.free_delivery,
    product_ins.upload_date,
    product_ins.trend_name,
    '''
    row = [product_ins.name,
           product_ins.description,
           product_ins.price,
           product_ins.stock,
           product_ins.category,
           product_ins.sub_category,
           product_ins.offer,
           product_ins.delevery_charge,
           product_ins.free_delivery,
           str(product_ins.upload_date),
           product_ins.trend_name, ]
    index = 2
    sheet.insert_row(row, index)
    return True
    # =================== send data to spreadsheet end ==================
