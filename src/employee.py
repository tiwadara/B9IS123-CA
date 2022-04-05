# Create a class employee

class Employee:
    __standard_rate = 0.2
    __higher_rate = 0.4
    __prsi = 0.04

    def __init__(self, staff_id=None, first_name=None, last_name=None, reg_hours=None, hourly_rate=None,
                 otm_multiple=None, tax_credit=None, standard_band=None):
        self.__hours_worked = None
        self.staff_id = staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.reg_hours = reg_hours
        self.hourly_rate = hourly_rate
        self.otm_multiple = otm_multiple
        self.tax_credit = tax_credit
        self.standard_band = standard_band

    def compute_payment(self, hours_worked, date):
        self.__hours_worked = hours_worked
        response = {
            "name": self.__get_employee_name(),
            "Date": date,
            "Regular Hours Worked": self.reg_hours,
            "Overtime Hours Worked": self.__get_overtime_hours(),
            "Regular Pay": self.__get_regular_pay(),
            "Regular Rate": self.hourly_rate,
            "Overtime Pay": self.__get_overtime_pay(),
            "Overtime Rate": self.__get_overtime_rate(),
            "Gross Pay": self.__get_gross_pay(),
            "Standard Rate Pay": self.standard_band,
            "Higher Rate Pay": self.__get_higher_rate_pay(),
            "Standard Tax": self.__get_standard_tax(),
            "Higher Tax": self.__get_higher_tax(),
            "Total Tax": self.__get_total_tax(),
            "Tax Credit": self.tax_credit,
            "Net Tax": self.__get_net_tax(),
            "PRSI": self.__get_prsi(),
            "Net Deductions": self.__get_net_deductions()
        }

        return response

    def get_net_pay(self):
        return self.__get_gross_pay() - self.__get_net_deductions()

    def __get_overtime_hours(self):
        return max(0, self.__hours_worked - self.reg_hours)

    def __get_employee_name(self):
        return self.first_name + ' ' + self.last_name

    def __get_regular_pay(self):
        return self.reg_hours * self.hourly_rate

    def __get_overtime_pay(self):
        return self.__get_overtime_hours() * self.__get_overtime_rate()

    def __get_overtime_rate(self):
        return self.hourly_rate * self.otm_multiple

    def __get_prsi(self):
        return self.__get_gross_pay() * self.__prsi

    def __get_gross_pay(self):
        if self.__hours_worked <= self.reg_hours:
            return self.__get_regular_pay()
        elif self.__hours_worked > self.reg_hours:
            return self.__get_regular_pay() + self.__get_overtime_pay()

    def __get_standard_tax(self):
        return self.standard_band * self.__standard_rate

    def __get_higher_tax(self):
        return self.__get_higher_rate_pay() * self.__higher_rate

    def __get_standard_rate_pay(self):
        return self.reg_hours * self.hourly_rate * self.__standard_rate

    def __get_higher_rate_pay(self):
        return self.__get_gross_pay() - self.standard_band

    def __get_higher_rate(self):
        return self.__get_higher_rate_pay() * self.__higher_rate

    def __get_net_deductions(self):
        return self.__get_net_tax() + self.__get_prsi()

    def __get_total_tax(self):
        return self.__get_standard_tax() + self.__get_higher_tax()

    def __get_net_tax(self):
        return round((self.__get_total_tax() - self.tax_credit), 2)
