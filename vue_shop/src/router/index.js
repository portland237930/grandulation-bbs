import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import {
    getToken
} from "../utils/Token";
Vue.use(VueRouter);
import routes from "./route.js";
// 重写push|replace方法,使编程式导航不会报错
// 保存Push|replace方法
let originPush = VueRouter.prototype.push;
let originReplace = VueRouter.prototype.replace;
// 重写push|replace方法,location表示要跳转的路由,resolve表示成功的回调,reject表示失败的回调
VueRouter.prototype.push = function(location, resolve, reject) {
    // 如果存在回调信息就调用push方法,如果不存在就返回回调信息
    if (resolve && reject) {
        originPush.call(this, location, resolve, reject);
    } else {
        originPush.call(
            this,
            location,
            () => {},
            () => {}
        );
    }
};
VueRouter.prototype.replace = function(location, resolve, reject) {
    if (resolve && reject) {
        originReplace.call(this, location, resolve, reject);
    } else {
        originReplace.call(
            this,
            location,
            () => {},
            () => {}
        );
    }
};

const router = new VueRouter({
    // mode: "history",
    // base: process.env.BASE_URL,
    routes,
    scrollBehavior(to, from, savedPosition) {
        // 始终滚动到顶部
        return {
            y: 0,
        };
    },
});
// 前置路由自动登录
router.beforeEach(async(to, from, next) => {
    let tokenStr = getToken("TOKEN");
    if (!tokenStr && to.name != "userlogin" && to.name != 'userregister') next("/userlogin");
    // 自动登录
    if (to.name == "userlogin" && tokenStr) {
        return next("/discuss");
    }
    next();
});

export default router;