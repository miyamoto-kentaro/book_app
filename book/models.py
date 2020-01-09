from django.db import models
from taggit.managers import TaggableManager

#book model
class Book(models.Model):
    #field here
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,help_text='本のタイトルを記入')
    author = models.CharField(max_length=100,help_text='著者名を記入')
    version = models.IntegerField(default=1,help_text='版数を入力')
    page_max = models.IntegerField(help_text='最大ページを記入')
    tags = TaggableManager(blank=True)
    
    def __str__(self):
        return str(self.title) + '(' + str(self.author) + ')' + '第' + \
            str(self.version) + '版'

    #Bookの中のページモデル    
class Page(models.Model):
    id = models.AutoField(primary_key=True)
    book_title = models.ForeignKey(Book, on_delete=models.CASCADE)
    page_number = models.IntegerField()
    
    def __init_(self, title):
        self.book_title = title
    
    def __str__(self):
        return  str(self.page_number) + 'ページ' + '(' + str(self.book_title) + ')'

#pegeの中の記事
class Page_content(models.Model):
    id = models.AutoField(primary_key=True)
    page_number = models.ForeignKey(Page, on_delete=models.CASCADE)
    content_title = models.CharField(max_length=100)
    #式
    formula_number = models.CharField(max_length=100)
    line = models.IntegerField()
    formula_or_sentence = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    
    def __str__(self):
        return str(self.content_title) + '(' + str(self.page_number) + ')'
    
    
    
    