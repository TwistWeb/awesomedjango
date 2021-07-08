from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

__all__ = [
    'start',
    'index',
    'hello',
    'test'
]


def start(request):
    """
    /
    :param request:
    :return:
    """
    return HttpResponse('')


def index(request):
    """
    index page
    :param request:
    :return:
    """
    return HttpResponse('<h2>Welcome, The is a Index Page!</h2>')


def hello(request):
    """
    hello
    :param request:
    :return:
    """
    return HttpResponse('<h2>Hello, World</h2>')


def test(request):
    """
    test page
    :param request:
    :return:
    """

    hi = "世界是美好的啊"
    test_msg = "这是一个测试页面，模版加载正常，测试成功"
    return render(request, 'test.html', {'hi': hi, 'test_msg': test_msg})
