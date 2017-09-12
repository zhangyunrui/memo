# coding: utf-8
from other.db.mysql import MysqlDBPool

pool = MysqlDBPool(**dict(
    host="127.0.0.1",
    port=3306,
    db="dev_cn_db_console",
    user="root",
    passwd="pabb"
))  # todo 写入yaml

with pool.connection() as cursor:
    cursor.execute("SELECT * FROM cs_admin;")
    print(cursor.fetchone())
