from locust import HttpUser, task, between
from random import randint


class WebSiteUser(HttpUser):
    wait_time = between(1, 5)

    @task(4)
    def view_products(self):
        # print('view_products')
        collection_id = randint(2, 6)
        self.client.get(
            f"/store/products/?collection_id={collection_id}",
            name="/store/products")

    @task(2)
    def view_product(self):
        # print('view_product')
        product_id = randint(1, 800)
        self.client.get(
            f"/store/products/{product_id}",
            name="/store/products/:id")

    @task(1)
    def add_to_cart(self):
        # print('add_to_cart')
        product_id = randint(1, 10)
        self.client.post(
            f"/store/carts/{self.cart_id}/items/",
            data={'product_id': {product_id}, 'quantity': 1},
            name="/store/carts/items")

    @task
    def say_hello(self):
        self.client.get('/playground/hello/', name='/playground/hello')

    def on_start(self):
        response = self.client.post("/store/carts/", name="/store/carts")
        result = response.json()
        self.cart_id = result['id']
