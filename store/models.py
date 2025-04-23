# models.py
from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    nickname = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True, max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'customer'


class Discount(models.Model):
    discount_id = models.AutoField(primary_key=True)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=0)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'discount'


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=255)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE)
    release_date = models.DateField()
    primary_price = models.DecimalField(max_digits=10, decimal_places=0)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    discount = models.ForeignKey(
        Discount, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = 'game'


class GameWishlist(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    wishlist = models.ForeignKey('Wishlist', on_delete=models.CASCADE)
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_wishlist'
        unique_together = (('game', 'wishlist'),)  # Ensures no duplicate game in wishlist


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'genre'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'order'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'order_item'


class Platform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    platform_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'platform'


class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    publisher_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'publisher'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'review'

class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='customer_wishlists'
    )

    class Meta:
        managed = False
        db_table = 'wishlist'
