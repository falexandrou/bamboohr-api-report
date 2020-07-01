"""Formatters the report"""
# -*- coding: utf-8 -*-
import re
import datetime


def _create_full_name(first_name=None, middle_name=None, last_name=None):
    """Returns a full name based on the given information"""
    full_name_parts = []

    if first_name:
        full_name_parts.append(first_name.strip())

    if middle_name:
        full_name_parts.append(middle_name.strip())

    if last_name:
        full_name_parts.append(last_name.strip())

    return ' '.join(full_name_parts).strip(' ')


def get_full_name(entry):
    """Returns the employee's first name"""
    return _create_full_name(
        first_name=entry.get('firstName'),
        middle_name=entry.get('middleName'),
        last_name=entry.get('lastName'))


def get_address(entry):
    """Returns the employee's full address"""
    address_parts = []

    if entry.get('addressLines'):
        address_parts.append(entry['addressLines'].strip())

    if entry.get('cityState'):
        address_parts.append(entry['cityState'].strip())

    if entry.get('country'):
        address_parts.append(entry['country'].strip())

    return ', '.join(address_parts).strip(', ')


def _calculate_leave(taken=0.0, balance=0.0):
    """Calculates the total leave for the user"""
    try:
        taken = float(taken)
    except ValueError:
        taken = 0.0

    try:
        balance = float(balance)
    except ValueError:
        balance = 0.0

    return taken + balance


def get_annual_leave(entry):
    """Returns the total annual leave"""
    return _calculate_leave(entry.get('annualLeaveTaken'), entry.get('annualLeaveBalance'))


def get_sick_leave(entry):
    """Returns the total sick leave"""
    return _calculate_leave(entry.get('sickLeaveTaken'), entry.get('sickLeaveBalance'))


def get_maternity_leave(entry):
    """Returns the total maternity leave"""
    return _calculate_leave(entry.get('maternityLeaveTaken'), entry.get('maternityLeaveBalance'))


def get_paternity_leave(entry):
    """Returns the total paternity leave"""
    return _calculate_leave(entry.get('paternityLeaveTaken'), entry.get('paternityLeaveBalance'))


def get_emergency_phone(entry):
    """Returns an emergency contact's phone number"""
    return entry.get('emergencyContactMobile', entry.get('emergencyContactPhone', ''))


def get_dependant_full_name(entry):
    """Returns a dependant's full name"""
    return _create_full_name(
        first_name=entry.get('dependentFirstName'),
        middle_name=entry.get('dependentMiddleName'),
        last_name=entry.get('dependentLastName'))


def get_formatted_salary(entry):
    """Returns the salary formatted"""
    salary = entry.get('salary', '').strip()
    return salary if re.match(r'[0-9]+', salary) else None


def get_validated_date(date_text):
    """Returns a formatted date"""
    if not date_text:
        return None

    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return date_text
    except ValueError:
        return None
