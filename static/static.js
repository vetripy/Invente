document.addEventListener("DOMContentLoaded", function() {
   var loginform = document.getElementById("login");
   
    loginform.addEventListener("click", function(e) {
        document.getElementById("event-form").style.display = "none";
        document.getElementById('login-form').style.display = 'block';
    });

    var eventform = document.getElementById("addevent");

    eventform.addEventListener("click", function(e) {
        document.getElementById("login-form").style.display = "none";
        document.getElementById('event-form').style.display = 'block';
    }
    );

    var home = document.getElementById("home");

    home.addEventListener("click", function(e) {
        document.getElementById("login-form").style.display = "none";
        document.getElementById('event-form').style.display = 'none';
    }
    );
});