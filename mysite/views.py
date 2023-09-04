from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import userforms
from .forms import EvenOddform, Marksheet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
def home(request):
    data={
        'title':'Home Page',
        'clist':['PHP','java','django'],
        'numbers':[10,20,30,40],
        's_details':[
            {'name':'Usama', 'phone':3124346681 },
            {'name':'Ali', 'phone':3124346681 },
        ]
    }
    return render(request, 'index.html', data)


def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password') 
        user = authenticate(username=username, password=password)    
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    return render(request,'login.html') 

def logoutuser(reques):
    logout(reques)
    return redirect('login')  



def EvenOdd(request):        
    ev = EvenOddform()
    c=''
    try:
        if request.method=='POST':
            a=int(request.POST.get('num'))
            if a % 2==0:
                c="Even"
            else:
                c="Odd"

    except:
        c='Invalid'    
    return render(request, 'EvenOdd.html',{'c':c, 'form':ev})




def form(request):
    fn=userforms()
    final = 0
    data = {'form':fn}
    try:
        if request.method == 'POST':
            a = int(request.POST.get('num1'))
            b = int(request.POST.get('num2')) 
            final = a + b 
            data = {
                'form':fn,
                'n1':a,
                'n2':b,
                'final':final
            }
          
    except:
        pass
    return render(request, 'form.html', data)


def base(request):
    if request.method=='GET':
        out=request.GET.get('output')
    return render(request, 'base.html',{'ou':out})

def subform(request):
    try:
        if request.method == 'POST':
            a = int(request.POST.get('num1'))
            b = int(request.POST.get('num2')) 
            final = a + b 
            data = {
                'n1':a,
                'n2':b,
                'final':final
            }
            return HttpResponse(final)
    except:
        pass


# def calculator(request):
#     c=''
#     if request.method=='POST':
#         n=eval(request.POST.get('Value1'))
#         m=eval(request.POST.get('Value1')) 
#         n1=eval(n)
#         n2=eval(m)
#         opr =request.POST.get('opr')  
#         if opr == '+':
#             c=n1+n2
#         elif opr == '-':
#             c=n1-n2
#         elif opr == '*':
#             c=n1*n2
#         elif opr == '/':
#             c=n1/n2
           
#     return render(request, 'calculator.html', {'c':c})
def calculator(request):
    ca=userforms()
    c = ''
    try:
        if request.method == 'POST':
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2')) 
            opr=request.POST.get('opr')
            if opr == '+':
                c = n1 + n2
            elif opr == '-':
                c = n1 - n2
            elif opr == '*':
                c = n1 * n2
            elif opr == '/':
                if n2 != 0:
                    c = n1 / n2
                else:
                    c = 'Cannot divide by zero'
            else:
                c = 'Invalid operator'
    except :
        c='Invalid'
    return render(request, 'calculator.html', {'c': c,'form':ca})

def marksheet(request):
    m = Marksheet()
    percentage=''
    total=''
    division=''
    if request.method=='POST':
        s1=eval(request.POST.get('sub1'))
        s2=eval(request.POST.get('sub2'))
        s3=eval(request.POST.get('sub3'))
        s4=eval(request.POST.get('sub4'))
        s5=eval(request.POST.get('sub5'))
        t=eval(request.POST.get('total'))
        total=s1+s2+s3+s4+s5
        percentage=(total/t)*100
        if percentage > 86:
            division='A'
        elif percentage < 86 and percentage > 80:
            division='A-'
        elif percentage < 80 and percentage > 75:
            division='B+'
        elif percentage < 75 and percentage > 70:
            division='B'
        elif percentage < 70 and percentage > 65:
            division='B-'
        elif percentage < 65 and percentage > 60:
            division='C'
        elif percentage < 60 and percentage > 55:
            division='c-'
        elif percentage < 55 and percentage > 51:
            division='D'
        elif percentage ==50:
            division='D-'
        else:
            division='F'
    return render(request, 'marksheet.html',{'form':m,'total_marks_obtained':total,'perc':percentage,'grade':division})
        
        
        

