<script setup lang="ts"></script>

<template>
  <header class="header">
    <div class="header__logo">
      <router-link to="/">
        <img src="/logo.svg" alt="A-lab Logo" />
      </router-link>
    </div>
  </header>
</template>

<style scoped>
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
</style>
