from django.shortcuts import render, redirect
from django.conf import settings

import stripe

from items.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request, item_id):
    print(Item.objects.get(id=item_id))
    name = Item.objects.get(id=item_id).name
    price = Item.objects.get(id=item_id).price

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": name,
                    },
                    "unit_amount": int(price * 100),
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url="http://localhost:8000/buy/success",
        cancel_url="http://localhost:8000/buy/cancel",
    )
    return redirect(checkout_session.url, code=303)


def success(request):
    return render(request, "buy/success.html")


def cancel(request):
    return render(request, "buy/cancel.html")
