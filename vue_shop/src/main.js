import Vue from 'vue'
import App from './App.vue'
import router from './router'
Vue.config.productionTip = false
// 引入全局样式
import './assets/css/global.css'
// 引用elementUI
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

// 初始化程序
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
