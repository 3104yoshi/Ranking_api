<script setup>
import { ref } from 'vue'
import LoginView from './LoginView.vue';
import SignupView from './SignupView.vue';
const count = ref(1)
const auth_type = ref(true)
function switch_auth() {
  auth_type.value = !auth_type.value
}
</script>

<template>
  <div class="about">
    <h1>{{ count }}</h1>
    <p>aaaaa</p>
    <LoginView v-if="auth_type"/>
    <SignupView v-else/>
    <button @click="switch_auth"></button>
  </div>
</template>
