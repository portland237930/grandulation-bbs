<template>
	<div>
<el-menu
  :default-active="activeIndex"
  class="el-menu-demo"
  mode="horizontal"
  @select="handleSelect"
  background-color="#aed0ee"
  text-color="#1e2732"
  active-text-color="#6f94cd">

  <el-menu-item index="1">博客</el-menu-item>
  <el-menu-item index="2">社区</el-menu-item>
  <el-menu-item index=3 v-show="!isLogin">登录/注册</el-menu-item>
  <el-submenu index="4" v-show="isLogin">
    <template slot="title">我的
    </template>
    <el-menu-item index="2-1">个人设置</el-menu-item>
    <el-menu-item index="2-2">我的帖子</el-menu-item>
    <el-menu-item index="2-4">退出登录</el-menu-item>
  </el-submenu>
  <el-menu-item index="5">发布帖子</el-menu-item>
</el-menu>
	</div>
</template>

<script>
import {removeToken,getToken} from "../utils/Token"
export default {
	name: 'Header',
	    data() {
      return {
        activeIndex: '1',
        isLogin:false
      };
    },
    methods: {
      handleSelect(key) {
        console.log(key);
        // 根据索引进入页面
        switch (key) {
          case "1":
            this.$router.push('/home')
            break;
          case '2':
            this.$router.push("/recommended")
            break;
          case '2-1':
            this.$router.push("/account")
            break;
          case '2-2':
            this.$router.push("/personal")
          case '2-4':
            // 删除Token
            removeToken()
            // 返回登录界面
            this.$router.push("/userlogin")
            break;
          case '3':
            this.$router.push("/userlogin")
            break;
          default:
            break;
        }
      },
    },
    created() {
      this.isLogin=getToken()?true:false
    },
};
</script>

<style lang="scss" scoped>

</style>