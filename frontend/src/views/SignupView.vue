<template>
    <div class="container">
    <h2>Signup</h2>
    <!-- <div>
      <p v-if="!canSignup">そのユーザーは既に使われています</p>
    </div> -->
    <form action="POST">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required>

      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required>

      <input type="submit" value="Sign up" id="login">
    </form>
  </div>
</template>

<style>
body {
    font-family: Arial, sans-serif;
  }
  
  .container {
    width: 300px;
    margin: 0 auto;
    margin-top: 100px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  h2 {
    text-align: center;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input[type="text"],
  input[type="password"] {
    width: 100%;
    padding: 5px;
    margin-bottom: 10px;
  }
  
  input[type="submit"] {
    width: 100%;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  input[type="submit"]:hover {
    background-color: #45a049;
  }

  form {
    margin: 20px;
  }

  #login {
    background-color: #4CAF50;
  }

  #signup {
    background-color: #f59dfd;
  }

  .canLogin {
    color: crimson;
    margin-top: 20px;
    margin-bottom: 20px;
  }
  
</style>