## 如何优雅地重启线上服务之 Gunicorn + Django + Celery

### 优雅地重启 Gunicorn + Django

#### 测试代码

```markdown
* tests/test01.py | 针对一般接口
* tests/test02.py | 针对有 Celery 任务的接口
* tests/test03.py | 针对有数据库写入的接口
```

#### 测试结论

在测试代码的顶部注释中

#### 结论总结

一般情况下可以使用 `kill -HUP {gunicorn pid}` 来重启通过 Gunicorn 启动的 Django 服务，但是需要注意：
1. gunicorn pid 是主进程 pid
2. 项目中涉及到复杂数据库读写的部分要严格确保业务逻辑的原子性，该加锁加锁该上事务上事务

### 优雅地重启 Celery

进行中