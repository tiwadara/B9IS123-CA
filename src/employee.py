# Create a class employee

class Employee:
    __standard_rate = 0.2
    __higher_rate = 0.4
    __prsi = 0.04

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
        response = {
            "name": self.__get_employee_name(),
            "Date": date,
            "Regular Hours Worked": self.reg_hours,
            "Overtime Hours Worked": self.__get_overtime_hours(hours_worked),
            "Regular Pay": "",
            "Regular Rate": self.hourly_rate,
            "Overtime Pay": "",
            "Overtime Rate": "",
            "Gross Pay": "",
            "Standard Rate Pay": "",
            "Higher Rate Pay": "",
            "Standard Tax": "",
            "Higher Tax": "",
            "Total Tax": "",
            "Tax Credit": self.tax_credit,
            "Net Tax": "",
            "PRSI": "",
            "Net Deductions": ""
        }

        return response

    def __get_overtime_hours(self, hours_worked):
        return max(0, hours_worked - self.reg_hours)

    def __get_employee_name(self):
        return self.first_name + ' ' + self.last_name
