from django.shortcuts import redirect, render
from .models import Article

# Create your views here.
# def index(request):
#     return render(request, 'articles/index.html')

# index 수정해주기
def index(request):
    # articles = Article.objects.all()[::-1]      # 파이썬이 변경해주는 내용(역출력)
    articles = Article.objects.order_by('-id')  # ORM으로 순서 변경
    
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')

def create(request):
    print(request.POST)
    title = request.POST.get('title')
    content = request.POST.get('content')

    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    
    # 첫번째 title: model title
    # 두번째 title: request.GET.get('title) 즉, 사용자로부터 받아온 title
    article = Article(title=title, content=content)
    # Validation 유효성 검증 중간 과정
    article.save()

    # return render(request, 'articles/create.html')
    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context= {
        'article': article
    }

    return render(request, 'articles/detail.html', context)

# delete는 주로 detail.html에 있음
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context= {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    # 사용자가 입력한 내용 받아와서, article.title에 넣어주기
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    
    return redirect('articles:detail', article.pk)
