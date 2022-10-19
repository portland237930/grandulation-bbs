<template>
  <div>
    <el-menu :default-active="activeIndex"
             class="el-menu-demo"
             mode="horizontal"
             @select="handleSelect"
             background-color="#545c64"
             text-color="#fff"
             active-text-color="#ffd04b">
      <el-menu-item index="1">首页</el-menu-item>
      <el-menu-item index="2">社区</el-menu-item>
      <el-menu-item index="3">使用手册</el-menu-item>
      <el-menu-item index="4">购买</el-menu-item>
      <el-submenu index="5">
        <template slot="title">我的
        </template>
        <el-menu-item index="6-1">个人设置</el-menu-item>
        <el-menu-item index="6-2">我的帖子</el-menu-item>
        <el-menu-item index="6-3">退出登录</el-menu-item>
      </el-submenu>
      <el-menu-item style="float:right;"
                    index="7">发布帖子</el-menu-item>
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
    };
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
          address = '/home'
          break;
        case '2':
          address = '/recommended'
          break;
        case '6-1':
          address = '/account'
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
    this.handleSelect()
  },
  activated () {

  },
};
</script>

<style lang="scss" scoped>
</style>