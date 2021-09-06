[TOC]

### 01. 왜 변수 context는 if else 구문과 동일한 레벨에 작성되어 있는가?

<br>

```
else 조건 내부에 context가 작성되어있다고 가정하면,

만일 요청 method가 POST이면서, 유효하지 않은 데이터가 작성되면,
첫번째 조건문인 if request.method == 'POST'는 통과하고,
두 번째 조건문인 if form.is_valid()에서는 통과하지 못하게 된다.
두번째 조건문에서는 유효성 검사를 통과한 경우에만 return 값을 주기 때문에, 위와 같은 경우는 에러가 발생할 수 있다.

이는 if else 구문과 동일한 레벨에 context가 위치하도록 들여쓰기를 조정하면 해결할 수 있다.

또한, if else 구문과 같은 레벨에 context를 작성함으로써, 
두번째 조건문인 form.is_valid()로 유효성 검사를 실패한 경우에도 is_valid()에서 발생한 에러 메시지를 context의 form에 담아서 전달할 수 있다.
```

<br>

### 02. 왜 request의 http method는 POST 먼저 확인하도록 작성하는가? 

> DB를 조작하는 부분을 POST 요청에서만 실행되게 하기 위해서

<br>

```python
# POST 먼저 확인하는 경우
def create(request):
    # create, 즉 게시물을 작성하는 POST 메서드인 경우
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # new
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)
```

<br>

```python
# 1. 불필요한 반복
def create(request):
    if request.method == 'GET':
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/index.html', context)

    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        else:
            context = {
                'form' : form
            }
            return render(request, 'articles/index.html', context)
```

<br>

```python
# 2. if (GET메서드일 때), else(POST, PUT, DELETE 등 GET이 아닌 다른 메서드일 때)
def create(request):
    if request.method == 'GET':
        form = ArticleForm()
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
   
    context = {
        'form': form,
    }
    return render(request, 'articles/index.html', context)
```

