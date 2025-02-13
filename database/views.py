from django.shortcuts import render
from django.db import connection

def index(request) :
    with connection.cursor() as cursor :
            cursor.execute("SELECT * FROM test_tb")
            response = cursor.fetchall()
    if request.method == "POST" :
        name = request.POST.get("name")
        pn = request.POST.get("pn")
        with connection.cursor() as cursor :
            cursor.execute("INSERT INTO test_tb (name, phone) VALUES(%s, %s)", (name, pn))
            connection.commit()
    return render(request, "index.html", {"response" : response})