#!/usr/bin/env python3

from sys import argv
import ldap3

LDAPHOST='ldaps://ldappv.rwth-aachen.de'
LDAPBASE='ou=People,dc=rwth-aachen,dc=de'

FILTER='(mail=*)'
ATTRS=['cn', 'mail']

with ldap3.Connection(LDAPHOST, auto_bind=True) as conn:
    print('Searching ' + LDAPHOST + ' …')
    flt = '(&' + FILTER + '(|(mail=' + argv[1] + '*)(cn=' + argv[1] + '*)))'
    conn.search(LDAPBASE, flt, attributes=ATTRS)
    for i in conn.entries:
        for m in i.mail.values:
            print(m + '\t' + i.cn[0] + '\t' + i.entry_dn)
