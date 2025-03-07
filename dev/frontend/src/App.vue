<script setup lang="ts">
import { ref } from "vue";

const fileInput = ref<HTMLInputElement | null>(null);

// アップロードボタンをクリックしたら file input を開く
const upload = () => {
  fileInput.value?.click();
};

// ファイルが選択されたときの処理
const handleFileUpload = (event: Event) => {
  const target = event.target as HTMLInputElement;
  if (target.files?.length) {
    const file = target.files[0];
    console.log("選択されたファイル:", file);

    // ここでファイルをアップロードする処理を書く（例: API に送信）
  }
};
</script>

<template>
  <div class="wrapper">
    <header class="header">
      <div class="header__logo">
        <img src="/logo.svg" alt="A-lab Logo" />
      </div>
    </header>

    <div class="container">
      <aside class="aside">
        <div class="img-wrapper btn-upload">
          <img src="/upload.svg" alt="upload button" />
        </div>
        <div class="img-wrapper btn-create">
          <img src="/create-data.svg" alt="create button" />
        </div>
      </aside>

      <main class="main">
        <h1 class="title">アップロード</h1>
        <div class="upload">
          <div class="input-area" @click="upload">
            <p>ドラッグ & ドロップでファイルを追加</p>
          </div>
          <input
            type="file"
            ref="fileInput"
            @change="handleFileUpload"
            style="display: none"
          />

          <button type="button" class="upload__btn">
            デバイスからアップロード
          </button>
        </div>
      </main>
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
  width: 70%;
  height: 500px;
  border-radius: 12px;
  background-color: var(--color-white);
  display: flex;
  align-items: center;
  justify-content: center;
}

.input-area > p {
  font-size: 1.4rem;
  /* color: var(--color-white); */
}

.upload__btn {
  width: 30%;
  padding: 1rem 0;
  margin-top: 3rem;
  margin-left: 4rem;
  border-radius: 6px;
  font-size: 1.1rem;
  border: 1px solid var(--color-white);
}
</style>
