import phonenumbers


from django.db import migrations


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phone_number = flat.owners_phonenumber
        parsed_number = phonenumbers.parse(phone_number, 'RU')
        if phonenumbers.is_valid_number(parsed_number):
            flat.owner_pure_phone = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20250115_1737'),
    ]

    operations = [migrations.RunPython(normalize_phone_numbers)
    ]
