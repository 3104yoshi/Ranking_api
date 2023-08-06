<template>
    <div class="container">
    <h2>Login</h2>
    <form action="/authentification/Login" method="POST">
      <div class="canLogin"></div>
      <label  for="username">Username:</label>
      <input type="text" id="username" name="username" required>

      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required>

      <input type="submit" value="Login" id="login">
    </form>
    <form action="/authentification/Signup" method="GET" >
      <input type="submit" value="Sign up" id="signup">
    </form>
  </div>
</template>
