function MainController($scope, $http) {
	$http.get('api/v1/post/').success(function(data) {
		$scope.posts = data.objects;
	})

	$scope.filter_data = function () {
		$scope.since = document.getElementById('date_since_hidden').value
		$scope.until = document.getElementById('date_until_hidden').value
		alert($scope.since);
		$http.get('api/v1/post/?since=' + $scope.date_since + '&until=' + $scope.date_until).success(function(data) {
			$scope.posts = data.objects;
		})
	}    
}

