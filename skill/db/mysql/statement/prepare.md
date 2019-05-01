- 组合字符串然后执行字符串
```mysql
SET @s = "xxx";
SET @ss = concat("xx ?", @s);
SET @a = 10;
PREPARE stmt FROM @ss;
EXECUTE stmt USING @a;
DEALLOCATE PREPARE stmt;
```