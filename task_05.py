#!/usr/bin/env python

"""task_05.py: Homework Task 5."""
from decimal import Decimal

__author__ = "Joe Graham"

# constants
HEADER_REPORT = 'Loan Report for: {}'
HEADER_DIV = '--------------------------------------------------------------------'
LINE_PRINCIPAL = "Principal:\t\t\t{:>20}"
LINE_DURATION = "Duration:\t\t\t{:>20}"
LINE_PREQUAL = "Pre-qualified?:\t\t{:>20}"
LINE_TOTAL = "Total:\t\t\t\t{:>20}"
INVALID_ENTRY = "Invalid entry, please try again."
LABELS = {
    'name': 'What is your name?',
    'principal': 'What is the whole dollar amount of your principal (the amount being borrowed)?',
    'duration': 'For how many years is this loan being borrowed?',
    'prequal': 'Are you pre-qualified for this loan?'

}
PQ_ENUM = {
    'y': 'Yes',
    'n': 'No'
}
FIELDS = [
    {
        'key': 'name',
        'type': 'string'
    },
    {
        'key': 'principal',
        'type': 'int'
    },
    {
        'key': 'duration',
        'type': 'int'
    },
    {
        'key': 'prequal',
        'type': 'enum',
        'values': ['y', 'n']
    }
]
RATES = [
    {
        'prequal': 'yes',
        'minterm': 0,
        'term': 15,
        'min': 0,
        'max': 199999,
        'rate': 3.63
    },
    {
        'prequal': 'yes',
        'minterm': 0,
        'term': 15,
        'min': 200000,
        'max': 999999,
        'rate': 3.02
    },
    {
        'prequal': 'yes',
        'minterm': 0,
        'term': 15,
        'min': 1000000,
        'max': None,
        'rate': 2.05
    },
    {
        'prequal': 'yes',
        'minterm': 15,
        'term': 20,
        'min': 0,
        'max': 199999,
        'rate': 4.04
    },
    {
        'prequal': 'yes',
        'minterm': 15,
        'term': 20,
        'min': 200000,
        'max': 999999,
        'rate': 3.27
    },
    {
        'prequal': 'yes',
        'minterm': 15,
        'term': 20,
        'min': 1000000,
        'max': None,
        'rate': 2.62
    },
    {
        'prequal': 'yes',
        'minterm': 20,
        'term': 30,
        'min': 0,
        'max': 199999,
        'rate': 5.77
    },
    {
        'prequal': 'yes',
        'minterm': 20,
        'term': 30,
        'min': 200000,
        'max': 999999,
        'rate': 4.66
    },
    {
        'prequal': 'no',
        'minterm': 0,
        'term': 15,
        'min': 0,
        'max': 199999,
        'rate': 4.65
    },
    {
        'prequal': 'no',
        'minterm': 0,
        'term': 15,
        'min': 200000,
        'max': 999999,
        'rate': 3.98
    },
    {
        'prequal': 'no',
        'minterm': 15,
        'term': 20,
        'min': 0,
        'max': 199999,
        'rate': 4.98
    },
    {
        'prequal': 'no',
        'minterm': 15,
        'term': 20,
        'min': 200000,
        'max': 999999,
        'rate': 4.08
    },
    {
        'prequal': 'no',
        'minterm': 20,
        'term': 30,
        'min': 0,
        'max': 199999,
        'rate': 6.39
    }
]

# members
# isNameValid, isAmountValid, isDurationValid, isPQValid = False
isInputComplete = False
TOTAL = 0
REPORT = ''
valueObject = {}
fieldIdx = 0
while not isInputComplete:
    field = FIELDS[fieldIdx]
    fieldName = field['key']
    fieldType = field['type']
    print LABELS[fieldName]
    s = raw_input()
    #print "s: " + s
    if fieldType == 'string':
        if s is not None and not '' == s.strip():
            valueObject[fieldName] = s
        else:
            print INVALID_ENTRY
            continue
    elif fieldType == 'enum':
        if s.lower()[0:1] in field['values']:
            valueObject[fieldName] = PQ_ENUM[s.lower()[0:1]]
        else:
            try:
                boolVal = bool(s)
                pqKey = 'y' if boolVal else 'n'
                valueObject[fieldName] = PQ_ENUM[pqKey]
            except ValueError:
                print INVALID_ENTRY
                continue
    else:
        try:
            numVal = int(s)
            valueObject[fieldName] = numVal
        except ValueError:
            print INVALID_ENTRY
            continue
    fieldIdx += 1
    if fieldIdx >= len(FIELDS):
        isInputComplete = True

rateList = []
borrower = valueObject['name']
prequal = valueObject['prequal']
principal = valueObject['principal']
duration = valueObject['duration']
pqCompare = prequal.lower()[0:1]
for elem in RATES:
    pqVal = elem['prequal'].lower()[0:1]
    if (pqVal == pqCompare and
            duration > elem['minterm'] and
                duration <= elem['term'] and
                    principal >= elem['min']):
        if elem['max'] is not None:
            if principal <= elem['max']:
                rateList.append(elem)
            else:
                continue
        else:
            rateList.append(elem)
rateObj = {}
if len(rateList) <= 0:
    TOTAL = None
else:
    rateObj = rateList[0]
if TOTAL is not None:
    r = rateObj['rate']
    dec_r = Decimal(r) / 100
    TOTAL = int(round(principal * ((1 + (dec_r / 12)) ** (12 * duration))))
totalStr = 'None' if TOTAL is None else '$' + '{:,.2f}'.format(TOTAL)
REPORT += '\n'
REPORT += HEADER_REPORT.format(borrower) + '\n'
REPORT += HEADER_DIV + '\n'
REPORT += '\n'
REPORT += '\t' + LINE_PRINCIPAL.format('$' + '{:,.2f}'.format(principal)) + '\n'
REPORT += '\t' + LINE_DURATION.format(duration) + '\n'
REPORT += '\t' + LINE_PREQUAL.format(prequal) + '\n'
REPORT += '\n'
REPORT += '\t' + LINE_TOTAL.format(totalStr) + '\n'
print REPORT