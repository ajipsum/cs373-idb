var app = angular.module('api2k15', [
    'ngTouch',
    'ui.grid',
    'ui.router',
    'ui.grid.pagination'    
]);

app.config(function($interpolateProvider, $stateProvider, $urlRouterProvider, $locationProvider) {
    app.constant('Host', 'http://127.0.0.1:5000');

    $urlRouterProvider.otherwise('/home');
    $locationProvider.html5Mode(true);

    $stateProvider
        .state('root', {
            url: '',
            abstract: true,
            views: {
                'navbar': {
                    templateUrl: 'assets/templates/shared/navbar.html',
                    controller: 'NavbarCtrl'
                }
               // 'footer': {
               //     templateUrl: 'assets/templates/shared/footer.html',
               //     controller: 'FooterCtrl'
               // }
            }
        })
        .state('root.home', {
            url: "/home",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/home.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.teams', {
            url: "/teams",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/teams/teams.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.players', {
            url: "/players",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/players/players.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.games', {
            url: "/games",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/games/games.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.about', {
            url: "/about",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/about/about.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.lac', {
            url: "/lac",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/teams/LAC.html",
                    controller: "TableCtrl"
                }
            }

        })
        .state('root.mia', {
            url: "/mia",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/teams/MIA.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.sas', {
            url: "/sas",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/teams/SAS.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.bg', {
            url: "/bg",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/players/BG.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.dw', {
            url: "/dw",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/players/DW.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.td', {
            url: "/td",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/players/TD.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.g102', {
            url: "/g102",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/games/102.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.g414', {
            url: "/g414",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/games/414.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.g559', {
            url: "/g559",
            views : { 
                '@' : {
                    templateUrl: "assets/templates/games/559.html",
                    controller: "TableCtrl"
                }
            }
        })
        ;
});
