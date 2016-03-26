(function(angular) {
angular.module('search', [])
  .controller('queryListCtrl', ['$scope','$filter',function($scope,$filter) {
    $scope.query = '';
    
    $scope.answers = [{
      post: "for a tutorial on LAMP with this Apache server, check http://www.susegeek.com/internet-browser/install-configure-lamp-apachemysqlphp-in-opensuse-110/",
      datetime: "answered Oct 28 '10 at 14:13",
      up_votes: 10,
      down_votes: 1,
      author: "Jack"
     },
      {
      post: "It really depends on the distribution you have chosen. Typically, though, you can start Apache using the init scripts. For example, on Ubuntu server it will be",
      datetime: "answered Jan 4 '12 at 19:13",
      up_votes: 1,
      down_votes: 0,
      author: "Anna"
     }];
    
  }]);
})(window.angular);