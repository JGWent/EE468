from django import forms
from datetime import datetime
import mysql.connector


def years():
    now = datetime.now()
    year_list = (('default', 'Select One'),)
    for i in range(now.year - 10, now.year + 2):
        year_list = year_list + ((i, i),)
    return tuple(year_list)


def departments():
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root",
        passwd='Cakeman345', #"mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )
    cursor = mydb.cursor()
    cursor.execute('select dept_name from department')
    depts = (('default', 'Select One'),)
    res = cursor.fetchall()
    for i in res:
        depts = depts + ((i[0], i[0]),)
    mydb.close()
    return depts


class StudentForm(forms.Form):
    semester = forms.ChoiceField(choices=(('default', 'Select One'), ('1', 'Spring'), ('2', 'Fall')))
    year = forms.ChoiceField(choices=years())
    department = forms.ChoiceField(choices=departments())
