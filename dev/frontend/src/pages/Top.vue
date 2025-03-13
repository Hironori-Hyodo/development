<script setup lang="ts">
import { ref } from "vue";

defineProps(["sheetsData"]);

const selectedWorkbook = ref<string | null>(null);
const selectedSheet = ref<string | null>(null);

const setSelectedSheet = (workbookName: string, sheetName: string) => {
  selectedWorkbook.value = workbookName;
  selectedSheet.value = sheetName;
};
</script>

<template>
  <main class="main">
    <div class="main__wrapper">
      <table class="main__table">
        <thead>
          <tr>
            <th>データ名</th>
            <th>更新日</th>
            <th>スクショ</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="sheet in sheetsData"
            :key="`${sheet.workbook_name}_${sheet.sheet_name}`"
          >
            <td>
              <button
                @click="setSelectedSheet(sheet.workbook_name, sheet.sheet_name)"
              >
                {{ sheet.sheet_name }}
              </button>
            </td>
            <td>
              {{ sheet.update_date }}
            </td>
            <td>
              <img
                v-if="selectedWorkbook && selectedSheet"
                :src="`http://localhost:8080/api/screenshot/${selectedWorkbook}/${selectedSheet}`"
                alt="Excel Screenshot"
              />
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
