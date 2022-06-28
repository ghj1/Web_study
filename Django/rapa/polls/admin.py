from django.contrib import admin
from django.db import models
from polls.models import Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin): #add admin 
    fieldsets = [
        #('Question Statement', {'fields': ['question_text']}),
        (None,                  {'fields':['question_text']}),
       # ('Date Information', {'fields': ['pub_date']}),
        ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [(ChoiceInline)] #add Choice 모델 클래스 같이 보이도록
    list_display = ('question_text', 'pub_date') # 레코드 리스트 컬럼 지정
    list_filter = ['pub_date'] # 필터 사이드 바 추가
    search_fields = ['question_text'] # 검색 박스 추가하기 

admin.site.register(Question, QuestionAdmin) # register admin: QuestionAdmin 
admin.site.register(Choice)