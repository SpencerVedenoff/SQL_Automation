import getpass
import oracledb

un = 'Username'
cs = 'IP/Database'
pw = getpass.getpass(f'Enter password for {un}@{cs}: ') #alternatively can use PSW in single quotes provided its not confidential

with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = """select sysdate from db"""
        for r in cursor.execute(sql):
            print(r)