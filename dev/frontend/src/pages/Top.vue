<script setup lang="ts">
import { computed, ref } from "vue";
import DataViewer from "../components/organism/data-viewer/DataViewer.vue";

const props = defineProps(["sheetsData"]);
console.log(props.sheetsData);

const selectedSheet = ref<string | null>(null);
const selectedData = ref<{ updateDate: string; data: any[] } | null>(null);

// シート名のリストを取得
const sheetNames = computed(() => Object.keys(props.sheetsData));

// `v-data-table` に適した `items` を作成（updateDate を追加）
const items = computed(() =>
  sheetNames.value.map((sheetName) => ({
    name: sheetName,
    updateDate: props.sheetsData[sheetName]?.updateDate || "N/A",
  }))
);

console.log("SV", items);

// シートを選択したときの処理
const selectSheet = (
  event: PointerEvent,
  { item }: { item: { name: string } }
) => {
  selectedSheet.value = item.name;
  selectedData.value = props.sheetsData[item.name] || {
    updateDate: "N/A",
    data: [],
  };
};

// シートを閉じる
const closeSheet = () => {
  selectedSheet.value = null;
  selectedData.value = null;
};
</script>

<template>
  <main class="main">
    <div class="main__wrapper">
      <h1 class="main__title">最近のデータ</h1>
      <!-- v-data-table: シート名一覧 -->
      <v-data-table
        :items="items"
        :headers="[
          { title: 'データ名', key: 'name' },
          { title: 'データ種別', key: 'dataKind' },
          { title: 'ユーザ名', key: 'userName' },
          { title: '更新日', key: 'updateDate' },
          { title: 'データID', key: 'dataID' },
        ]"
        @click:row="selectSheet"
        class="clickable-table"
      ></v-data-table>

      <!-- 選択されたシートのデータを表示 -->
      <DataViewer
        v-if="selectedData"
        :selectedSheet="selectedSheet"
        :selectedData="selectedData.data"
        :updateDate="selectedData.updateDate"
        @close="closeSheet"
      />
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
  min-height: 300px;
  max-height: 800px;
  opacity: 0.5;
}

.main__wrapper {
  padding-top: 2rem;
  padding-left: 1rem;
  position: relative;
}

.main__title {
  color: var(--color-white);
}

.clickable-table {
  height: 100%;
  min-height: 600px;
  margin-top: 2rem;
  background-color: inherit;
  color: var(--color-white);
  table-layout: auto;
}

.clickable-table tbody tr {
  cursor: pointer;
  border-bottom: 1px solid gray;
  text-align: left;
}

.clickable-table tbody tr:hover {
  background-color: rgba(0, 150, 255, 0.2);
}

.tr--clickable {
  border-bottom: 1px solid gray !important;
}

.v-table__wrapper table tbody tr td {
  border: 1px solid var(--color-white);
}
</style>
