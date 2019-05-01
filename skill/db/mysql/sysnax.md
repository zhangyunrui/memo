- GROUP_CONCAT
```mysql
SELECT GROUP_CONCAT(tb.col1 ORDER BY tb.col2) FROM tb;
```

- VIEW
```mysql
CREATE VIEW v AS SELECT qty, price, qty*price AS value FROM t;
```

- LOAD FROM FILE
```mysql
load data infile 'D:/Python workspace/user.txt' 
into table user(username, salt, pwd)
```