# Generated by Django 3.0.2 on 2020-01-29 12:01

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('languages_plus', '0004_auto_20171214_0004'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=False, max_length=30, unique=True, verbose_name='Method name')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SCType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='SpeedCam code name')),
                ('number', models.PositiveSmallIntegerField(unique=True, verbose_name='SpeedCam type number')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='SpeedCam description')),
                ('user', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SCPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lon', models.DecimalField(decimal_places=8, max_digits=11, verbose_name='Longitude (X)')),
                ('lat', models.DecimalField(decimal_places=8, max_digits=11, verbose_name='Latitude (Y)')),
                ('speed', models.PositiveSmallIntegerField(default=0, verbose_name='Speed limit')),
                ('dirtype', models.PositiveSmallIntegerField(default=1)),
                ('direction', models.SmallIntegerField(default=0, verbose_name='Direction from which SC catches')),
                ('danger', models.BooleanField(default=False)),
                ('priority', models.PositiveSmallIntegerField(default=0)),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date on which the SpeedCam was added')),
                ('active', models.BooleanField(default=False)),
                ('available', models.BooleanField(default=False)),
                ('method', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='TestDrive.Method', verbose_name='Method name')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestDrive.SCType', verbose_name='SpeedCam Type')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=200, verbose_name='Voice message text')),
                ('audio_file_name', models.CharField(blank=True, max_length=30)),
                ('image_file_name', models.CharField(blank=True, max_length=30)),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='languages_plus.Language')),
                ('sctype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TestDrive.SCType')),
            ],
        ),
    ]
