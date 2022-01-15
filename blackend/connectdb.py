import pyodbc
import datetime

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-NB0KKTS;"
    "Database=hackathon;"
    "Trusted_Connection=yes;"
)

def selectName():
    temp = "select * from Tbl_Instructor"
    cursor = conn.cursor()
    data = cursor.execute(temp)
    data_temp = {}
    for i in data:
        disableDates = [0, 1, 2, 3, 4, 5, 6]
        temp_disableDates = i[3].split("|")
        for j in temp_disableDates:
            if j == "7":
                disableDates.remove(0)
            else:
                disableDates.remove(int(j))
        data_temp[i[0]]= {"InstructorCode":i[1], "FullName":i[2], "DisableDates":disableDates, "Period":i[4], "TimeStart":str(i[5]), "TimeEnd":str(i[6])}
    conn.commit()
    return data_temp

def selectTime(code, date):
    temp = "select * from Tbl_TransactionTimeSlot where InstrutorCode = '{}' and CreateDate = '{}'".format(code, date)
    cursor = conn.cursor()
    data = cursor.execute(temp)
    data_temp = {}
    for i in data:
        data_temp[i[0]]= {"InstructorCode":i[1], "CreateDate":i[2], "TimeStart":str(i[3]), "TimeEnd":str(i[4])}
    conn.commit()
    return data_temp

def save(code, date, time):
    start_time = datetime.time(int(time["HH"]),0,0)
    end_time = datetime.time(int(time["HH"])+1,0,0)
    temp = "insert into Tbl_TransactionTimeSlot (InstrutorCode, CreateDate, TimeStart, TimeEnd) values ('{}', '{}', '{}', '{}')".format(code, date, start_time, end_time)
    cursor = conn.cursor()
    cursor.execute(temp)
    cursor.commit()

    
print(selectTime("VD0001", "2021-01-16"))