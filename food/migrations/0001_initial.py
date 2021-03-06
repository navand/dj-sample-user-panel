# Generated by Django 3.1.7 on 2021-03-27 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from food.models import Food

def createUserGroup(apps, schema_editor):
    clientGroup, created = Group.objects.get_or_create(name='Client')
    contentType = ContentType.objects.get_for_model(Food)
    # Can change food
    permission = Permission.objects.create(codename='change_food',
                                   name='Can change food',
                                   content_type=contentType)
    clientGroup.permissions.add(permission)
    # Can view food
    permission = Permission.objects.create(codename='view_food',
                                   name='Can view food',
                                   content_type=contentType)
    clientGroup.permissions.add(permission)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('telephone', models.CharField(max_length=15, null=True)),
                ('profilePicture', models.ImageField(default='blank.png', upload_to='uploads')),
                ('dateOfBirth', models.DateField(null=True)),
                ('favoriteFood', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(limit_choices_to={'groups__name': 'Client'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Food form',
                'db_table': 'food',
            },
        ),
        migrations.RunPython(createUserGroup),
    ]
