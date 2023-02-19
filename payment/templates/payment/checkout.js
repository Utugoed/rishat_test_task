var stripe = Stripe(checkout_public_id);

const btn = document.querySelector("#buy_now_btn");

btn.addEventListener('click', event => {
    stripe.redirectToCheckout({
        sessionId: checkout_session_id
    }).then(function (result) {

    })
})
