var cheerio = require('cheerio');
var request = require('request');
var servi = require('servi');

var app = new servi(true);
port(3000);
start();
var db = useDatabase('cameras');

var url = 'http://nyctmc.org/multiview2.php';
request(url, handleData);

function handleData(error, resp, body) {
	$ = cheerio.load(body);
	$('[id*=tableCam]').each(function() {
		var b = $(this).find('font').text();
		console.log(b)
		var lis = [];
		var count = 0;
		$(this).find('#repCam__ctl0_trCam span').each(function() {
			console.log($(this).text());
			lis.push($(this).text());
			count += 1;
		});
		var dic = {
			borough: b,
			location: lis,
			count: count
		};
		db.add(dic);
	});
}

route('/', showAll);

function showAll(request) {
	db.getAll(function(data){
		request.header('application/json');
		request.respond(JSON.stringify(data));
	});
}