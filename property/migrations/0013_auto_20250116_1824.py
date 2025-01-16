from django.db import migrations

def create_flateowner_connection(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(owner_name=flat.owner, owners_phonenumber=flat.owners_phonenumber, defaults={
            'owner_pure_phone':flat.owner_pure_phone
        })
        owner.owned_flats.add(flat)



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20250116_1815'),
    ]

    operations = [migrations.RunPython(create_flateowner_connection)
    ]