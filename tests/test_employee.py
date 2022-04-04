from unittest import TestCase

from src.employee import Employee


class TestEmployee(TestCase):

    def test_when_create_new_employee_all_attributes_are_default(self):
        new_employee = Employee()
        self.assertEqual(None, new_employee.first_name)
        self.assertEqual(None, new_employee.last_name)
        self.assertEqual(None, new_employee.staff_id)
        self.assertEqual(None, new_employee.hourly_rate)
        self.assertEqual(None, new_employee.reg_hours)
        self.assertEqual(None, new_employee.otm_multiple)
        self.assertEqual(None, new_employee.tax_credit)
        self.assertEqual(None, new_employee.standard_band)

    def test_compute_net_pay(self):
        self.fail()
