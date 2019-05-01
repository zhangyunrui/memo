- 基本命令
```python
# coding: utf-8
import logging
# 创建名为'spam_application'的记录器
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

# 创建级别为DEBUG的日志处理器
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

# 创建级别为ERROR的控制台日志处理器
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# 创建格式器，加到日志处理器中
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
```
- 在日志中传入上下文信息
  - 使用适配器传递上下文信息

