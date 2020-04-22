from django import forms
from datetime import datetime
import mysql.connector
from polls.dbmanager import *


def years():
    now = datetime.now()
    year_list = (('default', 'Select One'),)
    for i in range(now.year - 10, now.year + 2):
        year_list = year_list + ((i, i),)
    return tuple(year_list)


def departments():
    mydb = DbManager.instance()
    cursor = mydb.getConnection().cursor()
    cursor.execute('select dept_name from department')
    depts = (('default', 'Select One'),)
    res = cursor.fetchall()
    for i in res:
        depts = depts + ((i[0], i[0]),)
    return depts


class StudentForm(forms.Form):
    semester = forms.ChoiceField(choices=(('default', 'Select One'), ('1', 'Spring'), ('2', 'Fall'), ('3', 'Summer')), required=False)
    year = forms.ChoiceField(choices=years(), required=False)
    department = forms.ChoiceField(choices=departments(), required=False)
