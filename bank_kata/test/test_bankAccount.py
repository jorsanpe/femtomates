from unittest import TestCase
from bank_account import BankAccount
from operation import Operation


class TestBankAccount(TestCase):
    def test_deposit_should_increase_account_amount(self):
        account = BankAccount()
        account.deposit(1000, '2010-01-01')
        self.assertEqual(1000, account.balance())

    def test_retrieve_operation_list_after_several_deposits(self):
        account = BankAccount()
        account.deposit(1000, '2010-01-01')
        account.deposit(2000, '2010-01-01')
        self.assertEqual([Operation(1000, '2010-01-01'), Operation(2000, '2010-01-01')], account.operations())
