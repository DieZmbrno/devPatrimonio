# Generated by Django 4.2.5 on 2023-11-17 03:08

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='historialvisitas',
            name='fk_destino',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.destinocultural'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='usuario_groups', related_query_name='usuario_group', to='auth.group'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='default_password_value', max_length=128),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='usuario_user_permissions', related_query_name='usuario_user_permission', to='auth.permission'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default='default_username_value', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='historialvisitas',
            name='destinoVisitados',
            field=models.CharField(default='default_destino_value', max_length=255),
        ),
        migrations.AlterField(
            model_name='historialvisitas',
            name='idHistorial',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idUsuario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]