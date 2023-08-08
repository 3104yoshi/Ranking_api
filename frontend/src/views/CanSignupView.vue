<script setup>
import { defineOptions } from 'vue';
import { useRoute } from "vue-router";

defineOptions({
  inheritAttrs: false
})

const route = useRoute();
const SignupStatus = route.params.SignupStatus
</script>

<template>
    <div class="container">
    <h2>{{ SignupStatus }}</h2>
    <a href="/auth/Login">Loginページに戻る</a>
  </div>
</template>
