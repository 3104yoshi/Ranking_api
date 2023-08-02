<template>
    <div class="container">
    <h2>Login</h2>
    <form method="POST" action="/authentification/Signup">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required>

      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required>

      <input type="submit" value="Sign up" id="login">
    </form>
  </div>
</template>
