from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView


class MyLoginView(LoginView):
    template_name = 'schedule/login.html'
    success_url = reverse_lazy('course_list') # replace 'home' with the name of your homepage URL

    def get_success_url(self):
        return self.success_url


class SignupView(CreateView):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'schedule/sign_up.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
        return render(request, 'schedule/sign_up.html', {'form': form})


class CourseView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        return render(request, "schedule/course.html", {"course": course})


class TeacherView(View):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        return render(request, "schedule/teacher.html", {"teacher": teacher})


class SearchFormView(FormView):
    form_class = SearchForm
    template_name = '/schedule/index.html'
    success_url = reverse_lazy('main')

    def is_valid(self, form):
        q = form.cleaned_data['q']
        return super().form_valid(form)


# Create your views here.
class CourseListView(View):

    def get(self, request):
        form = SearchForm()
        search_query = request.GET.get('q', '')
        course_list = Course.objects.filter(title__contains=search_query) if search_query else Course.objects.all()
        return render(request, "schedule/index.html", {'form': form, "course_list": course_list})


class StudentRegisterFormView(FormView):
    def get(self, request):
        form = StudentRegisterModelForm()
        return render(request, "schedule/add_course.html", {'form': form})

    def post(self, request):
        form = StudentRegisterModelForm(request.POST)
        if form.is_valid():
            student = Student(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                age=form.cleaned_data['age'],
            )
            student.save()
            courses = [form.cleaned_data['course']]
            student.course.set(courses)
        return render(request, "schedule/add_course.html", {'form': form})