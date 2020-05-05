# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import TextInput, Textarea
from django.db import models
from django.forms import TextInput, Textarea
from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .models import Team




class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'id','name','dept'
    )
    

    

    

admin.site.register(Team,TeamAdmin)
