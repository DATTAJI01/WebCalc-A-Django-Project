from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    context={}
    return render(request,'Calculator.html',context)


def calculate(request):
    if request.method == 'POST':
        First_value = request.POST.get('First_value')
        Second_value = request.POST.get('Second_value')
        Operation = request.POST.get('Operation')

        if Operation == 'add':
            result = eval(First_value) + eval(Second_value)
            context = {'result': result}
            return render(request,'Calculator.html',context)
        
        elif Operation == 'subtract':
            result = eval(First_value) - eval(Second_value)
            context = {'result': result}
            return render(request,'Calculator.html',context)
        
        elif Operation == 'multiply':
            result = eval(First_value) * eval(Second_value)
            context = {'result': result}
            return render(request,'Calculator.html',context)
        
        elif Operation == 'divide':
            result = eval(First_value) / eval(Second_value)
            context = {'result': result}
            return render(request,'Calculator.html',context)
    else:
        return HttpResponse('Calculator.html')
