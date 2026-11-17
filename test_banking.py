import pytest
from banking import BankAccount


@pytest.fixture
def account():
    return BankAccount(1000)


# Test 1: Check initial balance
def test_check_balance(account):
    assert account.get_balance() == 1000


# Test 2: Successful deposit
def test_deposit(account):
    account.deposit(500)
    assert account.get_balance() == 1500


# Test 3: Successful withdrawal
def test_withdraw(account):
    account.withdraw(200)
    assert account.get_balance() == 800


# Test 4: Negative deposit
def test_negative_deposit(account):
    with pytest.raises(ValueError):
        account.deposit(-100)


# Test 5: Zero deposit
def test_zero_deposit(account):
    with pytest.raises(ValueError):
        account.deposit(0)


# Test 6: Insufficient balance
def test_insufficient_balance(account):
    with pytest.raises(ValueError):
        account.withdraw(2000)


# Test 7: Negative withdrawal
def test_negative_withdraw(account):
    with pytest.raises(ValueError):
        account.withdraw(-100)


# Test 8: Successful transfer
def test_transfer(account):
    receiver = BankAccount(500)
    account.transfer_to(receiver, 200)

    assert account.get_balance() == 800
    assert receiver.get_balance() == 700


# Test 9: Transfer more than available balance
def test_insufficient_transfer(account):
    receiver = BankAccount(500)

    with pytest.raises(ValueError):
        account.transfer_to(receiver, 2000)

# Test 10: Withdraw exact available balance
def test_withdraw_exact_balance():
    account = BankAccount(1000)
    account.withdraw(1000)
    assert account.get_balance() == 0


# Test 11: Transfer zero amount
def test_zero_transfer(account):
    receiver = BankAccount(500)
    with pytest.raises(ValueError):
        account.transfer_to(receiver, 0)


# Test 12: Transfer negative amount
def test_negative_transfer(account):
    receiver = BankAccount(500)
    with pytest.raises(ValueError):
        account.transfer_to(receiver, -100)


# Test 13: Deposit decimal amount
def test_decimal_deposit(account):
    account.deposit(100.50)
    assert account.get_balance() == 1100.50