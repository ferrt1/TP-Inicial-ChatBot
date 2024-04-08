
var userMessages = {};

var userChatboxes = {};

var socket = io.connect('https://ferrt.pythonanywhere.com');
socket.on('user_message', function(msg) {

  // solo el mensaje es "tecnico" muestro los mensajes
  if (msg.message.toLowerCase() === 'tecnico') {
    var button = $("<button>")
      .text("Responder a " + msg.user_id)
      .click(function() {
        // mostrar mensaje
        $("#admin-form").show();
        $("#admin-form").off("submit").on("submit", function(e) {
          e.preventDefault();
          var message = $("#admin-message").val();

          // agrego mensajes de usuario
          var adminMessageElement = $("<div class='outgoing'><div class='bubble'></div></div>")
            .find('.bubble')
            .text('Mensaje del administrador: ' + message)
            .end();
          userChatboxes[msg.user_id].append(adminMessageElement);

          // envio mensaje
          $.post("/admin/respond", { user_id: msg.user_id, message: message }, function(data) {
            $("#admin-message").val("");
          });
        });

        // cierro el ticket
        $("#close-ticket").click(function() {
          $.post("/admin/close", { user_id: msg.user_id }, function(data) {
              $("#admin-form").hide();
          });
        });
      });
    $("#requests").append(button);
  }

  if (!userMessages[msg.user_id]) {
    userMessages[msg.user_id] = [];
  }
  userMessages[msg.user_id].push(msg.message);

  // Crear un chatbox para el usuario si no existe
  if (!userChatboxes[msg.user_id]) {
    userChatboxes[msg.user_id] = $("<div id='chatbox' class='middle'></div>");
    $("body").append(userChatboxes[msg.user_id]);
  }

  // Mostrar los mensajes del usuario
  if (userMessages[msg.user_id]) {
    // Limpiar el chatbox
    userChatboxes[msg.user_id].empty();

    userMessages[msg.user_id].forEach(function(message) {
      var messageElement = $("<div class='incoming'><div class='bubble'></div></div>")
        .find('.bubble')
        .text('Mensaje de ' + msg.user_id + ': ' + message)
        .end();
      userChatboxes[msg.user_id].append(messageElement);
    });
  }
});
