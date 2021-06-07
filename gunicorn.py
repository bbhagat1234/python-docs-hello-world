bind = '0.0.0.0:8000'
workers: 1
worker_class: gevent
threads: 1
timeout: 600
graceful_timeout: 30
keepalive: 2
accesslog: /var/log/gunicorn-access.log
errorlog: /var/log/gunicorn-error.log
loglevel: debug
default_proc_name: app:app
