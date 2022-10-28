import * as Vue from 'vue'
export default [
  {
    path: '/',
    redirect: '/discuss',
  },
  {
    path: '/userlogin',
    name: 'userlogin',
    component: Vue.defineAsyncComponent(() => import('@/views/UserLogin.vue')),
    meta: {
      showHeader: false,
    },
  },
  {
    path: '/userregister',
    name: 'userregister',
    component: Vue.defineAsyncComponent(() => import('@/views/UserRegister')),
    meta: {
      showHeader: false,
    },
  },
  {
    path: '/discuss',
    name: 'discuss',
    component: Vue.defineAsyncComponent(() => import('@/views/Discuss')),
    meta: {
      showHeader: true,
    },
  },
  {
    path: '/search',
    name: 'search',
    component: Vue.defineAsyncComponent(() => import('@/views/Search')),
    meta: {
      showHeader: true,
    },
  },
  {
    path: '/account',
    name: 'account',
    component: Vue.defineAsyncComponent(() => import('@/views/Account')),
    meta: {
      showHeader: true,
    },
    children: [
      {
        path: 'personal',
        component: Vue.defineAsyncComponent(
          () => import('@/views/Account/Personal.vue')
        ),
        meta: {
          showHeader: true,
        },
      },
      {
        path: 'ownerarticle',
        name: 'ownerarticle',
        component: Vue.defineAsyncComponent(
          () => import('@/views/Account/OwnerArticle')
        ),
        meta: {
          showHeader: true,
        },
      },
      {
        path: '/account',
        redirect: '/account/personal',
      },
      {
        path: 'ownercomments',
        name: 'ownercomments',
        component: Vue.defineAsyncComponent(
          () => import('@/views/Account/OwnerComments')
        ),
        meta: {
          showHeader: true,
        },
      },
    ],
  },
  {
    path: '/publishart',
    name: 'publishart',
    component: Vue.defineAsyncComponent(() => import('@/views/PublishArt')),
    meta: {
      showHeader: false,
    },
  },
  {
    path: '/viewarticle',
    name: 'viewarticle',
    component: Vue.defineAsyncComponent(
      () => import('@/views/Articles/ViewArticle')
    ),
    meta: {
      showHeader: true,
    },
  },
  {
    path: '/editarticle',
    name: 'editarticle',
    component: Vue.defineAsyncComponent(
      () => import('@/views/Articles/EditArticle')
    ),
  },
]
