(function(angular) {
angular.module('search', [])
    .controller('queryListCtrl', ['$scope','$filter', '$http', function($scope, $filter, $http) {
        $scope.question = '';
     
        $scope.answers = [{
        }];

        $scope.submit = function() {
            $http.get( 
                'api/question',
                { params: {"question":$scope.question }}
            );
        };

    }]);
})(window.angular);
