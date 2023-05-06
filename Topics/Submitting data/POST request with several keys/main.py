from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):        
        if request.POST["todo"] not in self.all_todos:
            if request.POST["important"]:
                self.all_todos.insert(0, request.POST["todo"])
            else:
                self.all_todos.append(request.POST["todo"])
        return redirect('/')
