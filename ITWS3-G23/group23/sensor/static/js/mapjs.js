<script>
    
      var neighborhoods = [
        {lat: 13.521724, lng: 80.0007},
        {lat: 13.548883, lng: 80.0008},
        {lat: 13.554662, lng: 80.026871},
        {lat: 13.557478, lng: 80.018524}
      ];
	
      var markers = [];
      var map;

      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 14,
          center: {lat: 13.5232, lng: 79.9982}
        });
      }
	var i=1;
      function drop() {
        clearMarkers();
          if(i==1){
          	addMarkerWithTimeout1(neighborhoods[0], 0 * 200,'plant-1','Red');
          }
		  addMarkerWithTimeout2(neighborhoods[1], 1 * 200,'plant-2');
		  addMarkerWithTimeout3(neighborhoods[2], 2 * 200,'plant-3');
		  addMarkerWithTimeout4(neighborhoods[3], 3 * 200,'plant-4');
          
      }
      
      function addMarkerWithTimeout1(position, timeout,name,color) {
        window.setTimeout(function() {
          markers.push(new google.maps.Marker({
            position: position,
            map: map,
            label: name,
	    icon: pinSymbol(color),
            animation: google.maps.Animation.DROP
          }));
        }, timeout);
      }
	
      function addMarkerWithTimeout2(position, timeout,name) {
        window.setTimeout(function() {
          markers.push(new google.maps.Marker({
            position: position,
            map: map,
            label: name,
            icon: pinSymbol('Red'),
            animation: google.maps.Animation.DROP
          }));
        }, timeout);
      }	

      function addMarkerWithTimeout3(position, timeout,name) {
        window.setTimeout(function() {
          markers.push(new google.maps.Marker({
            position: position,
            map: map,
            label: name,
            icon: pinSymbol('Blue'),
            animation: google.maps.Animation.DROP
          }));
        }, timeout);
      }
	
      function addMarkerWithTimeout4(position, timeout,name) {
        window.setTimeout(function() {
          markers.push(new google.maps.Marker({
            position: position,
            map: map,
            label: name,
            icon: pinSymbol('Blue'),
            animation: google.maps.Animation.DROP
          }));
        }, timeout);
      }
	
      function clearMarkers() {
        for (var i = 0; i < markers.length; i++) {
          markers[i].setMap(null);
        }
        markers = [];
      }
      
	function pinSymbol(color) {
	  return {
	    path: 'M 0,0 C -2,-20 -10,-22 -10,-30 A 10,10 0 1,1 10,-30 C 10,-22 2,-20 0,0 z',
	    fillColor: color,
	    fillOpacity: 1,
	    strokeColor: '#000',
	    strokeWeight: 1,
	    scale: 1,
	    labelOrigin: new google.maps.Point(0, -29)
	  };
	}
      
      google.maps.event.addDomListener(window, 'load', initialize);
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBqKrqR6E3c2ZVLHYrrHtRVsuN3_FcVY1U&callback=initMap">
    </script>
