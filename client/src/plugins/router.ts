import Vue from "vue";
import VueRouter, {RouteConfig} from "vue-router";
import Main from "@/views/Main.vue";
import {default as GitHub} from "@/views/GitHub.vue";
import {default as ISS} from "@/views/ISS.vue";
import {default as Jokes} from "@/views/Jokes.vue";
import {default as Quotes} from "@/views/Quotes.vue";
import {default as HackerNews} from "@/views/HackerNews.vue";
import {default as Todo} from "@/views/Todo.vue";
import {default as Demo} from "@/views/Demo.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    component: Main,
  },
  {
    path: "/todo",
    component: Todo,
  },
  {
    path: "/home",
    component: Main,
  },
  {
    path: "/github",
    component: GitHub,
  },
  {
    path: "/ISS",
    component: ISS,
  },
  {
    path: "/jokes",
    component: Jokes
  },
  {
    path: "/quotes",
    component: Quotes
  },
  {
    path: "/news",
    component: HackerNews
  },
  {
    path: "/help",
    component: Demo
  }
];

export default new VueRouter({
  routes,
});
