<template>
  <div class="search-container">
    <el-card
      class="cell"
      @click="ViewArticle(a)"
      v-for="a in articlelist"
      :key="a.id"
    >
      <div class="cell-left">
        <h3>{{ a.title }}</h3>
        <div
          class="content"
          v-html="a.content.replace(/<[^>]*>/g, '').slice(1, 20) + '...'"
        ></div>
        <!-- <p>{{a.user.name}}</p> -->
        <p class="el-icon-thumb" style="margin-right: 5px">{{ a.thumb }}</p>
        <p class="el-icon-view">{{ a.viewed }}</p>
      </div>
      <div class="cell-right">
        <img v-if="a.cover.split(',')[0]" :src="a.cover.split(',')[0]" />
        <img v-else src="@/assets/hand.jpg" />
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'Search',

  data() {
    return {
      articlelist: {},
      searchContent: '',
    }
  },

  mounted() {
    // console.log('back',this.$qs.parse(this.$route.query.articlelist));
    this.articlelist = this.$qs.parse(this.$route.query.articlelist)
  },
  watch: {
    $route(to, path) {
      this.articlelist = this.$qs.parse(this.$route.query.articlelist)
    },
  },
  methods: {
    ViewArticle(article) {
      var datas = {
        article: article,
        role: article.user.role,
        user: article.user,
      }
      // 进入查看页
      this.$router.push({
        path: '/viewarticle',
        query: {
          datas: this.$qs.stringify(datas),
        },
      })
    },
  },
}
</script>

<style scoped>
.search-container {
  width: 880px;
  margin-left: 220px;
  margin-top: 20px;
}
.cell {
  width: 100%;
  padding: 18px;
  margin: 10px auto;
  height: 120px;
}
.cell .cell-left p {
  font-size: 12px;
  color: #dbe8e4;
  display: inline-block;
  margin: 0px 4px;
}
.cell-right {
  width: 20%;
  height: 100%;
  float: right;
}
.cell-left {
  width: 80%;
  height: 100%;
  float: left;
}
.cell >>> .el-card__body,
.el-main {
  width: 100%;
  height: 100%;
  padding: 0px;
}
.cell img {
  width: 100%;
  height: 100%;
  border-radius: 5px;
}
</style>
