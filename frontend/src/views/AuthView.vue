<script setup>
import { defineOptions } from 'vue';
import LoginView from './LoginView.vue';
import SignupView from './SignupView.vue';
import { useRoute } from "vue-router";

defineOptions({
  inheritAttrs: false
})

const route = useRoute();
const AuthType = route.params.AuthType
let isLogin = AuthType === 'Login'

</script>

<template>
  <LoginView v-if="isLogin"/>
  <SignupView v-else />
</template>
