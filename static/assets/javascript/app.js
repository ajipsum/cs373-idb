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
                    templateUrl: "../../../templates/table.html",
                    controller: "TableCtrl"
                }
            }
        });
});
