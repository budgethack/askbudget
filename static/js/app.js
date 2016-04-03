var app = angular.module('search', ['angular-jqcloud','googlechart']);

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
                console.log(response.data.answer.main_concepts);
                $scope.main_concepts = response.data.answer.main_concepts;

                words = [];
                angular.forEach($scope.related_things.keywords, function(value, key) {
                  words.push({"text": value.name, "weight": value.count * 10});
                });
                $scope.related_things_words = words;
                console.log(words);
                $scope.chart = false;
            });
        };
        
        /* Histrogram */
        var chart1 = {};
        chart1.type = "ColumnChart";
        chart1.cssStyle = "height:900px; width:100%;";
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
        
        //Reference: https://bouil.github.io/angular-google-chart/#/fat
    
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
