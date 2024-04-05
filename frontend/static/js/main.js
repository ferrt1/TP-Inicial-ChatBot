var socket = io.connect('https://f20e-2800-810-469-744-bcd6-1c5c-cc58-7cd9.ngrok-free.app');
var my_user_id;


$.get("/user_id", function(data) {
  my_user_id = data.user_id;
  console.log(my_user_id)
});

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


socket.on('admin_response', function(msg) {
  if (msg.user_id === my_user_id && msg.message.trim() !== "") {
      $("#chatbox").append(
          "<div class='incoming'><div class='bubble'><strong>Admin: </strong>" +
          msg.message +
          "</div></div>"
      );
      $("#chatbox").scrollTop($("#chatbox")[0].scrollHeight);
  }
});