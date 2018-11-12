#!/usr/bin/python3

import psycopg2

DBNAME = "news"


# Function definition is here
def printreport():
        # connect to databas
        conn = psycopg2.connect(database=DBNAME)

        # fetch data
        cur = conn.cursor()

        # 1. What are the most popular three articles of all time?
        qu = '''select articles.title, count(*) as visited from log
              join articles on articles.slug = split_part(log.path,'/',3)
              join authors on authors.id = articles.author
              where log.status = '200 OK'
              group by articles.title, authors.name
              order by visited desc
              limit 3;'''

        cur.execute(qu)
        rows = cur.fetchall()

        # print result
        print("--------------------------------------------------------")
        print("1. What are the most popular three articles of all time?\n")
        for row in rows:
            print('[' + row[0] + '] - ' + str(row[1]) + ' views')
        print("--------------------------------------------------------")

        # 2. Who are the most popular article authors of all time?
        qu = '''select authors.name, count(*) as visited from log
             join articles on articles.slug = split_part(log.path,'/',3)
             join authors on authors.id = articles.author
             where log.status = '200 OK'
             group by authors.name
             order by visited desc;'''
        cur.execute(qu)

        # print result
        print("2. Who are the most popular article authors of all time?\n")
        for row in cur:
            print(row[0] + ' - ' + str(row[1]) + ' views')
        print("--------------------------------------------------------")

        # 3. Which days did more than 1% of requests lead to errors??
        qu = '''select vwlogcount.onlydate,
             (elc.errors*100/num) as per from vwlogcount
             join vwerrorlogcount elc on elc.onlydate = vwlogcount.onlydate
             where elc.errors*100 >= vwlogcount.num;'''

        cur.execute(qu)
        rows = cur.fetchall()

        # print result
        print("3. which days did more than 1% of requests lead to errors?\n")
        for row in rows:
            print(str(row[0]) + ' - ' + str(row[1]) + '% errors')
        print("--------------------------------------------------------")

        # end connection
        cur.close()
        conn.close()


if __name__ == '__main__':
    printreport()
