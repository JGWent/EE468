from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import mysql.connector
from .forms import StudentForm


def get_name(request):

    template = loader.get_template('myapp/form.html')
    context ={ }

    return HttpResponse(template.render(context,request))

def Check(request):
    try:
        name = request.POST['your_name']
        if name =='admin':
            return HttpResponse(admin_page(request))
        elif name =='instructor':
            return HttpResponse(prof_page(request))
        elif name =='student':
            return HttpResponse(student(request))
        else:
            return HttpResponse('Please log in'+name)
    except:
        return HttpResponse('Please log in '+name)

def admin_page(request):
    template = loader.get_template('myapp/admin.html')
    context ={ }

    return HttpResponse(template.render(context,request))


def show(request):
    #name = request.POST['your_name']
    #print(name)
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root",
        passwd='Cakeman345', #"mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

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
    elif request.POST.get("4"):
        mycursor = mydb.cursor()

        mycursor.execute('select dept_name, min(salary), max(salary), avg(salary)from instructorgroup by dept_name')

        template = loader.get_template('myapp/table2.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("5"):
        mycursor = mydb.cursor()

        mycursor.execute('select instructor.name, ANY_VALUE(instructor.dept_name), count(instructor.ID) from instructor join takes,teaches where teaches.instr_id=instructor.ID and takes.course_id=teaches.course_id and takes.semester=teaches.semester and takes.semester=1 and takes.sec_id=teaches.sec_id group by instructor.name')

        template = loader.get_template('myapp/table3.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("6"):
        mycursor = mydb.cursor()

        mycursor.execute('select instructor.name, ANY_VALUE(instructor.dept_name), count(instructor.ID) from instructor join takes,teaches where teaches.instr_id=instructor.ID and takes.course_id=teaches.course_id and takes.semester=teaches.semester and takes.semester=2 and takes.sec_id=teaches.sec_id group by instructor.name')

        template = loader.get_template('myapp/table3.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("error: Hit back arrow of browser to return")

def prof_page(request):
    template = loader.get_template('myapp/professor.html')
    context ={ }

    return HttpResponse(template.render(context,request)) 

def semester(request):
    template = loader.get_template('myapp/semester.html')
    context ={ }

    return HttpResponse(template.render(context,request))
    
def semester2(request):
    template = loader.get_template('myapp/semester2.html')
    context ={ }

    return HttpResponse(template.render(context,request)) 

def results(request):
    #name = request.POST['your_name']
    #print(name)
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root",
        passwd='Cakeman345', #"mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

    if request.POST.get("1"):

        mycursor = mydb.cursor()

        mycursor.execute('select takes.course_id, ANY_VALUE(takes.sec_id), ANY_VALUE(takes.year), count(takes.course_id) as "# of students" from takes, teaches where takes.semester=1 and teaches.semester=1 and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year group by takes.course_id')

        template = loader.get_template('myapp/table4.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("2"):

        mycursor = mydb.cursor()

        mycursor.execute('select takes.course_id, ANY_VALUE(takes.sec_id), ANY_VALUE(takes.year), count(takes.course_id) as "# of students" from takes, teaches where takes.semester=2 and teaches.semester=2 and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year group by takes.course_id')

        template = loader.get_template('myapp/table4.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("3"):
        
        mycursor = mydb.cursor()

        mycursor.execute('select takes.course_id, ANY_VALUE(takes.sec_id), ANY_VALUE(takes.year), count(takes.course_id) as "# of students" from takes, teaches where takes.semester=3 and teaches.semester=3 and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year group by takes.course_id')

        template = loader.get_template('myapp/table4.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))  
    else:
        return HttpResponse("error")  

def results2(request):
    #name = request.POST['your_name']
    #print(name)
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root",
        passwd='Cakeman345', #"mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

    if request.POST.get("1"):

        mycursor = mydb.cursor()

        mycursor.execute('select name from takes, student, teaches where takes.semester=1 and teaches.semester=1 and takes.id=student.id and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year')

        template = loader.get_template('myapp/table5.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("2"):

        mycursor = mydb.cursor()

        mycursor.execute('select name from takes, student, teaches where takes.semester=2 and teaches.semester=2 and takes.id=student.id and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year')

        template = loader.get_template('myapp/table5.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))
    elif request.POST.get("3"):
        
        mycursor = mydb.cursor()

        mycursor.execute('select name from takes, student, teaches where takes.semester=3 and teaches.semester=3 and takes.id=student.id and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year')

        template = loader.get_template('myapp/table5.html')
        data = mycursor.fetchall()
        context = {
            'rows': data,
        }
        mycursor.close()

        return HttpResponse(template.render(context, request))  
    else:
        return HttpResponse("error")   

def student(request):
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root",
        passwd='Cakeman345', #"mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )
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