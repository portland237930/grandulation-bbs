<template>
  <div>
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#ffffff"
      text-color="#2f3542"
      active-text-color="#1e90ff"
    >
      <el-menu-item index="1">社区</el-menu-item>
      <el-menu-item index="2">学习</el-menu-item>
      <el-menu-item index="3">等你来问</el-menu-item>
      <el-submenu index="4">
        <template v-slot:title>我的 </template>
        <el-menu-item index="4-1">个人设置</el-menu-item>
        <el-menu-item index="4-2">我的帖子</el-menu-item>
        <el-menu-item index="4-3">退出登录</el-menu-item>
      </el-submenu>
      <div class="input-content">
        <el-autocomplete
          v-model:value="state"
          :fetch-suggestions="querySearchAsync"
          placeholder="请输入标题"
        ></el-autocomplete>
        <template v-slot:append>
          <el-button
            class="btn"
            @click="GoSearch"
            icon="el-icon-search"
          ></el-button>
        </template>
      </div>
    </el-menu>
  </div>
</template>

<script>
import { removeToken, getToken, removeUid } from '../utils/Token'
export default {
  name: 'Header',
  data() {
    return {
      activeIndex: '1',
      searchContent: '',
      state: '',
      restaurants: {},
      reslist: [],
    }
  },
  watch: {},
  computed: {},
  methods: {
    handleSelect(key) {
      this.activeIndex = key
      console.log(key)
      let address = ''
      // 根据索引进入页面
      switch (key) {
        case '1':
          address = '/discuss'
          break
        case '2':
          address = '/discuss'
          break
        case '3':
          address = '/publishArt'
          this.activeIndex = '1'
          break
        case '4-1':
          address = '/account/personal'
          break
        case '4-2':
          address = '/account/ownerarticle'
          break
        case '4-3':
          // 删除Token
          removeToken()
          // 删除Uid
          removeUid()
          // 返回登录界面
          address = '/userlogin'
          break
        default:
          break
      }
      this.$router.push(address)
    },
    // 去搜索页
    GoSearch() {
      console.log('front', this.searchlist)
      this.$router.push({
        path: '/search',
        query: {
          articlelist: this.$qs.stringify(this.reslist),
        },
      })
    },
    // 异步搜索
    async querySearchAsync(queryString, cb) {
      var that = this
      this.loadAll(queryString)
      console.log('resultssea', that.reslist)
      var titlelist = []
      // this.searchlist = results
      // 每隔一段时间进行搜索
      clearTimeout(this.timeout)
      this.timeout = setTimeout(() => {
        that.reslist.forEach((item) => {
          titlelist.unshift({
            value: item.title,
          })
        })
        cb(titlelist)
      }, 1000 * Math.random())
    },
    // 闭包查找相关信息
    createStateFilter(queryString) {
      return (state) => {
        return (
          state.title.toLowerCase().indexOf(queryString.toLowerCase()) === 0
        )
      }
    },
    // 获取所有文章接口
    async loadAll(queryString) {
      let { data: res } = await this.$axios.get('/getAllArticle', {
        params: {
          type: 'all',
        },
      })
      console.log(res)
      if (res.status == 200) {
        this.restaurants = res.data
        let restaurants = this.restaurants
        this.reslist = queryString
          ? restaurants.filter(this.createStateFilter(queryString))
          : restaurants
      }
    },
  },
  created() {},
  mounted() {
    // this.handleSelect()
  },
  activated() {},
}
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
