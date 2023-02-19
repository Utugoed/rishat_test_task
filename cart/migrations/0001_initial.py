# Generated by Django 4.1.6 on 2023-02-19 14:51

from django.db import migrations, models
import django.db.models.deletion
import payment.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0004_alter_item_stripe_price_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, validators=[payment.models.validate_positive])),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.item')),
            ],
        ),
    ]