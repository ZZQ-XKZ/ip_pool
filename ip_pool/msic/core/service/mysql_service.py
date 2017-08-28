import MySQLdb

def get_pool(host:str,db:str,user:str,passwd:str):
    db = MySQLdb.connect(host=host,    # your host, usually log                     
                    user=user,         # your username
                    passwd=passwd,  # your password
                    db=db)        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    return db


def excuate_sql(db,sql):
    print(sql.encode('utf-8'))
    cur=db.cursor()
    try:
        cur.execute(sql)
        db.commit()
    except Exception as e:
        print("rollback:"+e)
        db.rollback()
        return
    return cur.fetchall()
