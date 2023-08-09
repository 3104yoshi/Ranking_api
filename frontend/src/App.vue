<template>
  <div>
    <router-link v-bind:to="{name: 'home'}">
      <div id="logo-img">
        <img src="./assets/logo.jpg">
      </div>
    </router-link>
    <router-view/>
  </div>
</template>

<style>
#logo-img {
  display: flex;
  justify-content: center;
  align-items: center;
}

img {
  width: 10%;
  height: auto;
}

</style>