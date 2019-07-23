from django.shortcuts import render
from django.http import HttpResponse



def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})


def restaurant_list(request):

    context = {
 "my_list": [
            {"restaurant_name":"al bike","food_type":"chicken",},
            {"restaurant_name":"pizaa hut","food_type":"vegtables pizaa",},
            {"restaurant_name":"MAC","food_type":"chicken burger",},
        ],
    }
    return render(request, 'list.html', context)

def restaurant_detail(request):

    context = {
        "myobject":{"restaurant_name":"al bike","food_type":"chicken"},
    }
    return render(request, 'detail.html', context)
