export default [
    {
        path:"/",
        redirect: "/userlogin"
    },
    {
        path: '/home',
        name: 'home',
        meta: {
            showHeader: true
        },
        component: () =>
            import ("@/views/HomeView")
    },
    {
        path: "/userlogin",
        name: "userlogin",
        component: () =>
            import ("@/views/UserLogin"),
        meta: {
            showHeader: false
        }
    },
    {
        path: "/userregister",
        name: "userregister",
        component: () =>
            import ("@/views/UserRegister"),
        meta:{
            showHeader:false
        }
    },
    {
        path:"/account",
        name:"account",
        component:()=>
            import ("@/views/Account"),
        meta:{
            showHeader:true
        },
        children:[
            {
                path:"personal",
                component:()=>
                import ("@/views/Account/Personal.vue"),
                meta:{
                 showHeader:true
                },
            },
            {
                path:"ownerarticle",
                name:"ownerarticle",
                component:()=>
                import ("@/views/Account/OwnerArticle"),
                meta:{
                    showHeader:true
                },
            },
            {
                path:"/account",
                redirect:"/account/personal"
            }
        ]
    }
]