from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from Fruitipedia.fruits.forms import CategoryAddForm, AddFruitForm, EditFruitForm, DeleteFruitForm
from Fruitipedia.fruits.models import Fruit


# Create your views here.


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits
    }
    return render(request, 'common/dashboard.html', context)


class CreateFruitView(CreateView):
    model = Fruit
    form_class = AddFruitForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')


# function view
def details_view(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    # create context dictionary
    context = {
        'fruit': fruit
    }
    # render returns request, template_name and the created context dictionary
    return render(request, 'fruits/details-fruit.html', context)


def edit_view(request, pk):
    # get fruit
    fruit = Fruit.objects.get(pk=pk)

    if request.method == "GET":
        form = EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)
        # Check form validity!
        if form.is_valid():
            # save to db!
            form.save()
            # redirect to dashboard
            return redirect('dashboard')
        # fruit.delete() for delete_view FBV

    context = {
        'fruit': fruit,
        'form': form,
    }

    return render(request, 'fruits/edit-fruit.html', context)


class DeleteFruitView(DeleteView):
    model = Fruit
    form_class = DeleteFruitForm
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object)
        return self.render_to_response(self.get_context_data(form=form, object=self.object))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


def create_category_view(request):
    if request.method == "GET":
        form = CategoryAddForm()
    else:  # if "POST"
        form = CategoryAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'categories/create-category.html', context)
