FILES :=                              						\
    .travis.yml                       						\
    models.html                       						\
    IDB.log                           						\
    models.py                         						\
    tests.py                          						\
	__init__.py						  						\
	index.html						  						\
	static/vendors/angular.js		  						\
	static/vendors/bootstrap-3.3.5-dist/css/bootstrap.css 	\
	static/assets/javascript/app.js 						\
	static/assets/javascript/controllers/HomeCtrl.js

all:

check:
	@for i in $(FILES);                                         \
    do                                                          \
        [ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; \
    done

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  IDB.html
	rm -f  IDB.log
	rm -rf __pycache__

config:
	git config -l

models.html: models.py
	pydoc3 -w models

IDB.log:
	git log > IDB.log
