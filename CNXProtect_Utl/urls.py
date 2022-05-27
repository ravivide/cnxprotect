"""CNX_Protect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import re_path as url

admin.site.site_header = "CNX Protect"
admin.site.site_title = "CNX Protect Portal"
admin.site.index_title = "Welcome to CNX Protect Portal"

urlpatterns = [
    path('', views.index, name='index'),
    # path('login_page', views.login_page, name='login_page'),
    #path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('blog', views.blog, name='blog'),
    path('Contract_Library', views.Contract_Library, name='Contract_Library'),
    path('Contract_Library1', views.Contract_Library1, name='Contract_Library1'),
    path('FMEA', views.FMEA, name='FMEA'),
    path('cl_files', views.cl_files, name='cl_files'),# bring into login page
    # path('email_files', views.email_files, name='email_files'),  # bring into login page
    path('single_work', views.single_work, name='single_work'),
    #path('login_page/', views.keyword_list),
    path('keyword_list', views.keyword_list, name='keyword_list'),# bring into login page
    path('insert_keyword_item', views.insert_keyword_item, name='insert_keyword_item'),
    path('<int:keyword_id>', views.delete_keyword_item, name='delete_keyword_item'),

    path('keyword_list1', views.keyword_list1, name='keyword_list1'),# bring into login page
    path('insert_keyword_item1', views.insert_keyword_item1, name='insert_keyword_item1'),
    path('<int:keyword_id>', views.delete_keyword_item1, name='delete_keyword_item1'),

    path('keyword_list2', views.keyword_list2, name='keyword_list2'),# bring into login page
    path('insert_keyword_item2', views.insert_keyword_item2, name='insert_keyword_item2'),
    path('<int:keyword_id>', views.delete_keyword_item2, name='delete_keyword_item2'),

    path('read_file', views.read_file, name='read_file'),
    path('read_file1', views.read_file1, name='read_file1'),
    path('read_file_1', views.read_file_1, name='read_file_1'),
    path('CLBT_reports', views.CLBT_reports, name='CLBT_reports'),
    path('master_data', views.master_data, name='master_data'),
    path('Contract_library', views.Contract_library, name='Contract_library'),
    path('FMEA_Real', views.FMEA_Real, name='FMEA_Real'),
    path('FM_Real', views.FM_Real, name='FM_Real'),
    # path('FMEA_Files', views.FMEA_Files, name='FMEA_Files'),
    # path('indexing1', views.indexing1, name='indexing1'),
    path('Indexing', views.Indexing, name='Indexing'),
    path('insert_MSA_item', views.insert_MSA_item, name='insert_MSA_item'),
    path('MSA_list', views.MSA_list, name='MSA_list'),
    path('add_keywords', views.add_keywords, name='add_keywords'),
    path('add_keywords_FMEA', views.add_keywords_FMEA, name='add_keywords_FMEA'),
    path('download', views.download, name='download'),
    path('experiment', views.experiment, name='experiment'),
    path('experiment1', views.experiment1, name='experiment1'),
    path('experiment2', views.experiment2, name='experiment2'),
    path('FMEA_Indexing', views.FMEA_Indexing, name='FMEA_Indexing'),
    path('score_card', views.score_card, name='score_card'),
    path('pdfword', views.pdfword, name='pdfword'),
    path('indexing1', views.indexing1, name='indexing1'),
    path('indexing2', views.indexing_data2, name='indexing_data2'),
    path('indexing3', views.indexing_data3, name='indexing_data3'),
    path('indexing4', views.indexing_data4, name='indexing_data4'),
    path('indexing5', views.indexing_data5, name='indexing_data5'),
    path('Main_page_template', views.Main_page_template, name='Main_page_template'),

]

