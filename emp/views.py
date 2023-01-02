from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Student
from .forms import StudentForm

# Create your views here.


class HomeView(View):
    def get(self, request):
        std = Student.objects.all()
        return render(request, 'emp/base.html', {"std": std})


class Ad_data(View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'emp/form.html', {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request, 'emp/form.html', {'form': form})


class Delete(View):
    def get(self, id):
        std = Student.objects.get(id=id)
        std.delete()
        return redirect('/')


class Update(View):
    def get(self, request, id):
        std = Student.objects.get(id=id)
        form = StudentForm(instance=std)
        return render(request, 'emp/update.html', {'form': form})

    def post(self, request, id):
        std = Student.objects.get(id=id)
        form = StudentForm(request.POST,instance=std)
        if form.is_valid:
         form.save()
         return redirect( '/')



