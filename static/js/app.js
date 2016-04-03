var app = angular.module('search', ['ngRoute', 'angular-jqcloud', 'googlechart']);
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

app.controller('QueryCtrl', function($scope, $rootScope) {
  console.log('Here I am');
});

app.controller('HomeCtrl', ['$scope', '$http', function($scope, $http) {
  console.log('AT HOME');

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
      });
  }

  if ($routeParams.question) {
    $rootScope.question = $routeParams.question; 
    sendQuestion($routeParams.question);
  };

  var chart1 = {};
  chart1.type = "ColumnChart";
  chart1.cssStyle = "height:300px; width:100%";
  chart1.data = {"cols": [
    {id: 'year', label: 'Year', type: 'string'},
    {id: 'mentions', label: 'Mentions', type: 'number'}
  ], "rows": [
      {c: [
          {v: "2011"},
          {v: 100},
      ]},
      {c: [
          {v: "2012"},
          {v: 130},
      ]},
      {c: [
          {v: "2011"},
          {v: 90},
      ]}
  ]};

  chart1.options = {
      "isStacked": "true",
      "fill": 20,
      "displayExactValues": true,
      "hAxis": {
          "title": "Year"
      }
  };
  
  chart1.formatters = {};
  $scope.chart = chart1;
  //Reference https://bouil.github.io/angular-google-chart/#/fat

});
