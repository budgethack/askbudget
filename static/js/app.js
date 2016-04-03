var app = angular.module('search', ['ngRoute', 'angular-jqcloud', 'googlechart', 'ngSanitize']);
app.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/home', {
        templateUrl: '/static/partials/home.html',
        controller: 'HomeCtrl'
      }).
      when('/answer', {
        templateUrl: '/static/partials/answer.html',
        controller: 'AnswerCtrl'
      }).
      otherwise({
        redirectTo: '/home'
      });
  }
]);

app.controller('QueryCtrl', function($scope, $rootScope, $location) {
  $scope.sendQuestion = function(question) {
    if (question) {
      $location.path('/answer/').search({question: question});
    } else {
      $location.path('/')
    }
  }
});

app.controller('HomeCtrl', ['$scope', '$http', function($scope, $http) {
  $http.get('/api/get_concepts').then(function successCallback(response) {
    words = [];

    angular.forEach(response.data.main_concepts, function(value, key) {
      words.push({
        "text": value.text, "weight": value.weight,
        "link": "#/answer?question=" + value.text})
    });

    $scope.words = words;
  });

}]);

app.controller(
    'AnswerCtrl', function($scope, $filter, $http, $routeParams, $rootScope) {
  $scope.answer;
  $scope.words = [];

  sendQuestion = function(question) {
      $http.post('api/post_question', {
        'question': question
      }).then(function successCallback(response) {
          $scope.answer = response.data.answer;
          if ($scope.answer.historic_mentions) {
            buildChart();
          }
      });
  }

  if ($routeParams.question) {
    $rootScope.question = $routeParams.question; 
    sendQuestion($routeParams.question);
  };

  buildChart = function() {
    var historyChart = {};
    historyChart.type = "ColumnChart";
    historyChart.cssStyle = "height:300px; width:100%";
    historyChart.data = {
      "cols": [
        {id: 'year', label: 'Year', type: 'string'},
        {id: 'mentions', label: 'Mentions', type: 'number'}
      ]
    };

    rows = [];
    angular.forEach($scope.answer.historic_mentions, function(value, key) {
      rows.push({c: [{v: value.year}, {v: value.count}]});
    });
    console.log("ROWS");
    console.log(rows);
    historyChart.data['rows'] = rows;

    historyChart.options = {
        "isStacked": "true",
        "fill": 20,
        "displayExactValues": true,
        "hAxis": {
            "title": "Year"
        }
    };
  
    historyChart.formatters = {};
    $scope.chart = historyChart;
  }

    
});
