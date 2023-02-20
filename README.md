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
  **127.0.0.1:8000/admin**

With username **rishat** and password **V3rySt0ngP4ss** to create new Item and new Order with Items

This app contains the following endpoints:
1. /item/<int:pk> - Where pk is **item** primary key. Returns item details
2. /orders/<int:pk> - Where pk is **order** primary key. Returns order details
3. /orders/make_from_product/<int:pk> - Where pk is item primary key. Endpoint for internal use.
                                     Forms an order from one specified product
4. /buy/success - This page will be returned after successfull order payment
5. /buy/cancel - This page will be returned after order payment cancelation
6. /buy/<int:pk> - Where pk is **order** primary key. Returns Stripe session_id for order payment
