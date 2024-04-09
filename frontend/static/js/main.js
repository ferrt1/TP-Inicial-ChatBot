$("#chat-form").on("submit", function (e) {
  e.preventDefault();
  var userMessage = $("#user-message").val();
  $.post("/bot", { user_message: userMessage }, function (botMessage) {
    $("#chatbox").append(
      "<div class='outgoing'><div class='bubble'><strong>Tú: </strong>" +
      userMessage +
      "</div></div>"
    );
    if (botMessage.trim() !== "") {
      $("#chatbox").append(
        "<div class='incoming'><div class='bubble'><strong>Bot: </strong>" +
          botMessage +
          "</div></div>"
      );
      }
      $("#chatbox").scrollTop($("#chatbox")[0].scrollHeight);
  });
  $("#user-message").val("");
});
