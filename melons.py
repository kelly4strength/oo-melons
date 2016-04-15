"""This file should have our order classes in it."""
#superclass is Abstract Melon Order
class AbstractMelonOrder(object):
    """Initialize melon order attributes"""
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True
        print "shipped"

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty)

        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17
  
    def get_country_code(self):
        """Return the country code."""

        return self.country_code

