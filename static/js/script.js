$(document).ready(function() {
  // Validation du formulaire de connexion
  $('#login').validate({
    rules: {
      email: {
        required: true,
        email: true
      },
      password: {
        required: true
      }
    },
    messages: {
      email: {
        required: "Veuillez saisir votre adresse e-mail",
        email: "Veuillez saisir une adresse e-mail valide"
      },
      password: {
        required: "Veuillez saisir votre mot de passe"
      }
    },
    errorClass: "text-danger",
    errorElement: "span",
    highlight: function(element) {
      $(element).addClass('is-invalid');
    },
    unhighlight: function(element) {
      $(element).removeClass('is-invalid');
    },
    errorPlacement: function(error, element) {
      error.appendTo(element.parent());
    },
    submitHandler: function(form) {
   
      $.ajax({
        url: 'http://127.0.0.1:8000/',  
        type: 'POST',
        data: $(form).serialize(),
        success: function(response) {
          if (response.success) {
            Swal.fire({
              title: "Connexion réussie",
              text: "Vous êtes maintenant connecté",
              icon: "success"
            }).then(function() {
              form.submit(); //formulaire
            });
          } else {
           
            // message d'erreur
            Swal.fire({
              title: "Erreur de connexion",
              text: "Veuillez vérifier vos informations de connexion",
              icon: "error"
            });
          }
        },
        error: function(XHR, status, error) {
          
          //  requête AJAX ici
          Swal.fire({
            title: "Erreur",
            text: "Une erreur s'est produite lors de la connexion",
            icon: "error"
          });
        }
      });
    }
  });
});
