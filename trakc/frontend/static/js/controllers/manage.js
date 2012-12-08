function ManageController($scope, $http) {
   
    $http.get('api/v1/target/').success(function(data) {
        $scope.targets = data.objects;
    })

    $http.get('api/v1/user/0').success(function(data) {

        $scope.costs = data

    });

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

    $scope.add_target = function (suggested) {
        
        $http.post('api/v1/target/',
            data = {
                'google_id': suggested.id,
                'photo_url': suggested.image.url,
                'name': suggested.displayName
            }).success( function () {
                alert('Target added');
            })
    }

    $scope.remove_target = function (target) {
        $http.delete('api/v1/target/' + target.google_id).success(
            function () {
                alert('Target deleted');
            }
        );
    }

    $scope.update_weights = function () {
        var like = parseInt($scope.costs.like_cost)
        var share = parseInt($scope.costs.share_cost)
        var comment = parseInt($scope.costs.comment_cost)
    
        if (like > 0 && share > 0 && comment > 0) {
            $http.put('api/v1/user/0', 
                data= {
                    'like': like,
                    'share': share,
                    'comment': comment
                }).success( function () {
                    alert("Weights updates");
                });
        }
    }
}

