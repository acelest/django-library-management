$(document).ready(function() {
    // Validation du formulaire d'enregistrement
    $('#register').validate({
      rules: {
        first_name: {
          required: true
        },
        last_name: {
          required: true
        },
        email: {
          required: true,
          email: true
        },
        city: {
          required: true
        },
        age: {
          required: true,
          digits: true
        },
        gender: {
          required: true
        },
        photo: {
          required: true,
          accept: "image/*"
        },
        password: {
          required: true,
          minlength: 6
        }
      },
      messages: {
        first_name: {
          required: "Veuillez saisir votre prénom"
        },
        last_name: {
          required: "Veuillez saisir votre nom"
        },
        email: {
          required: "Veuillez saisir votre adresse e-mail",
          email: "Veuillez saisir une adresse e-mail valide"
        },
        city: {
          required: "Veuillez saisir votre ville"
        },
        age: {
          required: "Veuillez saisir votre âge",
          digits: "Veuillez saisir un nombre entier"
        },
        gender: {
          required: "Veuillez sélectionner votre sexe"
        },
        photo: {
          required: "Veuillez sélectionner une photo",
          accept: "Veuillez sélectionner une image"
        },
        password: {
          required: "Veuillez saisir votre mot de passe",
          minlength: "Le mot de passe doit contenir au moins 6 caractères"
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
        // Envoi du formulaire via AJAX ou autre traitement
        // Exemple avec redirection vers la page des livres après inscription
        Swal.fire({
          title: "Inscription réussie",
          text: "Vous êtes maintenant inscrit",
          icon: "success"
        }).then(function() {
          form.submit(); // Soumettre le formulaire
        });
      }
    });
  
    // Initialisation de la fonctionnalité Drop and Drag pour les fichiers
    $('.dropzone').on('dragover', function() {
      $(this).addClass('dragover');
    });
  
    $('.dropzone').on('dragleave', function() {
      $(this).removeClass('dragover');
    });
  });
  