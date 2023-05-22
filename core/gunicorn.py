import multiprocessing

# ip + port
bind = "0.0.0.0:8000"

# 超时时间
timeout = 60

# 并行工作进程数
workers = multiprocessing.cpu_count() * 2
threads = 4

# 服务器中在 pending 状态的最大连接数 (建议 64-2048)
backlog = 2048

# sync 同步 | eventlet 并发 | gevent 协程, | tornado, gthread
# worker_class = "uvicorn.workers.UvicornWorker"

# 以守护进程形式运行：后台运行
daemon = True

# 设置进程文件目录
pidfile = 'gunicorn.pid'

# 设置访问日志和错误信息日志路径
errorlog = 'error.log'
accesslog = 'access.log'

# 设置日志记录水平
loglevel = 'info'
