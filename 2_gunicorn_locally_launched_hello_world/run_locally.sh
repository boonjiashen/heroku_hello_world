gunicorn -b 0.0.0.0:5000 hello:app
#gunicorn hello:app  # if you don't want to specify host/port
