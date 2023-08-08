<template>
  <div id="home">
    <h1>ようこそ！</h1>
    <router-link v-bind:to="{ name : 'auth', params : { AuthType : 'Login' } }">
      <button class="auth-button" id="login-button">Login</button>
    </router-link>
    <router-link v-bind:to="{ name : 'auth', params : { AuthType : 'Signup' } }">
      <button class="auth-button" id="signup-button">Signup</button>
    </router-link>
  </div>
</template>

<style>
#home {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.auth-button {
  width: 200px;
  height: 50px;
  margin: 10px;
  border-radius: 5px;
  border: none;
  color: white;
  font-size: 20px;
  cursor: pointer;
}

#login-button {
  background-color: #45a049;
}

#login-button:hover {
  background-color: #3c8942;
}

#signup-button {
  background-color: #823df2;
}

#signup-button:hover {
  background-color: #6e2cc4;
}
</style>