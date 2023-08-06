import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SampleView from "../views/SampleView.vue";
import CanSignupView from "../views/CanSignupView.vue";
import LoginView from "../views/LoginView.vue";
import SignupView from "../views/SignupView.vue";
import NotFoundView from "../views/NotFoundView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/sample",
    name: "sample",
    // component: () => import(/* webpackChunkName: "sample" */ '../views/SampleView.vue')
    component: SampleView,
  },
  {
    path: "/authentification/login",
    name: "Login",
    // component: () => import(/* webpackChunkName: "sample" */ '../views/SampleView.vue')
    component: LoginView,
  },
  {
    path: "/authentification/signup",
    name: "Signup",
    // component: () => import(/* webpackChunkName: "sample" */ '../views/SampleView.vue')
    component: SignupView,
  },
  {
    path: "/authentification/CanSignup/:True",
    component: CanSignupView,
  },
  {
    path: "/authentification/CanSignup/:False",
    component: CanSignupView,
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
