# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View  
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.views.generic import CreateView
from .forms import UserCreateForm, LoginForm
from .models import UserDB
from .models import SampleDB


class Search_View(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_folder/search.html')


class Time_line_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_folder/time_line.html')


class History_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_folder/history.html')


class Registed_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_folder/registed.html')


class Saved_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_folder/saved.html')


class Notlogin_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_folder/notlogin.html')


class Registed_login_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_folder/registed/login.html')


class Registed_personal_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_folder/registed/personal.html')


class Registed_login_terms_View(View):
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_folder/registed/login/terms.html')


# 会員登録
class Registed_login_create_View(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            # フォームから'email'を読み取る
            email = form.cleaned_data.get('email')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'app_folder/registed/login/create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, 'app_folder/registed/login/create.html', {'form': form,})


# #ログイン機能
class Registed_login_login_View(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = UserDB.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'app_folder/registed/login/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'app_folder/registed/login/login.html', {'form': form,})


class Logout_View(LogoutView):
    template_name = 'app_folder/search.html'


class SampleView(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_folder/search.html')

    def post(self, request, *args, **kwargs):  
        input_data = request.POST['input_data']
        result = SampleDB.objects.filter(sample1=input_data)
        result_sample1 = result[0].sample1
        result_sample2 = result[0].sample2
        context={'result_sample1':result_sample1, 'result_sample2':result_sample2}
        return render(request, 'app_folder/admin.html', context=context,)


search = Search_View.as_view()
time_line = Time_line_View.as_view()
history = History_View.as_view()
registed = Registed_View.as_view()
saved = Saved_View.as_view()
notlogin = Notlogin_View.as_view()
registed_login = Registed_login_View.as_view()
registed_personal = Registed_personal_View.as_view()
registed_login_terms = Registed_login_terms_View.as_view()
registed_login_login = Registed_login_login_View.as_view()
registed_login_create = Registed_login_create_View.as_view()
logout = Logout_View.as_view()
sample = SampleView.as_view()