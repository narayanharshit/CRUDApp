from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        # if there's a migration you depend on, mention it here like ('app_name', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=255)),
            ],
        ),
    ]
