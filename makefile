FILES :=                              						\
    .travis.yml                       						\
    models.html                       						\
    IDB.log                           						\
    models.py                         						\
    tests.py                          						\
	__init__.py						  						\
	config.py												\
	createDB.py												\
	index.html												\
	requirements.txt										\
	UML.pdf													\
	templates/about/about.html								\
	templates/games/games.html								\
	templates/players/players.html							\
	templates/teams/teams.html								\
	templates/shared/navbar.html							\
	static/vendors/angular.js		  						\
	static/vendors/bootstrap-3.3.5-dist/css/bootstrap.css 	\
	static/assets/javascript/app.js 						\
	static/assets/javascript/controllers/HomeCtrl.js		\
	static/assets/javascript/controllers/NavbarCtrl.js		\
	static/assets/javascript/controllers/TableCtrl.js		\
	static/assets/stylesheets/style.css						

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

test: tests.py
	python3 tests.py

	
