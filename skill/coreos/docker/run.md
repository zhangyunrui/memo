### 指定ip
  - 使用`--ip`，且必须满足两个条件：
    - `--network foo`，foo必须是自己手动创建的
    - 创建foo时要指定`--subnet`，否则不能保证此子网的stable，从而不能指定ip