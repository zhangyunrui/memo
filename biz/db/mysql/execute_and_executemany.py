# coding: utf-8
"""
结论：当次数为 1000 时:
executemany: 0.05
execute: 0.05
update executemany: 8.19
update execute: 0.92

结论：当次数为 1000 时且有主键时:
executemany: 0.06
execute: 0.05
update executemany: 7.48
update execute: 0.15

结论：当次数为 10000 时:
executemany: 0.46
execute: 0.58
update execute: 0.65

结论：当次数为 100000 时:
executemany: 1.93/1.84
execute: 1.94/1.81
update execute: 2.45/2.39

总结：insert 时，分条执行和一次执行时间相差无几，而 update 时，批量执行会比分条执行快 10-50 倍。
新建虚拟表，先批量插入然后通过 join 批量 update 是一个很可行的解决办法。
另外，join 的时候如果是用主键或索引作为桥梁，速度会比不用要快 6 倍左右。
"""
import time

import itertools
from torndb import Connection

main_mysql = Connection(
    "127.0.0.1",
    "dev_cn_db_console",
    "xxxx",
    "xxxx"
)

TIMES = 100000


def main():
    main_mysql.execute("""DROP TABLE IF EXISTS `episodes_duration`;""")
    main_mysql.execute("""
    CREATE TABLE `episodes_duration` (
      `id` char(36) NOT NULL,
      `duration` int(10) unsigned NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;""")

    begin = time.time()
    main_mysql.executemany("""INSERT `episodes_duration` VALUES (%s, %s);
    """, [(i, i) for i in range(TIMES)])
    print("executemany: %.2f" % (time.time() - begin))

    main_mysql.execute("""TRUNCATE TABLE `episodes_duration`""")
    begin = time.time()
    sql = """INSERT `episodes_duration` VALUES %s;
    """ % ','.join(['(%s, %s)' for i in range(TIMES)])
    main_mysql.execute(sql, *list(itertools.chain.from_iterable(
        [(i, i) for i in range(TIMES)])))
    print("execute: %.2f" % (time.time() - begin))

    # begin = time.time()
    # main_mysql.executemany("""
    # UPDATE episodes_duration SET duration = %s WHERE id = %s;
    # """, [(i, TIMES - i) for i in range(TIMES)])
    # print("update executemany: %.2f" % (time.time() - begin))
    # rows = main_mysql.query("""
    # SELECT * FROM episodes_duration LIMIT 10;""")
    # print (rows)

    begin = time.time()
    main_mysql.execute("""DROP TABLE IF EXISTS `episodes_duration_bak`;""")
    main_mysql.execute("""
    CREATE TABLE `episodes_duration_bak` (
      `id` char(36) NOT NULL,
      `duration` int(10) unsigned NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;""")
    sql = """INSERT `episodes_duration_bak` VALUES %s;
    """ % ','.join(['(%s, %s)' for i in range(TIMES)])
    main_mysql.execute(sql, *list(itertools.chain.from_iterable(
        [(i, i) for i in range(TIMES)])))
    sql = """
    UPDATE episodes_duration AS e
      JOIN episodes_duration_bak AS d ON e.id = d.id
    SET e.duration = d.duration;"""
    main_mysql.execute(sql)
    main_mysql.execute("""DROP TABLE IF EXISTS `episodes_duration_bak`;""")
    print("update execute: %.2f" % (time.time() - begin))
    rows = main_mysql.query("""
    SELECT * FROM episodes_duration LIMIT 10;""")
    print (rows)

    main_mysql.execute("""DROP TABLE IF EXISTS `episodes_duration`;""")


if __name__ == '__main__':
    main()
