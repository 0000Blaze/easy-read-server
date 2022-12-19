import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = 'unix:flaskrest.sock'
umask = 0o007
reload = True
timeout = 900

#logging
accesslog = '-'
errorlog = '-'
