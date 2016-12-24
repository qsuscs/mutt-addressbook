#!/usr/bin/env python3

try:
    from sys import argv
    import ldap3

    LDAPDIRS=[('ldaps://ldappv.rwth-aachen.de', 'ou=People,dc=rwth-aachen,dc=de')]

    FILTER='(mail=*)'
    ATTRS=['cn', 'mail']

    print('Searching … ', end='', flush=True)
    entries = []
    for d in LDAPDIRS:
        with ldap3.Connection(d[0], auto_bind=True) as conn:
            print(d[0] + ' … ', end='', flush=True)
            flt = '(&' + FILTER + '(|(mail=' + argv[1] + '*)(cn=' + argv[1] + '*)))'
            conn.search(d[1], flt, attributes=ATTRS)
            entries.extend(conn.entries)

    if len(entries) == 0:
        print('No entries found!')
        exit(1)

    print(str(len(entries)) + ' entries found!')
    for i in entries:
        for m in i.mail.values:
            print(m + '\t' + i.cn[0] + '\t' + i.entry_dn)

except Exception as e:
    print("Error: " + type(e).__name__ + ": " + str(e))
    exit(1)
