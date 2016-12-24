#!/usr/bin/env python3

try:
    from sys import argv
    import ldap3

    LDAPHOST='ldaps://ldappv.rwth-aachen.de'
    LDAPBASE='ou=People,dc=rwth-aachen,dc=de'

    FILTER='(mail=*)'
    ATTRS=['cn', 'mail']

    with ldap3.Connection(LDAPHOST, auto_bind=True) as conn:
        print('Searching ' + LDAPHOST + ' … ', end='', flush=True)
        flt = '(&' + FILTER + '(|(mail=' + argv[1] + '*)(cn=' + argv[1] + '*)))'
        conn.search(LDAPBASE, flt, attributes=ATTRS)
        if len(conn.entries) == 0:
            print('No entries found!')
            exit(1)
        print()
        for i in conn.entries:
            for m in i.mail.values:
                print(m + '\t' + i.cn[0] + '\t' + i.entry_dn)
except Exception as e:
    print("Error: " + type(e).__name__ + ": " + str(e))
    exit(1)
