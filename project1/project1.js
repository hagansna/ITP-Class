var emotions = [emotional, emotions, happy, happiness, sad, sadness, anger, angry, hate, love, feel, feeling, jealous, jealousy];


for (i=0;i<emotions.length;i++) {
	var query_params = { apikey: 'API_KEY',
						 phrase: emotions[i],
						 sort: 'count desc'
						};
	var endpoint = 'http://capitolwords.org/api/1/phrases/party.json';

	var option = {
	  data: query_params,
	  type: 'GET',
	  dataType: 'jsonp'
	};

	var request = JQuery.ajax(endpoint, options)
						.done(showResponse);

}



