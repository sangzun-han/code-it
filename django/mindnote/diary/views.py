from django.shortcuts import render
from .models import Page

# Create your views here.
def page_list(request):
    object_list = Page.objects.all() # 데이터 조회
    return render(request, 'diary/page_list.html', {'object_list': object_list})

def page_detail(request, page_id):
    object = Page.objects.get(id=page_id)
    return render(request, 'diary/page_detail.html', {'object': object})

def info(request):
    return render(request, 'diary/info.html')