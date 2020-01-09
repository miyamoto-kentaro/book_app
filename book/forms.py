from django import forms
from .models import Book
from .models import Page
from .models import Page_content

#Book(model)の追加form
class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','version','page_max','tags']

#Searchform
class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)
    
#create page
class CreatePageForm(forms.ModelForm):
    class Meta:
        model = Page
                       #'book_title',
        fields = ['page_number']

#create page content
class CreatePage_contentForm(forms.ModelForm):
    class Meta:
        model = Page_content
        fields = ['content_title','formula_number',\
                  'line','formula_or_sentence','content']

#Bookの編集form

        
#tag追加form
