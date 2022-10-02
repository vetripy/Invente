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

    document.getElementById('event_form').addEventListener("submit", function(e) {
        e.preventDefault(); // before the code
        
        var event_title = document.getElementById('event_title').value;
        var event_description = document.getElementById('event_description').value;
        var event_schedule = document.getElementById('event_schedule').value;
        var event_note = document.getElementById('event_note').value;
        var event_rules = document.getElementById('event_rules').value;
        var rounds = document.getElementById('rounds').value;


        let rounds_data = {};
        for (var i = 0; i < rounds; i++) {
            let round = {
                "round_title": document.getElementById(`event_round_${i+1}_title`).value,
                "round_desc": document.getElementById(`event_round_${i+1}_desc`).value
            }
            let n = i + 1;
            rounds_data = {...rounds_data, [`round_${n}`]: round};
        }
        
        var event_part_desc = document.getElementById('event_part_desc').value;

        var event_prize = document.getElementById('event_prize').value;

        var event_data = {
            "event_title": event_title,
            "event_description": event_description,
            "event_schedule": event_schedule,
            "event_note": event_note,
            "event_rules": event_rules,
            "rounds": rounds_data,
            "event_part_desc": event_part_desc,
            "event_prize": event_prize
        };
        
        console.log(event_data);
      })
});
