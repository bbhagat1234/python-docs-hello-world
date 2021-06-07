bind = '0.0.0.0:8000'
workers: 2
worker_class: gevent
threads: 1
worker_connections: 1000
max_requests: 0
max_requests_jitter: 0
timeout: 30
graceful_timeout: 30
keepalive: 2
limit_request_line: 4094
limit_request_fields: 100
limit_request_field_size: 8190
accesslog: /var/log/gunicorn-access.log
errorlog: /var/log/gunicorn-error.log
loglevel: debug
default_proc_name: app:app
