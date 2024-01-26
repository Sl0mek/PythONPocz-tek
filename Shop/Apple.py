class Apple:

    def __init__(self, species_name, size, price_per_kg):
        self.species_name = species_name
        self.size = size
        self.price_per_kg = price_per_kg

    def calculate_price(self):
        return self.size * self.price_per_kg

    def __repr__(self):
        return f"<class: Apple, species_name: {self.species_name}, size: {self.size}, price_per_kg: {self.price_per_kg}"
