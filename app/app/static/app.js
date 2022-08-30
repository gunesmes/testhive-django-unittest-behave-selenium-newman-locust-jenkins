var $ = jQuery;
$(document).ready(addClickHandlers);

function addClickHandlers() {
    $("#registerbtn").click( function() { RegisterFormSubmit() });
}

function ajax_setup() {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
}


var isRegisterProcessing = false;
function RegisterFormSubmit() {
    if (isRegisterProcessing == false) {
        $("form#registerForm").submit(function (ev) {
            ev.preventDefault();
            ajax_setup();

            var username = $("#username").val();
            var email = $("#email").val();
            var birthday = $("#birthday").val();
            var address = $("#address").val();

            if (username && email && birthday && address) {
                $.ajax({
                    "type": "POST",
                    "dataType": "json",
                    "url": "api/register",
                    "data": {
                        "username": username,
                        "email": email,
                        "birthday": birthday,
                        "address": address,
                        "client": "web"
                    },
                    "success": function (result) {
                        var a = ''
                        if (result["result"] == true) {
                            a = '<li class="success">' + result["message"] + '</li>';
                        } else {
                            for (err in result["message"]) {
                                var a = a + '<li class="warning">' + result["message"][err][0] + '</li>'
                            }
                        }
                        $("#info").html(a);
                    }
                });
            } else {
                // console.log( username , email , birthday, address);
                alert("\nPlease fill-in all the field!")
            }
        });
    }
    isRegisterProcessing = true;
}

function getUser(username) {
    var modal = document.getElementById('myModal');

    $.ajax({
        "type": "GET",
        "dataType": "json",
        "url": "api/user",
        "data": {
            "username": username
        },
        "success": function (result) {
            user_info = "";
            for (var key in result["fields"]) {
                user_info += "<p>" + result["fields"][key] + "</p>";
            }
            $(".modal-content > p").html(user_info)
            modal.style.display = "block";
        }
    });
}

function closeModal() {
    $('#myModal').hide();
}
