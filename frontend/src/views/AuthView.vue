<script setup>
import { defineOptions } from 'vue';
import LoginComponent from '../components/LoginComponent.vue';
import SignupComponent from '../components/SignupComponent.vue';
import { useRoute } from "vue-router";

defineOptions({
  inheritAttrs: false
})

const route = useRoute()
const AuthType = route.params.AuthType
let isLogin = AuthType === 'Login'
</script>

<template>
  <LoginComponent v-if="isLogin"/>
  <SignupComponent v-else />
</template>
