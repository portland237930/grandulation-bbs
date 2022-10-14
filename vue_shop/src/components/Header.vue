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

  <el-menu-item index="1">首页</el-menu-item>
  <el-menu-item index="2">每日推荐</el-menu-item>
  <el-submenu index="3">
    <template slot="title">我的</template>
    <el-menu-item index="2-1">账户管理</el-menu-item>
    <el-menu-item index="2-2">设置</el-menu-item>
    <el-menu-item index="2-3">我的帖子</el-menu-item>
  </el-submenu>
  <el-menu-item index="4">消息中心</el-menu-item>
</el-menu>
	</div>
</template>

<script>
export default {
	name: 'Header',
	    data() {
      return {
        activeIndex: '1',
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
};
</script>

<style lang="scss" scoped>

</style>