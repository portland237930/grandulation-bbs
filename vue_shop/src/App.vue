<template>
  <div id="app"
       :style="autoHeight">
    <el-backtop></el-backtop>

    <vue-particles class="app_bg"
                   color="#333333"
                   :particleOpacity="0.7"
                   :particlesNumber="100"
                   shapeType="circle"
                   :particleSize="4"
                   linesColor="#333333"
                   :linesWidth="1"
                   :lineLinked="true"
                   :lineOpacity="0.4"
                   :linesDistance="70"
                   :moveSpeed="5"
                   :hoverEffect="true"
                   hoverMode="grab"
                   :clickEffect="true"
                   clickMode="push">
    </vue-particles>
    <Header id="header"
            v-show="$route.meta.showHeader" />
    <!-- 

 -->

    <router-view class="router" />
    <aplayer :music="audio[0]"
             style="z-index:1;position:fixed;bottom:0px;right:0px;"
             :mini="!ismini"
             @mouseenter.native="openList"
             @mouseleave.native="leavelist"
             :list="audio"
             :showlrc="true"></aplayer>
  </div>
</template>
<script>
import Header from './components/Header.vue'
import { getToken } from "./utils/Token"
import aplayer from "vue-aplayer";
import debounce from 'lodash.debounce'
let winowHeight = parseInt(window.outerHeight)
export default {
  data () {
    return {
      isLogin: false,
      ismini: false,
      autoHeight: {
        height: ''
      },
      audio: [
        {
          title: '写在风中的信',
          artist: 'Seiao',
          url: 'http://music.163.com/song/media/outer/url?id=1961053898.mp3',
          pic: 'http://p1.music.126.net/qAsUzd_XI7GvoypYhYHcdA==/109951167213554822.jpg',
        },
        {
          title: 'welcome to Wanderland',
          artist: 'Anson Seabra',
          url: 'http://music.163.com/song/media/outer/url?id=552060841.mp3',
          pic: "http://p2.music.126.net/s_W9YMEaOb6QrfDkVfpcaA==/109951164570331389.jpg",
        },
        {
          title: 'City',
          artist: '羽肿',
          url: 'http://music.163.com/song/media/outer/url?id=451319227.mp3',
          pic: 'http://p2.music.126.net/XQlI-cyn4ip07RGt1Fqqcw==/109951162837149540.jpg', // prettier-ignore
        },
        {
          title: "I'll Be Wating...(CxM Edit)'",
          artist: 'CxM-Earth_Crack',
          url: 'http://music.163.com/song/media/outer/url?id=451319227.mp3',
          pic: "http://p2.music.126.net/9GeUw49VovpPPfu6xHhZVQ==/109951167869058145.jpg",
        },
      ],
    }
  },
  components: {
    Header,
    aplayer,

  },
  methods: {
    getHeight () {
      this.autoHeight.height = (windowHeight + 110) + 'px';
    },
    openList: debounce(function () {
      this.ismini = true;
    }, 200),
    leavelist: debounce(function () {
      this.ismini = false;
    }, 200),
    // 防抖函数
    debounce (fn, wait) {
      var timer = null;
      return function () {
        if (timer !== null) {
          clearTimeout(timer);
        }
        timer = setTimeout(fn, wait);
      }
    }
  },
  mounted () {

  },
}
</script>
<style>
</style>
