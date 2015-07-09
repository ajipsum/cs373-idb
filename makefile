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
	assets/templates/about/about.html								\
	assets/templates/games/games.html								\
	assets/templates/players/players.html							\
	assets/templates/teams/teams.html								\
	assets/templates/shared/navbar.html							\
	vendors/angular.js		  						\
	vendors/bootstrap-3.3.5-dist/css/bootstrap.css 	\
	assets/javascript/app.js 						\
	assets/javascript/controllers/HomeCtrl.js		\
	assets/javascript/controllers/NavbarCtrl.js		\
	assets/javascript/controllers/TableCtrl.js		\
	assets/stylesheets/style.css						

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

	
