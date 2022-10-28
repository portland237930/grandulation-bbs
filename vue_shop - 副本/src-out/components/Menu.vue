<template>
  <div>
    <i class="el-icon-s-operation menu-item" @click="openMenu"></i>
    <el-drawer
      title="我是标题"
      direction="btt"
      class="drawer"
      size="15%"
      v-model:visible="drawer"
      :with-header="false"
    >
      <span class="el-icon-menu"></span>
      <el-button
        class="pub-btn"
        type="primary"
        v-show="type == 'publish'"
        @click="pubArticle"
        >发布博客</el-button
      >
      <el-button type="success" @click="compEdit" v-show="type == 'edit'"
        >完成编辑</el-button
      >
      <el-button class="pub-btn" type="primary" @click="BackHome"
        >取消</el-button
      >
    </el-drawer>
  </div>
</template>

<script>
import { $on, $off, $once, $emit } from '../utils/gogocodeTransfer'
import { getUid } from '@/utils/Token'
export default {
  name: 'Menu',
  props: [
    // 'content',
    // "imgs",
    // 'title',
    'type',
  ],
  components: {},
  data() {
    return {
      datas: {
        aid: 0,
        title: '',
        imgs: '',
        content: '',
      },
      drawer: false, // 展开菜单栏标志
    }
  },
  computed: {},
  watch: {
    // 监视组件
    // imgs: function (newval, oldval) {
    //   this.datas.imgs = newval
    // },
    // content: function (newval, oldval) {
    //   this.datas.content = newval
    // },
    // title: function (newval, oldval) {
    //   this.datas.title = newval
    // },
  },
  created() {
    var that = this
    $on(this.$bus, 'title', (data) => {
      that.datas.title = data
    })
    $on(this.$bus, 'content', (data) => {
      that.datas.content = data
    })
    $on(this.$bus, 'imgs', (data) => {
      that.datas.imgs += data
    })
  },
  mounted() {
    console.log('datas', this.$route.query.article)
    var that = this
    // 获取uid
    if (this.type == 'edit') this.datas.aid = this.$route.query.article.id
  },
  destoryed() {},
  methods: {
    // 发布博客功能
    async pubArticle() {
      let uid = getUid()
      // console.log(uid);
      var that = this
      let data = this.$qs.stringify({
        id: uid,
        content: that.datas.content,
        title: that.datas.title,
        cover: that.datas.imgs,
      })
      console.log(data)
      let { data: res } = await this.$axios.post('/article', data)
      console.log(res)
      if (res.status != 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      // 返回主页
      this.$router.push('/home')
    },
    // 取消发布返回页面
    BackHome() {
      this.data = {}
      this.$router.push('/home')
    },
    // 完成编辑按钮
    async compEdit() {
      let uid = getUid()
      // console.log('uid', uid);
      var that = this
      var datas = this.$qs.stringify({
        aid: that.datas.aid,
        uid: uid,
        content: that.datas.content,
        title: that.datas.title,
        cover: that.datas.imgs,
      })
      console.log(datas)
      let { data: res } = await this.$axios.put('/article', datas)
      if (res.status != 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      // 跳转回主页
      this.$router.push('/home')
    },
    // 打开菜单
    openMenu() {
      this.drawer = true
    },
  },
}
</script>

<style scoped>
.menu-item {
  font-size: 40px;
  position: fixed;
  bottom: 30px;
  left: 30px;
}
.drawer {
  float: left;
  line-height: 120px;
}
.drawer span {
  margin: 0px 50px;
  font-size: 30px;
}
</style>
