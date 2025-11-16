import sys
import io
import simple_add

# 强制标准输出使用 UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print(simple_add.__doc__)
print(simple_add.add(10, 3.5))
result = simple_add.hello("你好嘛")
print(result)
help(simple_add.add)