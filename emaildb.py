import sqlite3

conn = sqlite3.connect('maildb.sqlite')
attention = conn.cursor()

attention.execute('DROP TABLE IF EXISTS etable')

attention.execute('CREATE TABLE etable (email TEXT, count INTEGER)')

filename = input('ENTER FILE NAME:')
if (len(filename) < 1):
    filename = 'mailer.txt'
    filehandle = open(filename)
for subject in filehandle:
    if not subject.startswith('From: '): continue
    specific = subject.split()
    email = specific[1]
    attention.execute('SELECT count FROM etable WHERE email = ?', (email,))
    record = attention.fetchone()

    if record is None:
        attention.execute('INSERT INTO etable (email, count) VALUES ( ?, 1)', (email,))
    else:
        attention.execute('UPDATE etable SET count = count + 1 WHERE email = ? ', (email,))
conn.commit()

sqlcom = 'SELECT email, count FROM etable ORDER BY count DESC LIMIT 10'
for record in attention.execute(sqlcom):
    print(str(record[0]), record[1])
attention.close()
