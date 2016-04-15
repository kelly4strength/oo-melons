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
        #Christmas Melon Pricing
        #checkng if species is equal to christmas melon(first we 
        #had "is" which checked for christmas melon was in the same place in memory)
        if self.species == "christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
       
        #International Pricing       
        if self.qty < 10 and self.order_type == "international":
            total += 3 
        return total
                

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08

class GovernmentMelonOrder(DomesticMelonOrder):
    """US Government Melon orders, no tax applied, inspections required."""

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.passed_inspection = False
        self.order_type = "domestic"
        self.tax = 0 

    def mark_inspected(self):
        self.passed_inspection = True
        print "passed inspection"


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

