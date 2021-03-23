```shell
pyinstaller -F ./main.py --additional-hooks-dir ./extra-hooks
```

国税网站做了selenium控制，所以采用chrome remote debug 模式

some code copy from [半自动国税发票查验]

[半自动国税发票查验]: https://github.com/Snowing-ST/Invoice-Checking