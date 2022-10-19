<template>
  <div id="app">
    <el-backtop></el-backtop>

    <vue-particles class="login-bg"
                   color="#39AFFD"
                   :particleOpacity="0.7"
                   :particlesNumber="200"
                   shapeType="circle"
                   :particleSize="4"
                   linesColor="#8DD1FE"
                   :linesWidth="1"
                   :lineLinked="true"
                   :lineOpacity="0.4"
                   :linesDistance="70"
                   :moveSpeed="7"
                   :hoverEffect="true"
                   hoverMode="grab"
                   :clickEffect="true"
                   clickMode="push">
    </vue-particles>
    <Header id="header"
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
</style>
