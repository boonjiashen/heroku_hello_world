# Where the python module is hello.py and app is the python flask variable in the module
gunicorn -b 0.0.0.0:5000 hello:app  

#gunicorn hello:app  # if you don't want to specify host/port
