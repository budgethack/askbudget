(function(angular) {
angular.module('search', [])
    .controller('queryListCtrl', ['$scope','$filter', '$http', function($scope, $filter, $http) {
        
        $scope.question = '';
     
        $scope.submit = function() {
            $http.post( 
                'api/post_question',
                { data: {"question":$scope.question }}
            ).then(function successCallback(response) {
                /* top mentions */
                $scope.top_mention_count = response.data.answer.top_mentions.count;
                
                $scope.top_mentions_doc = response.data.answer.top_mentions.documents;
                
                /* related spend */
                $scope.related_spends = response.data.answer.related_spend.documents;
                console.log("spend: " + $scope.related_spends);

                /* related_keywords */
                $scope.related_keywords = response.data.answer.related_keyword.keyword;
                
            }, function errorCallback(response) {
            
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
