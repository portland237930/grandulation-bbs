<template>
  <div id="app">
    <el-backtop></el-backtop>
    <Header id="header"
            isLogin="isLogin"
            v-show="$route.meta.showHeader" />
    <router-view />
  </div>
</template>
<script>
import Header from './components/Header.vue'
import { getToken } from "./utils/Token"
export default {
  data () {
    return {
      isLogin: false
    }
  },
  components: {
    Header,
  },
  methods: {
  },
  mounted () {

  },
}
</script>
<style>
#app {
}
.login {
  animation-name: rotateIn;
  animation-duration: 1s;
}
.logout {
  animation-name: rotateOut;
  animation-duration: 1s;
}
</style>
