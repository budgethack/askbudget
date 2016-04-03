var app = angular.module('search', ['angular-jqcloud']);

app.controller('queryListCtrl', ['$scope','$filter', '$http', function($scope, $filter, $http) {
        $scope.question = '';
        $scope.top_mentions;
        $scope.related_things;
        $scope.main_concepts;
        $scope.related_things_words = [];
     
        $scope.submit = function() {
            $http.post( 
                'api/post_question', {
                  'question': $scope.question
                }
            ).then(function successCallback(response) {
                /* top mentions */
                $scope.top_mentions = response.data.answer.top_mentions;
                $scope.related_things = response.data.answer.related_things;
                $scope.related_spend = response.data.answer.related_spend;
                $scope.main_concepts = response.data.answer.main_concepts;

                words = [];
                angular.forEach($scope.related_things.keywords, function(value, key) {
                  words.push({"text": value.name, "weight": value.count * 10});
                });
                $scope.related_things_words = words;
            });
        };

}]);
