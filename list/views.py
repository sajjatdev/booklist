from django.shortcuts import render, redirect
from list.models import bookList, authers, Book_category, Home_Slider, Cart_view
# Create your views here.


def home(res):
    slider_list = []
    newmodel = bookList.objects.all()

    slider = Home_Slider.objects.all()

    for newdata in slider:
        slider_list.append(newdata)

    dir = {'book_list': newmodel, 'slider_data': slider_list}
    return render(res, 'index.html', context=dir)


def auther_view(res, auther_id):

    autherdetails = authers.objects.get(pk=auther_id)
    bookauthlist = bookList.objects.filter(auther=auther_id)
    dir = {'authDetails': autherdetails, 'auther_book': bookauthlist}
    return render(res, 'auther.html', context=dir)


def category(res, category_id):
    category = bookList.objects.filter(Book_categorys=category_id)
    print(category)
    dir = {'category_list': category}
    return render(res, 'category.html', context=dir)


def product_details(res, product_id):
    details = bookList.objects.get(pk=product_id)
    dir = {'product_details': details}
    return render(res, 'product_details_view.html', context=dir)


def shop_view(res):
    product = bookList.objects.all()
    dir = {'product': product}
    return render(res, 'shop.html', context=dir)


def ad_to_cart(res, cart_id):
    if not Cart_view.objects.filter(cart_product_id=cart_id):
        cart_id = Cart_view.objects.create(cart_product_id=cart_id)
        cart_id.save()
    return redirect('/cart/')


def cart_view(res):
    cartdata = []
    total_price = 0
    dcart_data = Cart_view.objects.all()
    print(dcart_data)
    for newdata in dcart_data:
        cartdata.append(bookList.objects.get(pk=newdata.cart_product_id))

    for i in cartdata:
        total_price = total_price + float(i.book_price)
    dir = {'cart_data': cartdata, 'total': round(total_price, 2)}
    return render(res, 'cart.html', context=dir)


def author_view(res):
    author_list = authers.objects.all()

    dir = {'auth_list': author_list}
    return render(res, 'author_list.html', context=dir)
