var app = angular.module('api2k15', [
    'ngTouch',
    'ui.grid',
    'ui.router'    
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
                    templateUrl: '../../../templates/shared/navbar.html',
                    controller: 'NavbarCtrl'
                }
               // 'footer': {
               //     templateUrl: '../../../templates/shared/footer.html',
               //     controller: 'FooterCtrl'
               // }
            }
        })
        .state('root.home', {
            url: "/home",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/home.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.teams', {
            url: "/teams",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/teams/teams.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.players', {
            url: "/players",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/players/players.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.games', {
            url: "/games",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/games/games.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.about', {
            url: "/about",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/about/about.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.lac', {
            url: "/lac",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/teams/LAC.html",
                    controller: "TableCtrl"
                }
            }

        })
        .state('root.mia', {
            url: "/mia",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/teams/MIA.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.sas', {
            url: "/sas",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/teams/SAS.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.bg', {
            url: "/bg",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/players/BG.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.dw', {
            url: "/dw",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/players/DW.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.td', {
            url: "/td",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/players/TD.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.g102', {
            url: "/g102",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/games/102.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.g414', {
            url: "/g414",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/games/414.html",
                    controller: "TableCtrl"
                }
            }
        })
        .state('root.g559', {
            url: "/g559",
            views : { 
                '@' : {
                    templateUrl: "../../../templates/games/559.html",
                    controller: "TableCtrl"
                }
            }
        })
        ;
});
