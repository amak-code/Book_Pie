let map, infoWindow;

const myLocation = new Promise(resolve => {
    if (!navigator.geolocation) {
        resolve()
    }
    else {
        navigator.geolocation.getCurrentPosition(
            position => 
                resolve({
                lat: position.coords.latitude,
                lng: position.coords.longitude
            }),
            () => resolve(undefined)
        )
    }
})

async function initMap()  {
    let pos = await myLocation
    if (!pos) {
        pos = {
            lat: 37.7749, lng: -122.4194
        }
    }
 
    

    map = new google.maps.Map(document.getElementById("map"), {
        center: pos,
        zoom: 15,
        zoomControl: true
    });

    const marker = new google.maps.Marker({
        position: pos,
        map: map,
    });
    
    var pyrmont = new google.maps.LatLng(pos);

    var request = {
    
    location: pyrmont,
    radius: '5000',
    type: ['book_store']
    };

    var service = new google.maps.places.PlacesService(map);
    service.nearbySearch(request, callback);
    // event listener for dragging the map 
    google.maps.event.addListener(map, "dragend", function() {
        var center = this.getCenter();
        var latitude = center.lat();
        var longitude = center.lng();

        var pyrmont = new google.maps.LatLng(pos);
        var request = {
        location: center,
        radius: '5000',
        type: ['book_store']
        };
    
        var service = new google.maps.places.PlacesService(map);
        service.nearbySearch(request, callback);

      });
 
}

function callback(results, status) {
    if (status == google.maps.places.PlacesServiceStatus.OK) {
    for (var i = 0; i < results.length; i++) {
        console.log(results[i]);
        const marker = new google.maps.Marker({
            position: results[i].geometry.location,
            icon: {
                path: "M3 3H8.4C9.35478 3 10.2705 3.37928 10.9456 4.05442C11.6207 4.72955 12 5.64522 12 6.6V21C12 20.2839 11.7155 19.5972 11.2092 19.0908C10.7028 18.5845 10.0161 18.3 9.3 18.3H3V3Z M21 3H15.6C14.6452 3 13.7295 3.37928 13.0544 4.05442C12.3793 4.72955 12 5.64522 12 6.6V20.7C12 19.9839 12.2845 19.2972 12.7908 18.7908C13.2972 18.2845 13.9839 18 14.7 18H21V3Z",
                fillOpacity: 0.3,
                fillColor: "blue",
                strokeWeight: 0.3,
                rotation: 0,
                scale: 1.7,
                anchor: new google.maps.Point(0, 20)
              },
            map: map,
            title: results[i].name,
        });

        // Builds an InfoWindow to display details above the marker
        let rating = "None"
        if (results[i].rating)
            rating = results[i].rating
        
        let photo = "/static/images/no-image-available.jpg"
        
        if (results[i].photos) {
            let firstPhoto = results[i].photos[0];
            photo = firstPhoto.getUrl();
            
        }

        // TODO: make a PlacesService.getDetails(request, callback) to get opening_hours
        let is_open = "not providing data if it's open ";
        var time_value = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
        console.log(time_value)
        if (results[i].opening_hours){
            var open_hours = results[i].opening_hours.open_now
            if (open_hours){
                is_open = "open"
            }
            else{
                is_open = "closed"
            }
            console.log("OPENIG HOURS")
            console.log(open_hours)

        }


        const markerInfo = `
        <img src = ${photo} style = "width: 100pt; height: 100pt;">
        <h3>${marker.title}</h3>
        <p>Rating: ${rating}</p>
        <p>The store is ${is_open} now at ${time_value}</p>
        `;
  
        const infoWindow = new google.maps.InfoWindow({
            content: markerInfo,
            maxWidth: 200,
        });
    
        marker.addListener('click', () => {
            infoWindow.close()
            infoWindow.open(map, marker);
            
        });
        
            }
    }
}


window.initMap = initMap;

