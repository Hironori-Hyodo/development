<script setup lang="ts">
import { computed, defineProps } from "vue";

const props = defineProps<{
  selectedSheet: string | null;
  selectedData: any[];
  updateDate: string;
  dataKind: string;
  userName: string;
}>();

console.log("P", props);

const emit = defineEmits(["close"]);

// テーブルのカラム名（最初の行から取得）
const columns = computed(() => {
  if (props.selectedData.length === 0) return [];
  return Object.keys(props.selectedData[0]).map((col, index) =>
    col.startsWith("Unnamed:") ? `Column_${index}` : col || `Column_${index}`
  );
});
</script>

<template>
  <Transition name="slide">
    <div v-if="selectedSheet" class="selected-data">
      <button class="close-button" @click="emit('close')">>>></button>
      <h2 class="title">{{ selectedSheet }}</h2>
      <div class="info">
        <p>登録者: {{ userName }}</p>
        <p>データ種別: {{ dataKind }}</p>
        <p>更新日: {{ updateDate }}</p>
      </div>

      <table class="table" border="1">
        <tbody>
          <tr v-for="(row, index) in selectedData" :key="index">
            <td v-for="col in columns" :key="col">{{ row[col] }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </Transition>
</template>

<style scoped>
/* スライドアニメーション */
.slide-enter-active,
.slide-leave-active {
  transition: 0.3s ease-in-out;
}

.slide-enter-from {
  transform: translateX(100%);
}

.slide-leave-to {
  transform: translateX(100%);
}

/* 閉じるボタン */
.close-button {
  position: absolute;
  top: 10px;
  left: 10px;
  background-color: inherit;
  /* background: #ff5555; */
  color: white;
  border: none;
  /* padding: 5px 10px; */
  font-size: 16px;
  cursor: pointer;
  border-radius: 50%;
}

.close-button:hover {
  /* background: #ff2222; */
}

.selected-data {
  height: 100%;
  width: 60%;
  position: absolute;
  right: 0;
  top: 0;
  padding: 3rem;
  border: 1px solid #ccc;
  background: var(--color-main);
  overflow: scroll;
}

.selected-data > p {
  color: var(--color-white);
}

.title {
  font-weight: bold;
  color: var(--color-white);
}

.info {
  margin-top: 1rem;
  display: flex;
  color: var(--color-white);
  gap: 2rem;
}

.table {
  margin-top: 2rem;
  border-collapse: collapse;
  color: var(--color-white);
}

.table td,
th {
  min-width: 120px;
  height: 40px;
  min-height: 100px;
  text-align: left;
  white-space: nowrap;
}

.table th {
  text-align: center;
}
</style>
