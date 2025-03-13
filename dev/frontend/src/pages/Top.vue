<script setup lang="ts">
defineProps(["sheetsData"]);
</script>

<template>
  <main class="main">
    <div class="main__wrapper">
      <table class="main__table">
        <thead>
          <tr>
            <th>データ名</th>
            <th>更新日</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="sheet in sheetsData" :key="sheet.sheet_name">
            <td>
              <button>{{ sheet.sheet_name }}</button>
            </td>
            <td>
              {{ sheet.update_date }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </main>
</template>

<style scoped>
.main {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  margin-bottom: 1.5rem;
  width: 100%;
  height: 100%;
  min-height: 800px;
  opacity: 0.5;
}

.main__wrapper {
  padding-top: 2rem;
  padding-left: 1rem;
}

.main__table {
  color: var(--color-white);
}
</style>
