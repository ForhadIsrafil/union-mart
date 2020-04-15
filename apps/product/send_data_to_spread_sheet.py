import gspread
from oauth2client.service_account import ServiceAccountCredentials


# =================== send data to spreadsheet start ==================
def send_to_spreadsheet(request):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('order_data_list.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("order_data").sheet1

    row = [str(request.POST['parent_name']), str(request.POST['child_name']), str(request.POST['phone_number']),
           str(request.POST['email']), str(request.POST.getlist('day'))]
    index = 2
    sheet.insert_row(row, index)
    return True
    # =================== send data to spreadsheet end ==================
