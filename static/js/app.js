(function(angular) {
angular.module('search', [])
    .controller('queryListCtrl', ['$scope','$filter', '$http', function($scope, $filter, $http) {
        
        $scope.question = '';
     
        $scope.submit = function() {
            $http.post( 
                'api/post_question',
                { data: {"question":$scope.question }}
            ).then(function successCallback(response) {
                $scope.answers = response.data.answer;
        
            }, function errorCallback(response) {
            
            });
        };

        $scope.init = function() {
            $http.post(
                'api/get_question',
                {data: {"question": $scope.question }}
            ).then(function successCallback(response) {
                $scope.prev_question = response.data.prev_question;
                console.log("adad" + response);

            }, function errorCallback(response) {

            });
        };


    }]);
})(window.angular);
