<script setup lang="ts">
import { ref } from "vue";
import HeaderComponent from "./components/organism/header/HeaderComponent.vue";

type SheetsData = {
  sheet_name: string;
  update_date: string;
};

const sheetsData = ref<SheetsData[]>([]);
const fileInput = ref<HTMLInputElement | null>(null);

// アップロードボタンが押されたら file input を開く
const selectFiles = () => {
  fileInput.value?.click();
};

// ファイルが選択されたときの処理（選択後すぐにアップロード）
const handleFileUpload = async (event: Event) => {
  const target = event.target as HTMLInputElement;
  if (!target.files?.length) return;

  const fileList = Array.from(target.files);
  await uploadFiles(fileList);
};

// ファイルをアップロード（選択されたら即座に実行）
const uploadFiles = async (files: File[]) => {
  if (files.length === 0) return;

  const formData = new FormData();
  files.forEach((file) => {
    formData.append("files", file);
  });

  try {
    const response = await fetch("http://localhost:8080/api/upload", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || "アップロードに失敗しました。");
    }

    const responseData = await response.json();
    console.log(responseData);
    sheetsData.value = responseData.sheets; // データを更新

    alert("アップロードが成功しました！");
  } catch (error: any) {
    console.error("アップロードエラー:", error);
    alert(error.message);
  }
};
</script>

<template>
  <div class="wrapper">
    <HeaderComponent />

    <div class="container">
      <aside class="aside">
        <div class="img-wrapper btn-upload" @click="selectFiles">
          <img src="/upload.svg" alt="upload button" />
        </div>

        <input
          type="file"
          ref="fileInput"
          @change="handleFileUpload"
          multiple
          style="display: none"
        />

        <div class="img-wrapper btn-create">
          <img src="/create-data.svg" alt="create button" />
        </div>
      </aside>

      <div class="main">
        <router-view :sheetsData="sheetsData" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.wrapper {
  width: 100vw;
  height: 100%;
  min-height: 100vh;
  background: var(--color-main);
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
  cursor: pointer;
}

.btn-upload {
  margin-top: 0.5rem;
}

.btn-create {
  margin-top: 1rem;
}

.main {
  width: 100%;
  height: 90vh;
}
</style>
