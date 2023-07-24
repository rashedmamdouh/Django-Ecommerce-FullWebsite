document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Message sent successfully!');
  });
  
  function initMap() {
    const printvilleLocation = { lat: 40.7128, lng: -74.0060 };
    const map = new google.maps.Map(document.getElementById('map'), {
      zoom: 14,
      center: printvilleLocation,
    });
    const marker = new google.maps.Marker({
      position: printvilleLocation,
      map: map,
    });
  }
  
  initMap();