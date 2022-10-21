export default [{
        path: "/",
        redirect: "/userlogin",
    },
    {
        path: "/userlogin",
        name: "userlogin",
        component: () =>
            import ("@/views/UserLogin.vue"),
        meta: {
            showHeader: false,
        },
    },
    {
        path: "/userregister",
        name: "userregister",
        component: () =>
            import ("@/views/UserRegister"),
        meta: {
            showHeader: false,
        },
    },
    {
        path: "/discuss",
        name: "discuss",
        component: () =>
            import ("@/views/Discuss"),
        meta: {
            showHeader: true,
        },
    },
    {
        path: "/search",
        name: "search",
        component: () =>
            import ("@/views/Search"),
        meta: {
            showHeader: true,
        },
    },
    {
        path: "/account",
        name: "account",
        component: () =>
            import ("@/views/Account"),
        meta: {
            showHeader: true,
        },
        children: [{
                path: "personal",
                component: () =>
                    import ("@/views/Account/Personal.vue"),
                meta: {
                    showHeader: true,
                },
            },
            {
                path: "ownerarticle",
                name: "ownerarticle",
                component: () =>
                    import ("@/views/Account/OwnerArticle"),
                meta: {
                    showHeader: true,
                },
            },
            {
                path: "/account",
                redirect: "/account/personal",
            },
            {
                path: "ownercomments",
                name: "ownercomments",
                component: () =>
                    import ("@/views/Account/OwnerComments"),
                meta: {
                    showHeader: true,
                },
            },
        ],
    },
    {
        path: "/publishart",
        name: "publishart",
        component: () =>
            import ("@/views/PublishArt"),
        meta: {
            showHeader: false,
        },
    },
    {
        path: "/viewarticle",
        name: "viewarticle",
        component: () =>
            import ("@/views/Articles/ViewArticle"),
        meta: {
            showHeader: true,
        },
    },
    {
        path: "/editarticle",
        name: "editarticle",
        component: () =>
            import ("@/views/Articles/EditArticle"),
    },
];