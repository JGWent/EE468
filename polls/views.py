from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import mysql.connector


def get_name(request):

    template = loader.get_template('myapp/form.html')
    context ={ }

    return HttpResponse(template.render(context,request))


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
    else:
        return HttpResponse("error")