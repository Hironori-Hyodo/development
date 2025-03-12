<script setup lang="ts">
import HeaderComponent from "./components/organism/header/HeaderComponent.vue";
</script>

<template>
  <div class="wrapper">
    <HeaderComponent />

    <div class="container">
      <aside class="aside">
        <div class="img-wrapper btn-upload">
          <router-link to="/upload">
            <img src="/upload.svg" alt="upload button" />
          </router-link>
        </div>
        <div class="img-wrapper btn-create">
          <img src="/create-data.svg" alt="create button" />
        </div>
      </aside>

      <router-view />
    </div>
  </div>
</template>

<style scoped>
.wrapper {
  width: 100vw;
  height: 100vh;
  background: var(--color-main);
}

.header {
  padding-bottom: 2rem;
}

.header__logo {
  padding-top: 2.125rem;
  padding-left: 1.5rem;
}

.header__logo > img {
  width: 12rem;
}

.container {
  display: flex;
  gap: 1.5rem;
  align-items: flex-start;
}

.aside {
  position: relative;
  left: 0;
  top: 0;
}

.img-wrapper {
  width: 13.5rem;
}

.btn-upload {
  margin-top: 0.5rem;
}

.btn-create {
  margin-top: 1rem;
}
</style>
