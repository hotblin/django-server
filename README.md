# django-server

## 跨域请求

## 类视图 CBV

## CSRF Token相关装饰器在CBV中的使用

CSRF Token相关装饰器在CBV只能加到dispatch方法上，
或者加在视图类上然后name参数指定为dispatch方法

## CSRF

- csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置全局中间件。
- csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了全局中间件。

## 请求方式拦截

```python
from django.views.decorators.http import require_GET,require_POST,require_safe
# require_GET() - 声明被装饰的视图仅支持GET方法
# require_POST() - 声明被装饰的视图仅支持POST方法
# require_SAFE() - 声明被装饰的视图仅支持GET和HEAD方法
```

## 新建表

```shell
# 可选，生成空记录文件在 `migrations` 目录下
python manage.py makemigrations --empty [appname] 

# 数据库迁移
python manage.py makemigrations [appname]

# 从记录文件写入到数据库
python manage.py migrate [appname] [记录文件id] 
```
#在api应用下新生成``目录以及初始化文件

models写入到记录文件： `` 
从记录文件写入到数据库： ``



## Token 认证

```python
# https://www.cnblogs.com/ShenLw/p/8608136.htmlhttps://www.jianshu.com/p/e0a206212df4

```