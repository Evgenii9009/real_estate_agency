from django.contrib import admin

from .models import Flat, Complaint, Owner

class OwnershipInline(admin.TabularInline):
    model = Flat.owned_by.through
    raw_id_fields=('owner',) 


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','owner','address')
    readonly_fields = ['created_at']
    list_display = ('address','price','new_building','construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by',)
    inlines = [OwnershipInline]

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'person')

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)

