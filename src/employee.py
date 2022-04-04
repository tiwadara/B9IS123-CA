# Create a class employee

class Employee:
    def __init__(self, staff_id=None, first_name=None, last_name=None, reg_hours=None, hourly_rate=None,
                 otm_multiple=None, tax_credit=None, standard_band=None):
        self.staff_id = staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.reg_hours = reg_hours
        self.hourly_rate = hourly_rate
        self.otm_multiple = otm_multiple
        self.tax_credit = tax_credit
        self.standard_band = standard_band

    def compute_payment(self, hours_worked, date):
        pass

