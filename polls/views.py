from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import mysql.connector
from .forms import StudentForm

mydb = mysql.connector.connect(
    host="localhost",
    user="djangouser",
    passwd='mypassword',  # "mypassword",
    auth_plugin='mysql_native_password',
    database="university",
)


def get_name(request):
    template = loader.get_template('myapp/form.html')
    context = {}

    return HttpResponse(template.render(context, request))


def admin_page(request):
    template = loader.get_template('myapp/admin.html')
    context = {}

    return HttpResponse(template.render(context, request))


def show(request):
    # name = request.POST['your_name']
    # print(name)

    if request.POST.get("1"):

        mycursor = mydb.cursor()

        mycursor.execute('select * from instructor order by name')

        template = loader.get_template('myapp/table.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("2"):

        mycursor = mydb.cursor()

        mycursor.execute('select * from instructor order by dept_name')

        template = loader.get_template('myapp/table.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("3"):

        mycursor = mydb.cursor()

        mycursor.execute('select * from instructor order by salary')

        template = loader.get_template('myapp/table.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("error")


def student(request):
    form = StudentForm()
    results = []
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            semester = form.cleaned_data['semester']
            year = form.cleaned_data['year']
            department = form.cleaned_data['department']
            if semester == 'default' or year == 'default' or department == 'default':
                results = "Please Select all Options"
            else:
                cursor = mydb.cursor()
                query = "SELECT section.course_id, title, sec_id, building, room, capacity FROM section JOIN course on course.course_id=section.course_id WHERE (dept_name=\'" + department + "\') AND (year=\'" + year + "\') AND (semester=\'" + semester + "\');"
                cursor.execute(query)
                results = cursor.fetchall()


    context = {
        "years": ['2019', '2018', '2020'],
        "test": "testing 1 2 3 ",
        "form": form,
        "results": results
    }
    return render(request, "myapp/student.html", context)
