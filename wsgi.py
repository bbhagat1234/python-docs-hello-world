from bb import application
gunicorn --bind=0.0.0.0 --worker-class gevent -w 1 app:app --access-logfile /var/log/gunicorn-access.log --error-logfile /var/log/gunicorn-error.log --log-level 'debug'
if __name__ == "__main__":
    application.run()
