from unittest import TestCase

from src.employee import Employee


class TestEmployee(TestCase):

    def test_when_create_new_employee_all_attributes_are_default(self):
        new_employee = Employee()
        self.assertEqual(None, new_employee.staff_id)
        self.assertEqual(None, new_employee.first_name)
        self.assertEqual(None, new_employee.last_name)
        self.assertEqual(None, new_employee.hourly_rate)
        self.assertEqual(None, new_employee.reg_hours)
        self.assertEqual(None, new_employee.otm_multiple)
        self.assertEqual(None, new_employee.tax_credit)
        self.assertEqual(None, new_employee.standard_band)

    def test_when_a_new_employee_is_initialized_then_the_exact_values_are_returned(self):
        new_employee = Employee(12345, 'Joe', 'Green', 37, 16, 1.5, 72, 710)
        self.assertEqual(12345, new_employee.staff_id)
        self.assertEqual('Joe', new_employee.first_name)
        self.assertEqual('Green', new_employee.last_name)
        self.assertEqual(37, new_employee.reg_hours)
        self.assertEqual(16, new_employee.hourly_rate)
        self.assertEqual(1.5, new_employee.otm_multiple)
        self.assertEqual(72, new_employee.tax_credit)
        self.assertEqual(710, new_employee.standard_band)

    def test_when_compute_payment_is_called_the_payment_dictionary_is_returned(self):
        new_employee = Employee(12345, 'Joe', 'Green', 37, 16, 1.5, 72, 710)
        hours_worked = 42
        date = '31/10/2021'
        response = {
            "name": "Joe Green",
            "Date": "31/10/2021",
            "Regular Hours Worked": 37,
            "Overtime Hours Worked": 5,
            "Regular Rate": 16,
            "Overtime Rate": 24,
            "Regular Pay": 592,
            "Overtime Pay": 120,
            "Gross Pay": 712,
            "Standard Rate Pay": 710,
            "Higher Rate Pay": 2,
            "Standard Tax": 142,
            "Higher Tax": 0.8,
            "Total Tax": 142.8,
            "Tax Credit": 72,
            "Net Tax": 70.8,
            "PRSI": 28.48,
            "Net Deductions": 99.28
        }
        payment = new_employee.compute_payment(hours_worked, date)
        self.assertEqual(response, payment)

    def testNetPayLessEqualGross(self):
        new_employee = Employee(12345, 'Joe', 'Green', 37, 16, 1.5, 72, 710)
        hours_worked = 42
        date = '31/10/2021'
        payment = new_employee.compute_payment(hours_worked, date)
        self.assertLessEqual(new_employee.get_net_pay(), payment['Gross Pay'])

    def testOvertimePayOrOvertimeHoursCannotBeNegative(self):
        new_employee = Employee(12345, 'Joe', 'Green', 37, 16, 1.5, 72, 710)
        hours_worked = 10
        date = '31/10/2021'
        new_employee.compute_payment(hours_worked, date)
        over_time = new_employee.get_overtime_pay()
        self.assertGreaterEqual(over_time, 0)

    def testHigherTaxCannotBeNegative(self):
        new_employee = Employee(12345, 'Joe', 'Green', 37, 16, 1.5, 72, 710)
        hours_worked = 10
        date = '31/10/2021'
        new_employee.compute_payment(hours_worked, date)
        higher_rate_pay = new_employee.get_higher_rate_pay()
        self.assertGreaterEqual(higher_rate_pay, 0)

    def testNetPayCannotBeNegative(self):
        new_employee = Employee(12345, 'Joe', 'Green', 37, 16, 1.5, 72, 710)
        hours_worked = -100
        date = '31/10/2021'
        new_employee.compute_payment(hours_worked, date)
        net_pay = new_employee.get_net_pay()
        self.assertGreaterEqual(net_pay, 0)
