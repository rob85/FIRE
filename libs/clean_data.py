#various libraries
import gspread
from datetime import *
from oauth2client.service_account import ServiceAccountCredentials




class CleanData:
    def __init__(
            self
    ):
        self.rows = None
        self.all_dates = ()

    def __creds(self):
        return {
         }

    def login(self):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(self.__creds(), scope)
        gs = gspread.authorize(creds)
        sheet = gs.open_by_url(
            'https://docs.google.com/spreadsheets/d/1QUCKVDlDFdJO_F4woYjcQ47cBJzVQf4gjPnQeOTq9mc/edit#gid=0'
        )
        worksheet = sheet.get_worksheet(0)
        rows = worksheet.get_all_records()

        temp_all_dates = []
        for i in rows:
            if i['first_of_month'] not in temp_all_dates:
                temp_date = datetime.strptime(i['first_of_month'], '%Y-%M-%d')
                temp_all_dates.append(temp_date)

        self.all_dates = temp_all_dates
        self.rows = rows

    def create_missing_data(
            self,
            company,
            type
    ):

        missing_data = []

        # Start to extracting the data.
        for i in self.rows:
            temp_list = (
                datetime.strptime(i['first_of_month'], '%Y-%M-%d'),
                i['company'],
                i['type'],
                i['begin_balance'],
                i['end_balance'],
                i['contributions'],
                i['asset']
            )
            # company and type we are going to update
            if i['first_of_month'] not in missing_data\
                    and i['company'].lower() == company.lower()\
                    and i['type'].lower() == type.lower():
                missing_data.append(temp_list)


        print(missing_data)

        # checking for any missing data
        missing_dates = []
        for m in missing_data:
            if m[0] not in self.all_dates:
                missing_dates.append(m[0])

        print(1)

