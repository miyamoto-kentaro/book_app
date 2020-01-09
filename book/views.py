from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator

from .forms import SearchForm
from .forms import CreateBookForm
from .forms import CreatePageForm
from .forms import CreatePage_contentForm

from .models import Book
from .models import Page
from .models import Page_content
from taggit.models import Tag

from django.db.models import Q

#ホームのview
def index(request, n=1):
    tags = Tag.objects.all().order_by('name')
    page = Paginator(tags, 10)
    params = {
            'data':page.get_page(n),
            'form':SearchForm(),
        }
    return render(request, 'book/index.html', params)

#検索処理
def search(request, n=1):
    if (request.method == 'POST'):
        str = request.POST['search']
        tag = Tag.objects.filter(name__contains=str)
        data = Book.objects.filter(Q(tags__in=tag) | Q(title__contains=str))\
            .order_by('title').distinct()
        page = Paginator(data, 10)
    params = {
            'word':str,
            'form':SearchForm(request.POST),
            'data':page.get_page(n),
        }
    return render(request, 'book/search_result.html', params)

def search_next(request, str, n=1):
    data = Book.objects.filter(title__contains=str).order_by('title')
    page = Paginator(data, 10)
    params = {
            'word':str,
            'form':SearchForm(),
            'data':page.get_page(n),
        }
    return render(request, 'book/search_result.html', params)


def search_by_tags(request, tag_id, n=1):
    tag = Tag.objects.get(id=tag_id)
    data = Book.objects.filter(tags=tag)
    page = Paginator(data, 10)
    params = {
            'form':SearchForm(),
            'data':page.get_page(n),
            'tag':tag
        }
    return render(request, 'book/search_by_tags_result.html', params)

#bookのmodel
def model_book(request, book_id, n=1):
    num=book_id
    obj = Book.objects.get(id=num)
    #pageを表示する処理
    data = Page.objects.filter(book_title=obj).order_by('page_number')
    page = Paginator(data, 100)
    page1 = page.get_page(n)[0:10]
    page2 = page.get_page(n)[10:20]
    page3 = page.get_page(n)[20:30]
    page4 = page.get_page(n)[30:40]
    page5 = page.get_page(n)[40:50]
    params = {
            'data1':page1,
            'data2':page2,
            'data3':page3,
            'data4':page4,
            'data5':page5,
            'data':page.get_page(n),
            'obj':obj,
            'title':obj.title,
            'form':SearchForm(),
        }
    return render(request, 'book/model_book.html', params)

#pageのmodel
def model_page(request, page_id, n=1):
    num=page_id
    obj = Page.objects.get(id=num)
    content = Page_content.objects.filter(page_number=obj)
    page = Paginator(content, 10)
    form = SearchForm()
    params = {
            'form':form,
            'data':page.get_page(n),
            'obj':obj,
            'book':obj.book_title,
            'page_num':obj.page_number,
        }
    return render(request, 'book/model_page.html', params)

#page_contentのmodel
def model_page_content(request, content_id):
    num=content_id
    obj = Page_content.objects.get(id=num)
    page = obj.page_number
    page_id = page.id
    form = SearchForm()
    params = {
            'form':form,
            'page_id':page_id,
            'content':obj,
            }
    return render(request, 'book/model_page_content.html', params)
#本作成処理
def create_book(request):
    message = '本を追加する'
    if (request.method == 'POST'):
        #Bookmodelの作成
        title = request.POST['title']
        author = request.POST['author']
        version = request.POST['version']
        check = Book.objects.filter(title=title).filter(author=author).\
            filter(version=version)
        if check.count() == 0:
            obj = Book()
            book = CreateBookForm(request.POST, instance=obj)
            book.save()
            book_id = obj.id

            return redirect('model_book',book_id)
        else:
            message = 'その本はすでに登録されています。'
#            exit = True
    params = {
#            'book':check,
#            'book_id':check.id,
#            'exit':exit,
            'message':message,
            'createform':CreateBookForm(),
            'form':SearchForm(),
        }
    return render(request, 'book/create_book.html', params)

#pageの作成
def create_page(request, book_id):
    book = Book.objects.get(id=book_id)
    message = '　' + str(book) + '　に新しいページを追加する'
    if (request.method == 'POST'):
        num = request.POST['page_number']
        check = Page.objects. filter(page_number=num).\
        filter(book_title=book)        
        if check.count() == 0:
            if (int(num) <= book.page_max):
                page = Page(book_title=book,page_number=num)
                page.save()
                page_id_num = Page.objects.filter(page_number=num).\
            filter(book_title=book).values_list('id', flat = True)[0]
                return redirect('model_page',page_id_num)
            else:
                message = 'そのページは本の最大ページを超えています'
        else:
            message = 'そのページはすでに存在しています'
    params = {
            'book':book,
            'book_id':book_id,
            'message':message,
            'createform':CreatePageForm(),
            'form':SearchForm(),
        }
    
    return render(request, 'book/create_page.html', params)

def create_content(request, page_id):
    page = Page.objects.get(id=page_id)
    message = '　' + str(page) + '　に新しいコンテンツを追加する'
    if (request.method == 'POST'):
        title = request.POST['content_title']
        formula_number = request.POST['formula_number']
        line = request.POST['line']
        formula_or_sentence = request.POST['formula_or_sentence']
        ct = request.POST['content']
        content = Page_content(page_number=page,content_title=title,\
                formula_number=formula_number,line=line,\
                formula_or_sentence=formula_or_sentence,content=ct)
        content.save()
        content_id = content.id
        return redirect('model_page_content',content_id)
    params = {
            'page':page,
            'page_id':page_id,
            'message':message,
            'createform':CreatePage_contentForm(),
            'form':SearchForm(),
        }

    return render(request, 'book/create_content.html', params)



















