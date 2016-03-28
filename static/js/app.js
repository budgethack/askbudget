(function(angular) {
angular.module('search', [])
    .controller('queryListCtrl', ['$scope','$filter', '$http', function($scope, $filter, $http) {
        $scope.question = '';
        $scope.top_mentions;
        $scope.related_things;
     
        $scope.submit = function() {
            $http.post( 
                'api/post_question', {
                  'question': $scope.question
                }
            ).then(function successCallback(response) {
                /* top mentions */
                $scope.top_mentions = response.data.answer.top_mentions;
                $scope.related_things = response.data.answer.related_things;
            });
        };

    
        /*
        $scope.init = function() {
            $http.post(
                'api/get_question',
                {data: {"question": $scope.question }}
            ).then(function successCallback(response) {
                $scope.prev_question = response.data.prev_question;
                console.log(response);

            }, function errorCallback(response) {
                
            });
        };
        */


    }]);
})(window.angular);
