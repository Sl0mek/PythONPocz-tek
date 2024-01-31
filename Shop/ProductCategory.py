from enum import Enum


class ProductCategory:
    FOOD = "FOOD"
    COMPUTER_PARTS = "COMPUTER PARTS"
    FRUITS_VEGETABLES = "FRUITS VEGETABLES"
    OTHER = "OTHER"

    def __str__(self):
        return self.value
