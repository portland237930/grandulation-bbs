import Vue from "vue";
import App from "./App.vue";
import router from "./router";
Vue.config.productionTip = false;
// 引入axios
import axios from "axios";
// 设置一个请求的拦截器，来设置token
axios.interceptors.request.use((config) => {
    // 获取token，sessionStorage
    const tokenStr = window.sessionStorage.getItem("token");
    if (tokenStr) {
        config.headers.token = tokenStr;
    }
    return config;
});
// 设置一个响应的拦截器,来处理token是否有效，如果无效，就跳转登录页面，有效继续操作
axios.interceptors.response.use((response) => {
    if (response.data.status === 10016 || response.data.status === 10017) {
        window.sessionStorage.removeItem("token");
        // 跳转到登录页面
        router.replace({
            path: "/login",
        });
    }
    return response;
});

import * as API from "@/api";
import "./assets/css/global.css";
// 引用elementUI
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
// 引入qs
import qs from "qs";
Vue.prototype.$qs = qs;
Vue.use(ElementUI);
// 引入animation
import animated from "animate.css";
Vue.use(animated);
// 引入粒子背景
import VueParticles from "vue-particles";
Vue.use(VueParticles);
// 引入swiper
// 注册轮播图为全局组件
import Swiper from "swiper";
import "swiper/dist/css/swiper.css";
// 引入控制台
import * as fundebug from "fundebug-javascript";
import FundebugVue from "fundebug-vue";
fundebug.apikey =
    "37e494002c1cca977a1edc1221ff8edf6b11a1af1785698ae2d91d885c9265f3";
new FundebugVue(fundebug).installVueErrorHandler(Vue); // Vue 2.x
// 初始化程序
new Vue({
    router,
    render: (h) => h(App),
    beforeCreate() {
        Vue.prototype.$bus = this;
        Vue.prototype.$API = API;
        Vue.prototype.$axios = axios;
    },
}).$mount("#app");