var express = require('express');
var AlchemyAPI = require('./alchemyapi_node/alchemyapi');
var alchemyapi = new AlchemyAPI();
var app = express();

app.set('views', './views');
app.set('view engine', 'jade');

app.get('/', function(req, res) {
// res.render('index', { title: 'Hey', message: 'Goodbye there!'});
  var myTxt = "Whoa, AlchemyAPI's Node.js SDK is really great, I can't wait to build my app!";
  alchemyapi.sentiment('text', myTxt, {}, function(response) {
   res.send('Sentiment: ' + response['docSentiment']['type']);
  });
});

app.get('/hi', function(req, res) {
  res.send();
});

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});
