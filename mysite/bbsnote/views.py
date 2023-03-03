from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board
from django.utils import timezone
from .forms import BoardForm
from django.core.paginator import Paginator

# Create your views here.

#목차 구현하기
def index(request):
    # return HttpResponse("bbsnote에 오신것을 환영합니다!")
    page = request.GET.get('page',1)
    board_list = Board.objects.order_by('-create_date')
    paginator = Paginator(board_list, 5)
    page_obj = paginator.get_page(page)
    context = {'board_list':page_obj}
    return render(request,'bbsnote/board_list.html', context)
#상세페이지 구현하기 
def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board':board}
    return render(request, 'bbsnote/board_detail.html',context)

#댓글구현하기
def comment_create(request, board_id):
    board = Board.objects.get(id=board_id)
    board.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # comment = Comment(board=board, content=request.POST.get('content'), create_date=timezone.now())
    # comment.save()
    return redirect('bbsnote:detail',board_id=board.id)

#폼 엘리먼트 생성..?
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.create_date = timezone.now()
            board.save()
            return redirect('bbsnote:index')
    else:
        form = BoardForm()
    return render(request, 'bbsnote/board_form.html',{'form':form})