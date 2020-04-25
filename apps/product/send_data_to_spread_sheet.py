from datetime import date
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# =================== send data to spreadsheet start ==================
def send_to_spreadsheet(order_payment):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('order_data_list.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("order_data_list").sheet1

    '''
    order_payment.user,
    order_payment.invoice_no,
    order_payment.product_list,
    order_payment.delivery_location,
    order_payment.contact_number,
    order_payment.payment_number,
    order_payment.delivery_charge,
    order_payment.total,
    order_payment.order_date,
    order_payment.city,
    order_payment.payment_gateway,
    order_payment.is_delivered,
    '''
    user = 'User ID: ' + str(order_payment.user.id) + ' user_name: ' + str(order_payment.user.user_name)
    row = [user,
           order_payment.invoice_no,
           order_payment.product_list,
           order_payment.delivery_location,
           order_payment.contact_number,
           order_payment.payment_number,
           order_payment.delivery_charge,
           order_payment.total,
           str(date.strftime(order_payment.order_date, '%d-%m-%Y')),
           order_payment.city,
           order_payment.payment_gateway,
           order_payment.is_delivered, ]
    index = 2
    sheet.insert_row(row, index)
    return True
    # =================== send data to spreadsheet end ==================
