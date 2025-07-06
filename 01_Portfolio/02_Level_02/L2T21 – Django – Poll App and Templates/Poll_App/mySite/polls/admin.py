
from django.contrib import admin
from .models import Question, Choice

# Solution for inline modeling courtesy of Google, to enable the choices
# to be nested withing the questions admin panel and linked accordingly based
# on the initial PK we set up between the two tables.

# Inline child table


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Main parent table


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
