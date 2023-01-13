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
 
    // infoWindow = new google.maps.InfoWindow();
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
       
        }
    }
}


window.initMap = initMap;

