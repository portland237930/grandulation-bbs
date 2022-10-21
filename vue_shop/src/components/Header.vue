<template>
  <div>
    <el-menu :default-active="activeIndex"
             class="el-menu-demo"
             mode="horizontal"
             @select="handleSelect"
             background-color="#ffffff"
             text-color="#2f3542"
             active-text-color="#1e90ff">
      <el-menu-item index="1">社区</el-menu-item>
      <el-menu-item index="2">学习</el-menu-item>
      <el-menu-item index="3">等你来问</el-menu-item>
      <el-submenu index="4">
        <template slot="title">我的
        </template>
        <el-menu-item index="4-1">个人设置</el-menu-item>
        <el-menu-item index="4-2">我的帖子</el-menu-item>
        <el-menu-item index="4-3">退出登录</el-menu-item>
      </el-submenu>
      <div class="input-content">
        <el-input v-model="searchContent"
                  placeholder="请输入关键字"></el-input>
        <el-button slot="append"
                   class="btn"
                   icon="el-icon-search"></el-button>
      </div>
    </el-menu>
  </div>
</template>

<script>
import { removeToken, getToken, removeUid } from "../utils/Token"
export default {
  name: 'Header',
  data () {
    return {
      activeIndex: '1',
      searchContent: ""
    };
  },
  watch: {
    // $route(to,from){
    //   switch (to) {
    //     case "/home":
    //       this.activeIndex = '1';
    //       break;
    //     case ""
    //   }
    // }
  },
  computed: {
  },
  methods: {
    handleSelect (key) {
      this.activeIndex = key
      console.log(key);
      let address = ''
      // 根据索引进入页面
      switch (key) {
        case "1":
          address = '/discuss'
          break;
        case '2':
          address = '/discuss'
          break;
        case '3':
          address = '/publishArt'
          this.activeIndex = '1'
          break;
        case '6-2':
          address = '/account/ownerarticle'
          break
        case '6-3':
          // 删除Token
          removeToken()
          // 删除Uid
          removeUid()
          // 返回登录界面
          address = '/userlogin'
          break;
        case '5':
          address = '/userlogin'
          break;
        case '7':
          address = '/publishArt'
          this.activeIndex = '1'
        default:
          break;
      }
      this.$router.push(address)
    },
  },
  created () {

  },
  mounted () {
    // this.handleSelect()
  },
  activated () {

  },
};
</script>

<style scoped>
.el-menu-demo {
  width: 100%;
  margin: 0 auto;
}
.el-menu-demo .el-menu-item:first-child {
  margin-left: 220px;
}
.input-content {
  float: right;
  display: flex;
  height: 61px;
  margin-right: 300px;
  line-height: 61px;
}
.el-button {
  border: none;
}
.el-button:hover {
  background-color: #fff;
}
</style>