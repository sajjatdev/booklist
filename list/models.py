from django.db import models

# Create your models here.
# name
# auther forenKey # auther name # auther Address # age # photo
# category
# public_date
# price


class Book_category(models.Model):
    cate_name = models.CharField(max_length=30)

    def __str__(self):
        return self.cate_name


class authers(models.Model):
    name = models.CharField(max_length=20)
    auther_address = models.CharField(max_length=200)
    author_photo = models.ImageField(upload_to='author')
    auther_dateofbr = models.DateField()

    def __str__(self):
        return self.name


class bookList(models.Model):
    auther = models.ForeignKey(authers, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=50)
    Book_categorys = models.ForeignKey(Book_category, on_delete=models.CASCADE)
    public_date = models.DateField()
    book_price = models.CharField(max_length=10)
    book_image = models.ImageField(upload_to='book_image')

    def __str__(self):
        return self.book_name


class Home_Slider(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    image_slider = models.ImageField(upload_to='slider',)

    def __str__(self):
        return self.title


class Cart_view(models.Model):
    cart_product_id = models.IntegerField(primary_key=False)

    def __str__(self):
        return "Cart Item"
