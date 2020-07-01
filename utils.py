"""Utils to format the report"""
# -*- coding: utf-8 -*-
from collections import OrderedDict
from formatters import get_full_name, get_address, get_annual_leave, get_sick_leave, \
    get_maternity_leave, get_paternity_leave, get_emergency_phone, \
    get_dependant_full_name, get_formatted_salary, get_validated_date

# Map the fields in the CSV to the fields in the report
CSV_FIELDS_TO_REPORT = {
    'id': 'id',
    'employeeNumber': 'employeeNumber',
    'firstName': 'firstName',
    'middleName': 'middleName',
    'lastName': 'lastName',
    'startDate': 'employeeStatusDate',
    'jobTitle': 'jobTitle',
    'department': 'department',
    'salary': 'payRate',
    'annualLeaveTaken': '4415.4',
    'annualLeaveBalance': '4415.7',
    'sickLeaveTaken': '4418.4',
    'sickLeaveBalance': '4418.7',
    'maternityLeaveTaken': '4436.4',
    'maternityLeaveBalance': '4436.7',
    'paternityLeaveTaken': '4464.4',
    'paternityLeaveBalance': '4464.7',
    'addressLines': '-23',
    'cityState': '-28',
    'country': 'country',
    'emergencyContactName': '158',
    'emergencyContactRelationship': '160',
    'emergencyContactPhone': '159',
    'emergencyContactMobile': '693',
    'birthDate': 'dateOfBirth',
    'dependentFirstName': '1923',
    'dependentMiddleName': '1925',
    'dependentLastName': '1924',
    'dependentRelationship': '1926',
    'dependentGender': '1927',
    'dependentBirthDate': '1928',
    'bankAddress': '4410.0',
    'bankName': '4402.0',
    'bankAccountHolder': '4401.0',
    'bankAccountNumber': '4404.0',
    'bankAccountIban': '4405.0',
    'bankSwift': '4408.0',
}

REPORT_TO_CSV_FIELDS = {val: key for key, val in CSV_FIELDS_TO_REPORT.items()}

OMITTED_FIELDS = [
    'id', 'firstName', 'middleName', 'lastName',
    'annualLeaveTaken', 'annualLeaveBalance',
    'sickLeaveTaken', 'sickLeaveBalance',
    'maternityLeaveTaken', 'maternityLeaveBalance',
    'paternityLeaveTaken', 'paternityLeaveBalance',
    'emergencyContactPhone', 'emergencyContactMobile',
    'dependentFirstName', 'dependentMiddleName', 'dependentLastName',
]

CALCULATED_FIELDS = {
    'fullName': get_full_name,
    'address': get_address,
    'annualLeave': get_annual_leave,
    'sickLeave': get_sick_leave,
    'maternityLeave': get_maternity_leave,
    'paternityLeave': get_paternity_leave,
    'emergencyPhone': get_emergency_phone,
    'dependentFullName': get_dependant_full_name,
    'salary': get_formatted_salary,
    'startDate': lambda e: get_validated_date(e.get('startDate')),
    'birthDate': lambda e: get_validated_date(e.get('birthDate')),
    'dependentBirthDate': lambda e: get_validated_date(e.get('dependentBirthDate')),
}

ORDERED_FIELDS = [
    'employeeNumber',
    'fullName',
    'startDate',
    'jobTitle',
    'department',
    'salary',
    'annualLeave',
    'sickLeave',
    'maternityLeave',
    'paternityLeave',
    'address',
    'emergencyContactName',
    'emergencyContactRelationship',
    'emergencyContactPhone',
    'emergencyContactMobile',
    'birthDate',
    'dependentFullName',
    'dependentRelationship',
    'dependentGender',
    'dependentBirthDate',
    'bankAddress',
    'bankName',
    'bankAccountHolder',
    'bankAccountNumber',
    'bankAccountIban',
    'bankSwift',
]

def map_report_fields(row):
    """Maps the employee's information to our usable fields"""
    mapped = {}

    for field_id, field_value in row.items():
        key = REPORT_TO_CSV_FIELDS[field_id]
        mapped[key] = field_value

    return mapped


def get_employee_entry(row):
    """Returns an entry for the """
    # map the field values according to the mapping above
    row = map_report_fields(row)

    entry = OrderedDict()

    for field in ORDERED_FIELDS:
        value = ''

        if field in CALCULATED_FIELDS:
            value = CALCULATED_FIELDS[field](row)
        elif field in row:
            value = row[field]

        entry[field] = value

    return entry


def filter_empty_values_from_entry(entry):
    """Filters the empty values from the dependent entries"""
    return OrderedDict({key: value if value else None for key, value in entry.items()})


def remove_employee_number(entry):
    """Removes employee number from rows"""
    entry['employeeNumber'] = None
    return entry


def order_employee_entries(entries):
    """
    Orders an employee’s entries, first by the main entry that contains
    the employee’s information and then by the dependents
    """
    main = None
    additionals = []

    for entry in entries:
        if entry.get('fullName'):
            main = entry
        else:
            additionals.append(filter_empty_values_from_entry(entry))

    return [main, *[remove_employee_number(e) for e in additionals]]
