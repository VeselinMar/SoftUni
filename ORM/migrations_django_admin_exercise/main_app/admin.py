from django.contrib import admin
from main_app.models import EventRegistration, Movie, Student, Supplier, Course, Person, Item, Smartphone, Order


# Register your models here.


class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'participant_name', 'registration_date')
    list_filter = ('event_name', 'registration_date')
    search_fields = ('event_name', 'participant_name')


admin.site.register(EventRegistration, EventRegistrationAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_year', 'genre')
    list_filter = ('release_year', 'genre')
    search_fields = ('title', 'director')


admin.site.register(Movie, MovieAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'grade')
    list_filter = ('age', 'grade', 'date_of_birth')
    search_fields = ('first_name',)
    # organize in two sections
    fieldsets = (
        ('Personal Information', {
         'fields': ('first_name', 'last_name', 'age', 'date_of_birth')}
         ),
        ('Academic Information', {
            'fields': ('grade',)
        })
    )


admin.site.register(Student, StudentAdmin)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_filter = ('name', 'phone')
    search_fields = ('email', 'contact_person', 'phone')
    list_per_page = 20
    fieldsets = (
        ('Information', {
            'fields': ('name', 'contact_person', 'email', 'address')
        }),
    )


admin.site.register(Supplier, SupplierAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'lecturer', 'price', 'start_date')
    list_filter = ('is_published', 'lecturer')
    search_fields = ('title', 'lecturer')
    readonly_fields = ('start_date',)
    fieldsets = (
        ('Course Information', {
            'fields': ('title', 'lecturer', 'price', 'start_date', 'is_published')
        }),
        ('Description', {
            'fields': ('description',)
        })
    )


admin.site.register(Course, CourseAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'age_group')
    list_filter = ('name', 'age_group')
    search_fields = ('name', 'age', 'age_group')
    exclude = ('age_group',)


admin.site.register(Person, PersonAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'rarity')
    list_filter = ('name', 'rarity')
    search_fields = ('name', 'rarity')
    exclude = ('rarity',)


admin.site.register(Item, ItemAdmin)


class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'price', 'category')
    list_filter = ('brand', 'category')
    search_fields = ('brand', 'category')
    exclude = ('category', 'price')


admin.site.register(Smartphone, SmartphoneAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'customer_name', 'order_date', 'status',
                    'amount', 'product_price', 'total_price',
                    'warranty', 'delivery')
    list_filter = ('warranty', 'delivery')
    search_fields = ('product_name', 'customer_name', 'total_price')
    exclude = ('warranty', 'delivery')


admin.site.register(Order, OrderAdmin)
