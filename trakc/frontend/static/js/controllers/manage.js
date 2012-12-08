function ManageController($scope, $http) {
   
    $http.get('api/v1/target/').success(function(data) {
        $scope.targets = data.objects;
    })

    $scope.fetch_partial_results = function() {
        var t_name = $scope.target_name
   
        if (typeof t_name == 'undefined') {
            return;     
        }

        $http.get('suggestion?name=' + t_name).success(
            function (data) {
                $scope.suggestions = data
            });
 
    }

}

