import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SampleView from "../views/SampleView.vue";
import CanSignupView from "../views/CanSignupView.vue";
import LoginView from "../views/LoginView.vue";
import SignupView from "../views/SignupView.vue";
import NotFoundView from "../views/NotFoundView.vue";
import AuthView from "../views/AuthView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/sample",
    name: "sample",
    component: SampleView,
  },
  {
    path: "/auth/:AuthType",
    name: "auth",
    component: AuthView,
    props : (route) => ({ AuthType: route.params.AuthType }),
  },
  {
    path: "/authentification/login",
    name: "Login",
    component: LoginView,
  },
  {
    path: "/authentification/signup",
    name: "Signup",
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
