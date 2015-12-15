#!/usr/bin/env python3

import math
from xero import Xero
from xero.auth import PrivateCredentials
import pprint

def get_membership_list(xero):
  members = list()
  shame_list = list()

  contacts = xero.contacts.all()
  #for c in cs:
  #  print(c['Name'], c['AccountNumber'], c['ContactID'])
  
  # "ACCREC" means money in.  Status is only "AUTHORISED" or "DELETED".
  repeating_invoices = xero.repeatinginvoices.filter(Type="ACCREC", Status='AUTHORISED')  
  for ri in repeating_invoices:
    #if not ri['Contact']['Name'].startswith('Brendan'):
    #  continue
    print(ri['Contact']['Name'], ri['Reference'], ri['Contact']['ContactID'], ri['ID'], ri['RepeatingInvoiceID'])  

    # Look for a Contact that matches the one on the invoice
    try:
      c = next(x for x in contacts if x['ContactID'] == ri['Contact']['ContactID'])
    except StopIteration:
      print('Couldnt find a Contact for the Invoice with ID ', ri['InvoiceID'])
      continue

    # Xero doesn't return the Balances section for a Contact if all values are all zero.
    c_is_member = False
    if not 'Balances' in c or c['Balances']['AccountsReceivable']['Overdue'] > 0:
      c_is_member = True
    
    # A simplified Contact
    c_simple = {
        'Name': ri['Contact']['Name'],
        #'Reference': ri['Reference'],
        #'ContactID': ri['Contact']['ContactID'],
      }

    if c_is_member:
      members.append(c_simple)
    else:
      shame_list.append(c_simple)

  return {'members': members, 'shame_list': shame_list}

def initXero():
  with open("./credentials/privatekey.pem") as rsa_key_file, \
       open("./credentials/consumer_key") as consumer_key_file:
    rsa_key = rsa_key_file.read()
    consumer_key = consumer_key_file.read().strip()
    credentials = PrivateCredentials(consumer_key, rsa_key)
    return Xero(credentials)

def quorum(num_members):
  num_man_com = 5
  return num_man_com + math.ceil(0.25 * (num_members - num_man_com))

def main():
  xero = initXero()

  pp = pprint.PrettyPrinter(indent=4)
  

  membership_list = get_membership_list(xero)

  print('Members:')
  pp.pprint(membership_list['members'])
  print(len(membership_list['members']))
  print('quorum:', quorum(len(membership_list['members'])))

  print('Shame List:')
  pp.pprint(membership_list['shame_list'])
  print(len(membership_list['shame_list']))

if __name__ == "__main__":
    main()

