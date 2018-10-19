
function initialize(coords, id) {
    if (coords != undefined){
        res = coords.split(",");
        var myStyles = [{
            "featureType": "administrative",
            "elementType": "geometry",
            "stylers": [{
                "visibility": "off"
            }]
        },
        {
            "featureType": "road",
            "elementType": "labels.icon",
            "stylers": [{
                "visibility": "off"
            }]
        },
        {
            "featureType": "transit",
            "stylers": [{
                "visibility": "off"
            }]
        }
        ];

        var mapOptions = {
            center: new google.maps.LatLng(parseFloat(res[0]), parseFloat(res[1])),
            zoom: 16,
            mapTypeId: 'satellite',
            // draggable: false,
            // scrollwheel: false,
            // disableDefaultUI: true,
            // panControl: false,
            // minZoom: 4,
            // maxZoom: 12,
            styles: myStyles
        };
        var map = new google.maps.Map(document.getElementById("mapCanvas" + id),
            mapOptions);
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(parseFloat(res[0]), parseFloat(res[1]))
        });
        marker.setMap(map);
    }
}

function ifElseTest() {
    var first = document.getElementById('pilotName');
    var second = document.getElementById('pilotNumber');
    if (first.value == "pilot") {
        second.value = first.value;
    } else if (first.value == "otherpilot") {
        second.value = first.value;
    };
}

// var darkmode = "http://localhost:8080/static/css/bootstrap_darkly.min.css";
var darkmode = "https://bootswatch.com/4/darkly/bootstrap.min.css";
var lightmode = "https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css";

function togglePageContentLightDark() {
    var css = document.getElementById('theme_css');
    var currentClass = css.href;
    var newClass = css.href == darkmode ? lightmode : darkmode;
    css.href = newClass;
    document.cookie = 'theme=' + (newClass == lightmode ? 'light' : 'dark');
}

function isDarkThemeSelected() {
    return document.cookie.match(/theme=dark/i) != null;
}

function setThemeFromCookie() {
    var css = document.getElementById('theme_css');
    css.href = isDarkThemeSelected() ? darkmode : lightmode
}

function outputToConsole(input){
    console.log(input);
    console.log(typeof input);
}

function secondsToHms(d) {
    d = Number(d);

    var h = Math.floor(d / 3600);
    var m = Math.floor(d % 3600 / 60);
    var s = Math.floor(d % 3600 % 60);

    return ('0' + h).slice(-2) + ":" + ('0' + m).slice(-2) + ":" + ('0' + s).slice(-2);
}

function hmsToSeconds(hms) {
    var a = hms.split(':'); // split it at the colons
    return (+a[0]) * 60 + (+a[1]);
}

function totalTime(input){
    // expects the raw log data from 
    var res = doubleToJSON(input);
    var ttlTime = 0
    for (var i=0; i < res.length; i++) {
        for (const [key, value] of Object.entries(res[i])){
            if (key == "duration"){
                // value is a string (mm:ss)
                ttlTime += hmsToSeconds(value);
            }
        }
    }
    console.log("The total flown time is: " + secondsToHms(ttlTime))
    return secondsToHms(ttlTime);
}

function doubleToJSON(str){
    var res =  replaceAll(str, "&#34;", "\"");
    var out = JSON.parse(res);
    return out
}

function singleToJSON(str){
    var res =  replaceAll(str, "&#39;", "\"");
    return res
}

function replaceAll(str, find, replace) {
    return str.replace(new RegExp(find, 'g'), replace);
}

// Generates an alert on flash messages
$(document).ready(function(){
    setThemeFromCookie();

    var alrt = $("#box-descr")
    if ((alrt).length){
        swal({
            type: $(alrt).attr("class"),
            // title: 'Hey!!!',
            text: $(alrt).text(),
          })
    }
});