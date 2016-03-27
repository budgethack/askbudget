(function(angular) {
angular.module('search', [])
    .controller('queryListCtrl', ['$scope','$filter', '$http', function($scope, $filter, $http) {
        $scope.question = '';
     
        $scope.submit = function() {
            $http.get( 
                'api/question',
                { params: {"question":$scope.question }}
            ).then(function successCallback(response) {
                $scope.answers = response.data.answer;
        
            }, function errorCallback(response) {
            
            });
        };

    }]);
})(window.angular);
