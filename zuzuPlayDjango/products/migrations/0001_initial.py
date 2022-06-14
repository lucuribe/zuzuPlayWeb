# Generated by Django 4.0.4 on 2022-06-14 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.CharField(max_length=1, primary_key=True, serialize=False, verbose_name='Id')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombreMarca', models.CharField(max_length=50, verbose_name='Nombre')),
                ('estadoMarca', models.BooleanField(default=True, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('idPlataforma', models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='Id')),
                ('nombrePlataforma', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='SKU')),
                ('nombreProducto', models.CharField(max_length=75, verbose_name='Nombre')),
                ('imagenProducto', models.ImageField(upload_to='products/media', verbose_name='Imagen')),
                ('fechaLanProducto', models.DateField(blank=True, null=True, verbose_name='Fecha de lanzamiento')),
                ('precioProducto', models.IntegerField(verbose_name='Precio')),
                ('estadoProducto', models.BooleanField(default=True, verbose_name='Estado')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.marca')),
                ('plataforma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.plataforma')),
            ],
        ),
        migrations.CreateModel(
            name='Suscriptor',
            fields=[
                ('idSuscriptor', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('emailSuscriptor', models.CharField(max_length=100, unique=True, verbose_name='Email')),
                ('estadoSuscriptor', models.BooleanField(default=True, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('idUnidad', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='UPC')),
                ('fechaIngUnidad', models.DateField(verbose_name='Fecha de ingreso')),
                ('estadoUnidad', models.BooleanField(default=True, verbose_name='Estado')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('idSubcategoria', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Id')),
                ('nombreSubcategoria', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('estadoSubcategoria', models.BooleanField(default=True, verbose_name='Estado')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoria', verbose_name='Categoría')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='subcategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.subcategoria', verbose_name='Subcategoría'),
        ),
    ]
