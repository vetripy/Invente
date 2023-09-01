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
        var event_type = document.getElementById('event_type').value;
        var rounds = document.getElementById('rounds').value;
        var teamSize = document.getElementById('event_participants').value;
        var event_date = document.getElementById('event_date').value;
        var dept = document.getElementById('dept').value;
        var venue = document.getElementById('venue').value;

        var type_desc = document.getElementById('type_desc').value;
        let meta = {};

        if (type_desc === "desc"){
            for (var i = 0; i < rounds; i++) {
                let round = {
                    "round_title": document.getElementById(`event_round_${i+1}_title`).value,
                    "round_desc": document.getElementById(`event_round_${i+1}_desc`).value
                }
                meta = {...meta, [round.round_title]: round.round_desc};
            
            }
        }
        else if (type_desc === "bullets"){
            for(var i = 0; i < rounds; i++){

                let no_bullets = document.getElementById(`no_bullets_${i+1}`).value;

                let bullets = [];

                for(var j = 0; j < no_bullets; j++){
                    bullets.push(document.getElementById(`event_round_${i+1}_bullet_${j+1}`).value);
                }
                let round = {
                    "round_title": document.getElementById(`event_round_${i+1}_title`).value,
                    "round_desc": bullets
                }
                meta = {...meta, [round.round_title]: round.round_desc};
            }

            
        }
        

        var winner = document.getElementById('winner').value;
        var runner = document.getElementById('runner').value;

        var event_data = {
            "id": 0,
            "title": event_title,
            "desc": event_description,
            "type": event_type,
            "teamSize": teamSize,
            "dept": dept,
            "venue": venue,
            "time": event_date,
            "winner": winner,
            "runner": runner,
            "meta": meta,
        };
        
        console.log(event_data);
        
      })
});
