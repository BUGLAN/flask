## flask 源码解析

> 兴趣使然的源码解析

## _PackageBoundObject

用于绑定类属性, 在`Flask`和`Blueprint`这两个类都有使用到

重要代码
```python
_PackageBoundObject.__init__(
            self,
            import_name,
            template_folder=template_folder,
            root_path=root_path
        )
```

## Flask 类

### Flask.run()


关键代码

```python
def wsgi_app(self):
    ctx = self.request_context(environ)
    error = None
    try:
        try:
            ctx.push()
            response = self.full_dispatch_request()
        except Exception as e:
            error = e
            response = self.handle_exception(e)
        except:
            error = sys.exc_info()[1]
            raise
        return response(environ, start_response)
    finally:
        if self.should_ignore_error(error):
            error = None
        ctx.auto_pop(error)
```

一行一行解释:

`ctx = self.request_context(environ)`


> flask wsgi server 启动器


## wsgi

wsgi server gateway

wsgi application / framework


## Response


## Request