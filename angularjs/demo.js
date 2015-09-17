(function() {
  var app = angular.module('store', []);

  app.controller('StoreContainer', function() {
    this.product = gem;
  });

  app.controller('PanelController', function() {
   this.tab = 1;

   this.selectTab = function(setTab) {
    this.tab = setTab;
   };

   this.isSelected = function(checkTab) {
     return this.tab === checkTab;
   };
  });

  app.controller('ReviewController', function() {
    this.review = {};

    this.addReview = function(product) {
      product.reviews.push(this.review);
      this.review = {};
    }
  })

  app.directive('productTitle', function() {
    return {
      restrict: 'E',
      templateUrl: 'product-title.html'
    }
  });

  var gems = [
    {
      name : 'Dodecahedron',
      price : 2.95,
      description : ' . . . ',
      canPurchase : false,
      soldOut: true
    },
    {
      name : "Pentagonal Gem",
      price : 5.95,
      description : ' . . . ',
      canPurchase : false
    }
  ];
})();
