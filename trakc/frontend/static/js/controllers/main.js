function MainController($scope, $http) {
	$scope.prevpage = ''
	$scope.nextpage = ''

	$http.get('api/v1/post/').success(function(data) {
		$scope.prevpage = data.meta.previous
		$scope.nextpage = data.meta.next
		$scope.posts = data.objects;
	})

	$scope.gonextpage = function () {
		if ($scope.nextpage != 'null')
		{
			$http.get($scope.nextpage).success(function(data) {
				$scope.prevpage = data.meta.previous
				$scope.nextpage = data.meta.next
				$scope.posts = data.objects;
			})
		}
	}



	$scope.goprevpage = function () {
		if ($scope.nextpage != 'null')
		{
			$http.get($scope.prevpage).success(function(data) {
				$scope.prevpage = data.meta.previous
				$scope.nextpage = data.meta.next
				$scope.posts = data.objects;
			})
		}
	}

	$scope.filter_data = function () {
		$scope.since = document.getElementById('date_since_hidden').value
		$scope.until = document.getElementById('date_until_hidden').value
		//alert($scope.since);
		$http.get('api/v1/post/?since=' + $scope.since + '&until=' + $scope.until).success(function(data) {
			$scope.posts = data.objects;
			$scope.prevpage = data.meta.previous
			$scope.nextpage = data.meta.next
		})
	}    
}

