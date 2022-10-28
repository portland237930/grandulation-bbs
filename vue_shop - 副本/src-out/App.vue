<template>
  <div id="app" :style="autoHeight">
    <el-backtop></el-backtop>

    <vue-particles
      class="app_bg"
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
      clickMode="push"
    >
    </vue-particles>
    <Header id="header" v-show="$route.meta.showHeader" />
    <!-- 

   -->

    <router-view class="router" />
    <aplayer
      :music="audio[0]"
      style="z-index: 1; position: fixed; bottom: 0px"
      :mini="ismini"
      @mouseenter="openList"
      @mouseleave="openList"
      :list="audio"
      @play="openList"
      :showlrc="true"
    ></aplayer>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import { getToken } from './utils/Token'
import aplayer from 'vue-aplayer'
import debounce from 'lodash.debounce'
let winowHeight = parseInt(window.outerHeight)
export default {
  data() {
    return {
      isLogin: false,
      ismini: true,
      autoHeight: {
        height: '',
      },
      audio: [
        {
          title: '可乐',
          artist: '黄叶',
          url: 'https://m801.music.126.net/20221022012326/a0abf1c5a959a1dcf253615d970f1e77/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/14096407730/c368/ce18/00fb/44b61082af5a2feacf70bb7340cbb7ba.m4a',
          pic: 'https://edu-guil-1010.oss-cn-beijing.aliyuncs.com/QQ%E5%9B%BE%E7%89%8720200713203148.jpg',
          lrc: '(,,•́ . •̀,,) 刚刚开始学编程的hhhh',
        },
        {
          title: '蒲空英的约定',
          artist: '黄叶',
          url: 'https://edu-guil-1010.oss-cn-beijing.aliyuncs.com/%E8%92%B2%E5%85%AC%E8%8B%B1%E7%9A%84%E7%BA%A6%E5%AE%9A.m4a',
          pic: 'https://edu-guil-1010.oss-cn-beijing.aliyuncs.com/QQ%E5%9B%BE%E7%89%8720200713203148.jpg',
          lrc: '(,,•́ . •̀,,) 刚刚开始学钢琴弹的hhhh',
        },
        {
          title: '无畏',
          artist: '马頔',
          url: 'https://edu-guil-1010.oss-cn-beijing.aliyuncs.com/%E9%A9%AC%E9%A0%94%20-%20%E6%97%A0%E7%95%8F.flac',
          pic: 'https://edu-guil-1010.oss-cn-beijing.aliyuncs.com/%E4%BB%A5%E5%AE%B6%E4%B9%8B%E5%90%8D.jpg', // prettier-ignore
          lrc: '[00:00.00] (,,•́ . •̀,,) 抱歉，当前歌曲暂无歌词',
        },
        {
          title: '蓝乐',
          artist: '白纸',
          url: 'https://edu-guil-1010.oss-cn-beijing.aliyuncs.com/%E8%93%9D%E4%B9%90%20-%20%E7%99%BD%E7%BA%B8.flac',
          pic: 'https://edu-guil-1010.oss-cn-beijing.aliyuncs.com/-1992181439.jpg',
          lrc: '[00:00.00] (,,•́ . •̀,,) 抱歉，当前歌曲暂无歌词',
        },
      ],
    }
  },
  components: {
    Header,
    aplayer,
  },
  methods: {
    getHeight() {
      this.autoHeight.height = windowHeight + 110 + 'px'
    },
    openList: debounce(function () {
      this.ismini = !this.ismini
    }, 500),
    // 防抖函数
    debounce(fn, wait) {
      var timer = null
      return function () {
        if (timer !== null) {
          clearTimeout(timer)
        }
        timer = setTimeout(fn, wait)
      }
    },
  },
  mounted() {},
}
</script>

<style></style>
