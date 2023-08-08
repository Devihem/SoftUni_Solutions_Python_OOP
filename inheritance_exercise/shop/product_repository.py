from product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for searched_product in self.products:
            if searched_product.name == product_name:
                return searched_product

    def remove(self, product_name):
        removing_product = self.find(product_name)
        if removing_product is not None:
            self.products.remove(removing_product)

    def __repr__(self):
        products_info_repr = '\n'.join([f'{obj_product}: {obj_product.quantity}' for obj_product in self.products])
        return products_info_repr
