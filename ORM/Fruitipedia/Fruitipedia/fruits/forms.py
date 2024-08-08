from django import forms

from Fruitipedia.fruits.models import Category, Fruit


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Category name', }), }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''


class CategoryAddForm(CategoryForm):
    pass


class CategoryDeleteForm(CategoryForm):
    pass


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Fruit name', }),
            'image_url': forms.TextInput(attrs={'placeholder': 'Enter Image url', }),
            'description': forms.TextInput(attrs={'placeholder': 'Enter Fruit description', }),
            'nutrition': forms.TextInput(attrs={'placeholder': 'Enter Fruit nutrition', }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''


class AddFruitForm(BaseFruitForm):
    pass


class EditFruitForm(BaseFruitForm):
    pass


class DeleteFruitForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
