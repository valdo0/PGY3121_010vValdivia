# Generated by Django 4.0.4 on 2022-07-16 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petsociety', '0009_orden_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='accesorio',
            field=models.BooleanField(default=False, verbose_name='Es Accesorio'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='idCategoria',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Id De Categoria'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombreCategoria',
            field=models.CharField(max_length=50, verbose_name='Nombre De La Categoria'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=50, verbose_name='Correo Del Cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombreCliente',
            field=models.CharField(max_length=50, verbose_name='Nombre Del Cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rutCliente',
            field=models.CharField(max_length=13, primary_key=True, serialize=False, verbose_name='Rut Del Cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(verbose_name='Telefono Del Cliente'),
        ),
        migrations.AlterField(
            model_name='estado',
            name='estado',
            field=models.CharField(max_length=30, verbose_name='Estado De Pedido'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='petsociety.cliente', verbose_name='Rut Cliente'),
        ),
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='petsociety.estado', verbose_name='Estado De Orden'),
        ),
        migrations.AlterField(
            model_name='ordenproducto',
            name='cantidad',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Cantidad De Producto'),
        ),
        migrations.AlterField(
            model_name='ordenproducto',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petsociety.orden', verbose_name='Id De La Orden'),
        ),
        migrations.AlterField(
            model_name='ordenproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petsociety.producto', verbose_name='Id Producto'),
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ManyToManyField(to='petsociety.categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Del Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='', verbose_name='Imagen Del Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(max_length=50, verbose_name='Marca Del Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombreProducto',
            field=models.CharField(max_length=50, verbose_name='Nombre Del Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(verbose_name='Precio Del Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default='2', verbose_name='Stock Del Producto'),
        ),
    ]