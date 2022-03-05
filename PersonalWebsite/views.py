
import random
from django.shortcuts import render 
from articles.models import Article


def home_view(request):
    random_id = random.randint(1,4)
    article_object = Article.objects.get(id = random_id)
    article_list = Article.objects.all( )
    list = [100,200,300,400]
    list_str = ""
    for x in list:
        list_str += f"number is {x}\n"
    context = {
        "list_str": list_str,
        "my_list": article_list,
        "objects": article_object,
        # "title":article_object.title,
        "id":article_object.id
    }
    return render(request,"home_view.html",context)



# from django.http import HttpResponse
# from django.shortcuts import render

# HTML_STRING = """
# <h1>Hello world</h1>
# """


# def home_view(request):
#     # Django Templates
#     return HttpResponse(HTML_STRING)


