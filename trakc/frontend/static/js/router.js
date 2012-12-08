angular.module('trakc', []).config(function ($routeProvider) {
    $routeProvider.when('/',
            {templateUrl: 'static/templates/main.html',
            controller: MainController}
            ).
            when('/manage',
            {templateUrl: 'static/templates/manage.html',
            controller: ManageController}
            )
});

