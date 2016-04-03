var app = angular.module('search', ['angular-jqcloud','googlechart']);

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
        
        /* Histrogram */
        var chart1 = {};
        chart1.type = "ColumnChart";
        chart1.cssStyle = "height:500px; width:100%;border:1px solid red";
        chart1.data = {"cols": [
            {id: "category", label: "Year", type: "string"},
            {id: "families", label: "Families", type: "number"},
            {id: "jobs", label: "Jobs", type: "number"},
            {id: "health", label: "Health", type: "number"},
            {id: "education", label: "Education", type: "number"},
            {id: "trade", label: "Trade", type: "number"},
            {id: "small-business", label: "Small business", type: "number"},
            {id: "transportation", label: "Transportation", type: "number"},
        ], "rows": [
            {c: [
                {v: "2011"},
                {v: 10, f: "Majority are in Budget Overview  Doc,Suburban Growth Doc"},
                {v: 11},
                {v: 7},
                {v: 4},
                {v: 4},
                {v: 2},
                {v: 6}
            ]},
            {c: [
                {v: "2012"},
                {v: 13},
                {v: 3},
                {v: 10},
                {v: 2},
                {v: 4},
                {v: 3},
                {v: 5}
            ]},
            {c: [
                {v: "2013"},
                {v: 9},
                {v: 0},
                {v: 11},
                {v: 6},
                {v: 6},
                {v: 3},
                {v: 3}
            ]},
            {c: [
                {v: "2014"},
                {v: 8},
                {v: 3},
                {v: 11},
                {v: 6},
                {v: 4},
                {v: 2},
                {v: 6}

            ]},
            {c: [
                {v: "2015"},
                {v: 9},
                {v: 10},
                {v: 12},
                {v: 9},
                {v: 3},
                {v: 4},
                {v: 5}

            ]},
            {c: [
                {v: "2016"},
                {v: 9},
                {v: 3},
                {v: 8},
                {v: 10},
                {v: 2},
                {v: 4},
                {v: 2}

            ]}
        ]};

        chart1.options = {
            "title": "Victoria Budget Data per yearly",
            "isStacked": "true",
            "fill": 20,
            "displayExactValues": true,
            "vAxis": {
                "title": "Budget Information in Percentage", "gridlines": {"count": 6}
            },
            "hAxis": {
                "title": "Year"
            }
        };
        
        chart1.formatters = {};
        $scope.chart = chart1;
        //Reference https://bouil.github.io/angular-google-chart/#/fat
    
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
