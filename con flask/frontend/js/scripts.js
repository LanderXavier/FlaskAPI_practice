$('#loginForm').submit(function (e) {
  e.preventDefault();
  const email = $('#email').val();
  const password = $('#password').val();
  $.ajax({
      url: 'http://127.0.0.1:5000/api/auth/login', // Your login API endpoint
      type: 'POST',
      contentType: 'application/json', // Content type is JSON
      data: JSON.stringify({ email, password }), // Send data as JSON in the body
      success: function (response) {
          console.log('Login successful:', response);
          localStorage.setItem('token', response.access_token); // Guarda el token en localStorage
          window.location.href = 'index.html'; // Redirige al usuario
      },
      error: function (error) {
          console.error('Login failed:', error);
          alert('Error al iniciar sesión. Verifica tus credenciales.');
      }
  });
});
  
$('#loadTasks').click(function () {
    const token = localStorage.getItem('token'); // Obtén el token almacenado
    if (!token) {
        alert('No estás autenticado. Por favor, inicia sesión.');
        return;
    }

    $.ajax({
        url: 'http://127.0.0.1:5000/api/tasks', // Tu endpoint de tareas
        type: 'GET',
        headers: {
            Authorization: `Bearer ${token}` // Incluye el token en el encabezado
        },
        success: function (data) {
            $('#taskList').empty();
            data.tasks.forEach(function (task) {
                $('#taskList').append(`<li class="list-group-item">${task.title}</li>`);
            });
        },
        error: function (error) {
            console.error('Error al cargar las tareas:', error);
            alert('No se pudieron cargar las tareas. Verifica tu autenticación.');
        }
    });
});