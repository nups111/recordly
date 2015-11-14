
// TODO: Need to verify username and pwd from DB
function signIn() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      document.getElementById("demo").innerHTML = xhttp.responseText;
    }
  }
  xhttp.open("GET", "/users", true);
  xhttp.send();
}


function SignupPage() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      document.getElementById("loginForm").innerHTML = xhttp.responseText;
    }
  }
  xhttp.open("GET", "/signup", true);
  xhttp.send();
}