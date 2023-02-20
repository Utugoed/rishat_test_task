# rishat_test_task

## To test this app you need to:
1. Clone this repository:
  git clone https://github.com/Utugoed/rishat_test_task
2. Update .env file - 
    Put your Stripe API key and Stripe Public key to 
    STRIPE_API_KEY and STRIPE_PUBLIC_KEY  variables respectively
3. Run docker-compose:
  docker-compose up

Then you will be able to log in Django-admin:
  127.0.0.1:8000/admin

With username rishat and password V3rySt0ngP4ss to create new Item and new Order with Items

This app contains the following endpoints:
/item/<int:pk> - Where pk is item primary key. Returns item details
/orders/<int:pk> - Where pk is order primary key. Returns order details
/orders/make_from_product/<int:pk> - Where pk is item primary key. Endpoint for internal use.
                                     Forms an order from one specified product
/buy/success - This page will be returned after successfull order payment
/buy/cancel - This page will be returned after order payment cancelation
/buy/<int:pk> - Where pk is order primary key. Returns Stripe session_id for order payment
