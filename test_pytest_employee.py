import pytest
from employee import Employee

person = Employee('Sara', 'Smith', 10)


def test_email():
    assert person.email == 'Sara.Smith@email.com'


def test_fullname():
    assert person.fullname == 'Sara Smith'


def test_apply_raise():
    assert person.pay == 10
    person.apply_raise()
    assert person.pay == 10


def test_monthly_schedule(requests_mock):
    requests_mock.get("http://company.com/Smith/june", text="data")
    assert person.monthly_schedule('june') == 'data'
