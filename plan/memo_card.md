- Mysql
  - 坑
    - NULL <> 1 -> false
  - Control Flow Functions
    - CASE
    - IF
    - IFNULL
    - NULLIF
      - STRCMP
  - utf8mb4_unicode_ci 速度上比 utf8mb4_general_ci 慢百分之十，但排序更精确
  - `ALTER TABLE tableName CHANGE "oldcolname" "newcolname" datatype(length);`
  - `SET FOREIGN_KEY_CHECKS = 0;` 关闭外键检查
  - 影响行数
    - FOUND_ROWS() : select 
    - ROW_COUNT()  : update delete insert
  - function
    - LOWER()
    - TRIM()
  - time
    - DATE_FORMAT(now(), '%Y-%m-%d')
    - UNIX_TIMESTAMP(now())
    - UNIX_TIMESTAMP('2016-01-02')
    - STR_TO_DATE('2016-01-02', '%Y-%m-%d')
    - FROM_UNIXTIME(1451997924)
    - FROM_UNIXTIME(1451997924,'%Y-%d')
  - json 类型字段长度的限制
    - `set global max_allowed_packet=999`
    - `mysql --max_allowed_packet=999`
  - mysql 架构
    - 锁
      - 读写锁
        - 读锁:共享锁
        - 写锁:排他锁(有可能插入读锁前面)
      - 锁粒度
        - 表锁
        - 行级锁
    - 事务
      - ACID
        - 原子性(atomicity)
        - 一致性(consistency)
        - 隔离性(isolation)
        - 持久性(durability)
      - AUTOCOMMIT 如果为 1,则每一句都是一个事务 `SHOW VARIABLES LIKE 'AUTOCOMMIT'`
      - 在执行 DDL 或 `LOCK TABLES` 时会强制执行 `COMMIT` 提交当前事务
    - 隔离级别
      - 四种
        - READ UNCOMMITTED(未提交读) 可能脏读
        - READ COMMITTED(提交读) 同一个事务执行两次相同的查询，结果可能不一样
        - REPEATABLE READ(可重复读) 同一个事务执行两次相同的查询，结果一样，但是可能幻读 todo 幻读?
        - SERIALIZABLE(可串行读) 强制串行执行
      - `SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;`
      - 查看隔离级别
        - `SELECT @@tx_isolation;`
        - `SELECT @@global.tx_isolation;`
    - 死锁
      - InnoDB 处理死锁的方法:将持有最少行级排他锁的事务进行回滚
    - 显式指定锁
      - `select ... lock in share mode` 上的是共享锁,不允许其它事务对此行 update,但是不能阻止其它事务对此行上共享锁
      - `select ... for update` 会把本句当成 update 语句一样持有锁,上的是排他锁
    - MVCC 多版本并发控制,大都实现了非阻塞的读操作,写操作也只锁定必要的行
      - 是在每一行上加额外的两列来实现的,一列是该行的创建时刻,另一列是删除时刻,这里的时刻其实是一个版本号,每开始一个新事务,就会有一个新的版本号
      - REPEATABLE READ 下,MVCC 如何工作
        - SELECT 只选创建版本号小于等于事务版本号且删除版本号大于事务版本号或为空的行
        - INSERT 创建版本号为"当前系统"版本号
        - DELETE 删除版本号为"当前系统"版本号
        - UPDATE 相当于 DELETE 老的,INSERT 新的
      - MVCC 只在 READ COMMITTED 和 REPEATABLE READ 下生效
  - trigger
    - 注意事项
      - trigger 应该是紧接 Event on Table 的单语句事务,而不能依赖多语句事务
      - 当报错报的莫名奇妙时,很有可能是 trigger 写错了
  - time_zone
    - `SHOW Variable like '%time_zone%'`
    
- Git
  - `git rebase -i <commit>` 把要合并的改为`squash`
  - `git reset`
    - `--hard` 齐头切
    - `--mixed` 切最外层和中间层，保留最内层
    - `--soft` 切最外层，保留中间层和最内层 (可以用作合并 commit)
  - `git commit -a` = `git add -U` 加 `git commit`

- ES
  - `GET /_cat/indices?v` List All indices
  - document 增删改查
    - `PUT /{index}/{type}/{id}` 新增或更新 document,新增时也可以不要 id
      - 保证是新增 `?op_type=create` or `/_create`
        - 201 Created: 创建成功
        - 409 Conflict: 冲突
      - 版本控制
        - `?version=1` 只希望 document 的 _version 是 1 时更新才生效
        - `?version=5&version_type=external` 使用外部版本号,版本号小于 5 的文档才能被更新 
      - 局部更新 `?/_update`
        - ` -d {"doc": {"key1": 1, "key2": 2}}` 存在的标量字段被覆盖,新字段被添加
        - 使用 Groovy 脚本
          - ` -d {"script": "ctx._source.views+=1"}`
          - ` -d {"script": "ctx._source.views+=1", "upsert": {"views": 1}}` 等于`INSERT ... ON DUPLICATE KEY UPDATE`
          - ` -d {"script": "ctx._source.tags+=new_tag", "params": {"new_tag": "a"}}` tags 是数组
          - `?retry_on_conflict=5 -d {"script": "ctx._source.views+=1", "upsert": {"views": 0}}` 在发生错误前重试5次,默认值为0 todo 为0?
    - `GET /{index}/{type}/{id}` 按 id 查询 document
      - `/?pretty` 以更美的格式返回结果
      - `/?_source={key1},{key2}` 只返回 key1,key2 字段 
      - `/_source` 只返回 _source 部分
    - `HEAD /{index}/{type}/{id}` 按 id 查询 document 是否存在
    - `DELETE /{index}/{type}/{id}` 删除,注意即使没找到 _version 也会增加，确保在多节点间正确的操作顺序
      - 200 OK: {"found": true}
      - 404 Not Found: {"found": false}
    - _mget
      - `GET /_mget` -d
        - ```js
          {
            "docs": [
              {
                "_index": "website",
                "_type": "blog",
                "_id": 2
              },
              {
                "_index": "website",
                "_type": "pageviews",
                "_id": 1,
                "_source": "views"
              }
            ]
          }
          ```
      - `GET /website/blog/_mget` -d
        - ```js
          {
            "docs" : [
              { "_id" : 2 },
              { "_type" : "pageviews", "_id" :   1 }
            ]
          }
          ```
        - `{"ids": ["2", "1"]}`
    - 搜索 `/_search`
      - 空搜索 `GET /_search`
      - 多索引多类别
        - `/{index1},{index2},{3*}/{type1},{type2}/_search`
        - `/_all/{type1},{type2}/_search`
      - 限时 `?timeout=10ms`
      - 分页 `?size=10&from=20`