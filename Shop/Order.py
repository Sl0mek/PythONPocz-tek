class Order:

    def __init__(self, customer_first_name, customer_last_name, products = None):
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name
        if products is None:
            products = []
        self.total_price = 0
        for product in products:
            self.total_price = self.total_price + product.unite_price
    
