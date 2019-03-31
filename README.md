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

## Token 认证

```python
# https://www.cnblogs.com/ShenLw/p/8608136.htmlhttps://www.jianshu.com/p/e0a206212df4

```

## 逆向生成数据表,根据数据库生成models

```bash
python manage.py inspectdb > [appname]/models.py
```

忽略已提交到版本的文件
1.git rm -r --cached file_name/dir
2.添加到.gitignore中
3.提交、推送

## 共享虚拟环境

```bash
# linux
python3 -m vemv /home/snowman/.local/share/virtualenvs/django2.0

# windows
python -m vemv c://
```

## django 命令行使用

```bash
django-admin startproject [projectname]
python3 manage.py startapp [appname]

```

##　项目结构

app 拆分

## debug模式

## 请求参数获取

- 请求参数转换器

## url 模块化

```python
from django.urls import path,include
urlpatterns = [
    path('',include())
]

```
- url 命名
- url 反转
- url 应用app命名空间 ,在urls中定义 app_name 定义命名空间,反转url的时候
- url 实例命名空间 namespace, include('api.urls',namespace="api1")
- 指定实例命名空间必须提前指定应用命名空间
- include 函数方法 在include方法中指定应用命名空间和实例命名空间
- 重定向,带有参数的重定向
- 制定url参数默认参数

```python
from django.urls import include,reverse
include('api.urls','api')
path = reverse('应用命名空间:视图函数名称')
```

- re_path

```python
from django.urls import re_path
# re_path,在urls中写正则
```

## 自定义 path 转换器

- 针对url参数做修改