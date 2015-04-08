$(document).ready(function() {
  // array of epoch times (from April 1st to April 6th)
  var times = [1427904000,1427990400,1428076800,1428163200,1428249600,1428336000];
  // loop through each timestamp and use time in api call
  $.each(times, function(index, value) {
    var url = 'https://api.instagram.com/v1/media/search?max_timestamp='+value+'&lat=40.7300&lng=-73.9950&client_id=API_KEY'
    // use ajax to get data from instagram
    $.ajax({
      url: url,
      dataType: 'jsonp',
      success: function(jsonData) {
        console.log(jsonData.data);

        var pics = jsonData.data;
        // for each picture, append the picture to the container div with height and width scaled based on likes/tagmeasure ratio.
        for(var i=0;i<pics.length;i++) {
          var likes = pics[i].likes.count;
          var tags = pics[i].tags.length;
          var image = pics[i].images.standard_resolution.url
          $('#container').append("<div class='box'><img title='Likes per tag: "+likes/(tags + 1)+"' src='"+image+"' height="+(likes)/(tags + 1) +" width="+(likes)/(tags + 1)  +"/><br />Likes: "+likes+"<br />Tags: "+tags+"</div>");
        }
      },
      error: function() {
        alert("error");
      }
    });
  });
  // adds tooltip functionality that reads image title.
  $(function() {
    $(document).tooltip();
  });



});
