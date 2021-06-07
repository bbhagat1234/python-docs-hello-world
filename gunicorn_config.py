bind = '0.0.0.0:8000'
workers: 2
worker_class: gevent
threads: 1
timeout: 600
graceful_timeout: 30
accesslog: /home/LogFiles/gunicorn-access.log
errorlog: /home/LogFiles/gunicorn-error.log
loglevel: debug
default_proc_name: app:app
