import type { RouteRecordRaw } from 'vue-router';
import { createRouter, createWebHistory } from 'vue-router';

// ルートの型を定義
const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'top',
    component: () => import('../pages/Top.vue'),
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
