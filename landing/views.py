from django.shortcuts import render

##인덱스 파일로 url 설정
def index(request):
    return render(request, 'landing/index.html')
