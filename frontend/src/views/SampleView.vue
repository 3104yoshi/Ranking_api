<script setup>
import LoginView from './LoginView.vue';
import SignupView from './SignupView.vue';
let isLogin = true;

function switchLoginOrSignup() {
  isLogin = !isLogin;
}
</script>

<template>
  <div>
    <button @click="switchLoginOrSignup">Switch</button>
    <component :is="isLogin ? LoginView : SignupView" />
  </div>
</template>
