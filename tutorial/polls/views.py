from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
import mysql.connector

from .dbmanager import DbManager
from .forms import StudentForm



def get_name(request):
    request.session.setdefault('user', 0)
    request.session['user'] = 0
    template = loader.get_template('myapp/form.html')
    context = {}

    return HttpResponse(template.render(context, request))


def Check(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('your_name')
            password = request.POST.get('your_pass')
            if name == 'admin' and password == '1234':
                request.session['user'] = 1
                return redirect('/polls/admin_page', request)
            elif name == 'instructor' and password == 'abcd':
                request.session['user'] = 2
                return redirect('/polls/prof_page', request)
            elif name == 'student' and password == 'hello':
                request.session['user'] = 3
                return redirect('/polls/student', request)
            else:
                request.session['user'] = 0
                return HttpResponse('Please log in')
        else:
            request.session.flush()
            return redirect("/")


    except:
        request.session.flush()
        return redirect("/")


def admin_page(request):
    if request.session['user'] == 1:
        template = loader.get_template('myapp/admin.html')
        context = {}

        return HttpResponse(template.render(context, request))
    else:
        request.session.flush()
        return redirect("/")


def logout(request):
    request.session.flush()
    return redirect("/")


def show(request):
    if request.session['user'] == 1:
        # name = request.POST['your_name']
        # print(name)
        mydb = DbManager.instance()

        if request.POST.get("1"):

            mycursor = mydb.getConnection().cursor()

            mycursor.execute('select * from instructor order by name')

            template = loader.get_template('myapp/table.html')
            data = mycursor.fetchall()
            context = {
                'rows': data,
            }
            mycursor.close()

            return HttpResponse(template.render(context, request))
        elif request.POST.get("2"):

            mycursor = mydb.getConnection().cursor()

            mycursor.execute('select * from instructor order by dept_name')

            template = loader.get_template('myapp/table.html')
            data = mycursor.fetchall()
            context = {
                'rows': data,
            }
            mycursor.close()

            return HttpResponse(template.render(context, request))
        elif request.POST.get("3"):

            mycursor = mydb.getConnection().cursor()

            mycursor.execute('select * from instructor order by salary')

            template = loader.get_template('myapp/table.html')
            data = mycursor.fetchall()
            context = {
                'rows': data,
            }
            mycursor.close()

            return HttpResponse(template.render(context, request))
        elif request.POST.get("4"):
            mycursor = mydb.getConnection().cursor()

            mycursor.execute(
                'select dept_name, min(salary), max(salary), avg(salary)from instructorgroup by dept_name')

            template = loader.get_template('myapp/table2.html')
            data = mycursor.fetchall()
            context = {
                'rows': data,
            }
            mycursor.close()

            return HttpResponse(template.render(context, request))
        elif request.POST.get("5"):
            mycursor = mydb.getConnection().cursor()

            mycursor.execute(
                'select instructor.name, ANY_VALUE(instructor.dept_name), count(instructor.ID) from instructor join takes,teaches where teaches.instr_id=instructor.ID and takes.course_id=teaches.course_id and takes.semester=teaches.semester and takes.semester=1 and takes.sec_id=teaches.sec_id group by instructor.name')

            template = loader.get_template('myapp/table3.html')
            data = mycursor.fetchall()
            context = {
                'rows': data,
            }
            mycursor.close()

            return HttpResponse(template.render(context, request))
        elif request.POST.get("6"):
            mycursor = mydb.getConnection().cursor()

            mycursor.execute(
                'select instructor.name, ANY_VALUE(instructor.dept_name), count(instructor.ID) from instructor join takes,teaches where teaches.instr_id=instructor.ID and takes.course_id=teaches.course_id and takes.semester=teaches.semester and takes.semester=2 and takes.sec_id=teaches.sec_id group by instructor.name')

            template = loader.get_template('myapp/table3.html')
            data = mycursor.fetchall()
            context = {
                'rows': data,
            }
            mycursor.close()

            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse("error: Hit back arrow of browser to return")
    else:
        return HttpResponse("error: Hit back arrow of browser to return")


def prof_page(request):
    if request.session['user'] == 2:
        template = loader.get_template('myapp/professor.html')
        context = {}

        return HttpResponse(template.render(context, request))
    else:
        return redirect('/')


def semester(request):
    if request.session['user'] == 2:
        template = loader.get_template('myapp/semester.html')
        context = {}

        return HttpResponse(template.render(context, request))
    else:
        return redirect('/')


def semester2(request):
    if request.session['user'] == 2:
        template = loader.get_template('myapp/semester2.html')
        context = {}

        return HttpResponse(template.render(context, request))
    else:
        return redirect('/')


def results(request):
    if request.session['user'] == 2:
        # name = request.POST['your_name']
        # print(name)
        mydb = DbManager.instance()

        if request.POST.get("1"):

            mycursor = mydb.getConnection().cursor()

            mycursor.execute(
                'select takes.course_id, ANY_VALUE(takes.sec_id), ANY_VALUE(takes.year), count(takes.course_id) as "# of students" from takes, teaches where takes.semester=1 and teaches.semester=1 and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year group by takes.course_id')

            template = loader.get_template('myapp/table4.html')
            data = mycursor.fetchall()
            context = {
                'rows': data,
            }
            mycursor.close()

            return HttpResponse(template.render(context, request))
        elif request.POST.get("2"):

            mycursor = mydb.getConnection().cursor()

            mycursor.execute(
                'select takes.course_id, ANY_VALUE(takes.sec_id), ANY_VALUE(takes.year), count(takes.course_id) as "# of students" from takes, teaches where takes.semester=2 and teaches.semester=2 and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year group by takes.course_id')

            template = loader.get_template('myapp/table4.html')
            data = mycursor.fetchall()
            context = {
                'rows': data,
            }
            mycursor.close()

            return HttpResponse(template.render(context, request))
        elif request.POST.get("3"):

            mycursor = mydb.getConnection().cursor()

            mycursor.execute(
                'select takes.course_id, ANY_VALUE(takes.sec_id), ANY_VALUE(takes.year), count(takes.course_id) as "# of students" from takes, teaches where takes.semester=3 and teaches.semester=3 and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year group by takes.course_id')

            template = loader.get_template('myapp/table4.html')
            data = mycursor.fetchall()
            context = {
                'rows': data,
            }
            mycursor.close()

            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse("error")
    else:
        return redirect('/')


def results2(request):
    if request.session['user'] == 2:
        # name = request.POST['your_name']
        # print(name)
        mydb = DbManager.instance()

        if request.POST.get("1"):

            mycursor = mydb.getConnection().cursor()

            mycursor.execute(
                'select name from takes, student, teaches where takes.semester=1 and teaches.semester=1 and takes.id=student.id and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year')

            template = loader.get_template('myapp/table5.html')
            data = mycursor.fetchall()
            context = {
                'rows': data,
            }
            mycursor.close()

            return HttpResponse(template.render(context, request))
        elif request.POST.get("2"):

            mycursor = mydb.getConnection().cursor()

            mycursor.execute(
                'select name from takes, student, teaches where takes.semester=2 and teaches.semester=2 and takes.id=student.id and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year')

            template = loader.get_template('myapp/table5.html')
            data = mycursor.fetchall()
            context = {
                'rows': data,
            }
            mycursor.close()

            return HttpResponse(template.render(context, request))
        elif request.POST.get("3"):

            mycursor = mydb.getConnection().cursor()

            mycursor.execute(
                'select name from takes, student, teaches where takes.semester=3 and teaches.semester=3 and takes.id=student.id and takes.course_id=teaches.course_id and takes.sec_id=teaches.sec_id and takes.year=teaches.year')

            template = loader.get_template('myapp/table5.html')
            data = mycursor.fetchall()
            context = {
                'rows': data,
            }
            mycursor.close()

            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse("error")
    else:
        return redirect('/')


def student(request):
    if request.session['user'] == 3:
        mydb = DbManager.instance()
        form = StudentForm()
        results = [""]
        if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                semester = form.cleaned_data['semester']
                year = form.cleaned_data['year']
                department = form.cleaned_data['department']
                if semester == 'default' or year == 'default' or department == 'default':
                    results = "Please Select all Options"
                else:
                    cursor = mydb.getConnection().cursor()
                    query = "SELECT section.course_id, title, sec_id, building, room, capacity FROM section JOIN course on course.course_id=section.course_id WHERE (dept_name=\'" + department + "\') AND (year=\'" + year + "\') AND (semester=\'" + semester + "\');"
                    cursor.execute(query)
                    results = cursor.fetchall()

        context = {
            "form": form,
            "results": results
        }
        return render(request, "myapp/student.html", context)
    else:
        request.session.flush()
        return redirect("/")
