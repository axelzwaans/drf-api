# Generated by Django 3.2.17 on 2023-03-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://res.cloudinary.com/doj2kdoew/image/upload/v1675409186/samples/default_profile_oulcxp.jpg', upload_to='images/'),
        ),
    ]
