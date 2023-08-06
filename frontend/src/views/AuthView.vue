<script setup>

// import { ref } from 'vue'
import { toRef } from 'vue';
import LoginView from './LoginView.vue';
import SignupView from './SignupView.vue';
// const count = ref(1)
// const auth_type = ref(true)
const xxx = this.$route.params.LoginOrSignup === 'Login' ? true : false
const props = defineProps(['IsLogin'])
const IsLogin = toRef(props.IsLogin)
function switch_login_or_signup() {
  IsLogin.value = !IsLogin.value
}

</script>

<template>
  <LoginView v-if="IsLogin"/>
  <SignupView v-else />
  <SignupView v-if="xxx" />
  <button @click="switch_login_or_signup"></button>
</template>
