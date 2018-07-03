from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # 请求路径和请求方法
    print(request.path, request.method)
    # 请求头的元信息和GET请求参数(查询叁数)
    # print(request.META)
    print(request.GET)
    print(request.GET.get('page'), request.GET.get('tag'))

    # POST请求参数(表单参数)
    print(request.POST)
    return render(request,
                  'art/list.html',
                  context={'name':'disen', 'age':20})
    # return JsonResponse({'name':'disen', 'age':20})

