var app = angular.module('search', ['angular-jqcloud']);

app.controller('queryListCtrl', ['$scope','$filter', '$http', '$location', function($scope, $filter, $http, $location) {
        $scope.answer;
        $scope.words = [];

        $scope.sendQuestion = function() {
          console.log($scope.question);
            $http.post('api/post_question', {
              'question': $scope.question
            }).then(function successCallback(response) {
                $scope.answer = response.data.answer;
            });
        };

        $http.get('/api/get_concepts').then(function successCallback(response) {
            words = [];
            angular.forEach(response.data.main_concepts, function(value, key) {
              words.push({"text": value.text, "weight": value.weight, "handlers": {
                click: function(clicked) {
                   $scope.question = clicked.currentTarget.innerText;
                   $scope.sendQuestion();
               }}, "link": "#!?question=" + value.text})
            });

            $scope.words = words;
        });
}]);
