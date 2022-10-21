<template>
  <div id="app"
       :style="autoHeight">
    <el-backtop></el-backtop>

    <vue-particles class="app_bg"
                   color="#dfe4ea"
                   :particleOpacity="0.7"
                   :particlesNumber="200"
                   shapeType="circle"
                   :particleSize="4"
                   linesColor="#dfe4ea"
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
    <router-view class="router" />

  </div>
</template>
<script>
import Header from './components/Header.vue'
import { getToken } from "./utils/Token"
let winowHeight = parseInt(window.outerHeight)
export default {
  data () {
    return {
      isLogin: false,
      autoHeight: {
        height: ''
      }
    }
  },
  components: {
    Header,
  },
  methods: {
    getHeight () {
      this.autoHeight.height = (windowHeight + 110) + 'px';
    },
  },
  mounted () {

  },
}
</script>
<style>
</style>
