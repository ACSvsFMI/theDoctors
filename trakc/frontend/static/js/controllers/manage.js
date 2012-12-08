function ManageController($scope, $http) {
   
    $http.get('api/v1/target/').success(function(data) {
        $scope.targets = data.objects;
    })
}

