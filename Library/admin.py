from django.contrib import admin
from .models  import Author, Publication, Book, PublicationAuthor

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","year_of_birth")
    list_filter = ("first_name","year_of_birth")
    readonly_fields = ('first_name',)


    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    # def has_add_permission(self, request):
    #     return False

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

b = Author(first_name="Martin",last_name="Stojanov",year_of_birth="1970")



admin.site.register(Author,AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    pass
    # exclude = ("user",)
admin.site.register(Book,BookAdmin)

class PublicationAuthorAdmin(admin.StackedInline):
    model = PublicationAuthor
    extra = 0
class PublicationAdmin(admin.ModelAdmin):
    inlines = [PublicationAuthorAdmin,]

admin.site.register(Publication,PublicationAdmin)


