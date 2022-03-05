from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Article
from .form import ArticleForm
# Create your views here.
# create a form to handle the title and content

@login_required
#before model form
def article_create_view(request):
    # initialize the form here
    form = ArticleForm(request.POST or None)
    # print(dir(form))
    context={
        "form": form
    }
    if form.is_valid():
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")
        article_obj = Article.objects.create(title=title,content=content)
        context["object"] = article_obj
        context["created"] = True
    return render(request,"articles/create.html",context= context)

# after model form
# def article_create_view(request):
#     # initialize the form here
#     form = ArticleForm(request.POST or None)
#     # print(dir(form))
#     context={
#         "form": form
#     }
#     if form.is_valid():
#         article_object = form.save
#         context["object"] = article_object
#         context["created"] = True
#     return render(request,"articles/create.html",context= context)




















# with form initial
# @login_required
# def article_create_view(request):
#     # initialize the form here
#     form = ArticleForm()
#     # print(dir(form))
#     context={
#         "form": form
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST) # this form is set for get cleaned value
#         context["form"] = form ## again set the form after cleaned method
#         if form.is_valid():
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get("content")
#             article_obj = Article.objects.create(title=title,content=content)
#             context["object"] = article_obj
#             context["created"] = True
#     return render(request,"articles/create.html",context= context)






#without form
# @login_required
# def article_create_view(request):
#     context={

#     }
#     if request.method == "POST":
#         title = request.POST.get("title")
#         content = request.POST.get("content")
#         article_obj = Article.objects.create(title=title,content=content)
#         context["object"] = article_obj
#         context["created"] = True
#         print(context)
#     return render(request,"articles/create.html",context= context)



def article_search_view(request):
    # print(request.GET)
    query_dic = request.GET # is a dictionary
    # query = query_dic.get("q")

    try:
        query = int(query_dic.get("q"))
    except:
        query = None

    article_obj =None
    if query is not None:
        article_obj= Article.objects.get(id=query)
    context = {
        "objects": article_obj
    }
    return render(request,"articles/search.html",context)

def article_details_view(request,id=None):
    article_obj = None
    if id is not None:
        article_obj= Article.objects.get(id=id)
    context = {
        "objects": article_obj
    }
    return render(request,"articles/detail.html",context)