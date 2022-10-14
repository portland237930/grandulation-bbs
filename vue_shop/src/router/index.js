import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: "/userlogin",
        name: "userlogin",
        component: () =>
            import ("@/views/UserLogin")
    },
    {
        path:"/userregister",
        name:"userregister",
        component:()=>import("@/views/UserRegister")
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router