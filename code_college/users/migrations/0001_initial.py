<<<<<<< b033a97a75edabfdf649fb096b8618557a6a01f9
# Generated by Django 2.0.4 on 2018-04-22 14:13
=======
# Generated by Django 2.0.4 on 2018-04-22 14:03
>>>>>>> Refactor models to Package Diagram

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< b033a97a75edabfdf649fb096b8618557a6a01f9
=======
        ('universities', '__first__'),
>>>>>>> Refactor models to Package Diagram
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdinaryUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birthday', models.DateField()),
                ('college', models.CharField(max_length=80)),
                ('college_registry', models.CharField(max_length=20)),
<<<<<<< b033a97a75edabfdf649fb096b8618557a6a01f9
=======
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='universities.University')),
>>>>>>> Refactor models to Package Diagram
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
