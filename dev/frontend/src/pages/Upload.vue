<script setup lang="ts">
import { ref } from "vue";

const fileInput = ref<HTMLInputElement | null>(null);
const fileList = ref<File[]>([]); // ファイルのリスト

// アップロードボタンをクリックしたら file input を開く
const selectFiles = () => {
  fileInput.value?.click();
};

// ファイルが選択されたときの処理
const handleFileUpload = (event: Event) => {
  const target = event.target as HTMLInputElement;
  if (target.files?.length) {
    fileList.value = [...fileList.value, ...Array.from(target.files)]; // 配列に追加
  }

  console.log(
    "現在のファイルリスト:",
    fileList.value.map((file) => file.name)
  );
};

// ファイルをアップロード
const uploadFiles = async () => {
  if (fileList.value.length === 0) {
    alert("アップロードするファイルを選択してください。");
    return;
  }

  const formData = new FormData();
  fileList.value.forEach((file) => {
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

    alert("アップロードが成功しました！");
    fileList.value = []; // 成功後、リストをクリア
  } catch (error: any) {
    console.error("アップロードエラー:", error);
    alert(error.message);
  }
};

// ファイルをリストから削除
const removeFile = (index: number) => {
  fileList.value.splice(index, 1);
};
</script>

<template>
  <main class="main">
    <h1 class="title">アップロード</h1>
    <div class="upload">
      <div class="input-area">
        <p>ドラッグ & ドロップでファイルを追加</p>
      </div>
      <input
        type="file"
        ref="fileInput"
        @change="handleFileUpload"
        multiple
        style="display: none"
      />

      <button type="button" class="upload__btn" @click="selectFiles">
        デバイスからアップロード
      </button>

      <!-- ファイルリスト -->
      <ul v-if="fileList.length" class="file-list">
        <li v-for="(file, index) in fileList" :key="index">
          {{ file.name }}
          <button class="remove-btn" @click="removeFile(index)">削除</button>
        </li>
      </ul>

      <!-- アップロードボタン -->
      <button
        type="button"
        class="upload__btn upload-action"
        @click="uploadFiles"
      >
        アップロード
      </button>
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

.title {
  color: var(--color-white);
  margin-top: 1rem;
  margin-left: 2.5rem;
}

.input-area {
  margin-top: 2rem;
  margin-left: 4rem;
  width: 60%;
  height: 400px;
  border-radius: 12px;
  background-color: var(--color-white);
  display: flex;
  align-items: center;
  justify-content: center;
}

.input-area > p {
  font-size: 1.4rem;
}

.upload__btn {
  width: 30%;
  padding: 1rem 0;
  margin-top: 1.5rem;
  margin-left: 4rem;
  border-radius: 6px;
  font-size: 1.1rem;
  border: 1px solid var(--color-white);
}

.upload-action {
  background-color: var(--color-blue);
  color: white;
}

.file-list {
  margin-top: 1.5rem;
  margin-left: 4rem;
  padding: 0;
  list-style-type: none;
  color: var(--color-white);
}

.file-list li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.5rem;
  border-bottom: 1px solid var(--color-white);
}

.remove-btn {
  background-color: red;
  color: white;
  border: none;
  padding: 0.3rem 0.6rem;
  cursor: pointer;
  border-radius: 4px;
}

.remove-btn:hover {
  background-color: darkred;
}
</style>
