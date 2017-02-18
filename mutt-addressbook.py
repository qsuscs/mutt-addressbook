#!/usr/bin/env python3

try:
    from sys import argv
    import configparser
    import os
    import ldap3

    config = configparser.ConfigParser()
    config.read(['config.ini', os.path.expanduser('~/.mutt-addressbook.ini')])

    FILTER = '(mail=*)'
    ATTRS = ['cn', 'mail']

    print('Searching … ', end='', flush=True)
    entries = []
    for d in config:
        if d == 'DEFAULT':
            continue
        with ldap3.Connection(config[d]['URI'], auto_bind=True) as conn:
            print(''.join((d, ' … ')), end='', flush=True)
            flt = '(&{0}(|(mail={1}*)(cn={1}*)(sn={1}*)(givenName={1}*)))'.format(FILTER, argv[1])
            conn.search(config[d]['Base'], flt, attributes=ATTRS)
            entries.extend(conn.entries)

    if len(entries) == 0:
        print('No entries found!')
        exit(1)

    print('{:d} entries found!'.format(len(entries)))
    for i in entries:
        for m in i.mail.values:
            print('{}\t{}\t{}'.format(m, i.cn[0], i.entry_dn))

except Exception as e:
    print('Error: {}: {}'.format(type(e).__name__, e))
    exit(1)
