## ascii
> ascii(美国信息交换标准代码,American Standard Code for Information Interchange,是基于拉丁字母的一套编码系统,范围[0, 127], [128, 255]为扩展字符集)
## unicode
> unicode字符集(通用多八位编码字符集, Universal Multiple-Octet Coded Character Set, 简称UCS. 此时字符集和编码规则开始区分开来. 
范围17\*2\*\*16 = 17\*65536,每种语言的每个字符都有统一且唯一的二进制编码)

> unicode编码(utf-8和utf-16等具体编码方案的统称)

在计算机内存中,统一使用unicode编码,当需要存入硬盘或传输时,通过encode转换为utf-8编码.

e.g.'报'
* unicode: '\u62a5' (16进制),01100010 10100101 (2进制),25253 (10进制)
* utf-8: '&#x62A5;', '\xe6\x8a\xa5' (16进制),1110`0110` 10`001010` 10`100101` (2进制字节码)
* python2:
  * '报'.decode('utf-8') = unicode('报', 'utf-8') --> u'\u62a5'
  * u'报'.encode('utf-8') --> '\xe6\x8a\xa5'
* python3:
  * b'\xe6\x8a\xa5'.decode('utf-8') --> '报' 
  * '报'.encode('utf-8') = bytes('报', 'utf-8') --> b'\xe6\x8a\xa5'
  * ord('报') --> 25253
  * chr(25253) --> '报'
## other
> ANSI(美国国家标准协会, American National Standards Institute, 通常指的是平台默认编码, 例如英文是ISO-8859, 中文是GBK)

> GB2312(中国国家标准字符编码, 两个英文字符为一个中文字符, 两个字节均为大于127)

> GBK(第二个字节允许小于128)

> DBSC(双字节字符集, Double Byte Character Set)
