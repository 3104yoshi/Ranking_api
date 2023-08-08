import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CanSignupView from "../views/CanSignupView.vue";
import NotFoundView from "../views/NotFoundView.vue";
import AuthView from "../views/AuthView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/auth/:AuthType",
    name: "auth",
    component: AuthView,
    props : (route) => ({ AuthType: route.params.AuthType }),
  },
  {
    path: "/auth/CanSignup/:SignupStatus",
    name: "CanSignup",
    component: CanSignupView,
    props : (route) => ({ SignupStatus: route.params.SignupStatus }),
  },
  {
    path: "/*",
    component: NotFoundView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
