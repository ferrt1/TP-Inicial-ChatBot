$("#chat-form").on("submit", function(e) {
    e.preventDefault();
    var userMessage = $("#user-message").val();
    $.post("/bot", {user_message: userMessage}, function(botMessage) {
        $("#chatbox").append("<p class='mb-2'><strong>Tú:</strong> " + userMessage + "</p>");
        $("#chatbox").append("<p class='mb-2 text-blue-500'><strong>Bot:</strong> " + botMessage + "</p>");
    });
    $("#user-message").val("");
});