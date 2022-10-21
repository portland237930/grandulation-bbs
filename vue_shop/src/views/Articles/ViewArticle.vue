<template>
  <div class="content">
    <el-card style="width:100%">
      <h1>{{article.title}}</h1>
      <div class="personal-content">
        <img src="@/assets/bluetoothe.png">
        <span class="title">{{user.name}}</span>
        <div class="personal-text">
          <span style="margin:0px 5px 0px 20px;">于</span>
          <i style="color:#6b5458;"
             class="el-icon-time"></i>
          <span>{{article.create_time}} 发布</span>
        </div>
        <div class="vts">
          <p style="margin-left:5px;">
            <span>浏览</span>
            <i style="margin:0px 2px;"
               class="el-icon-view"></i>{{article.viewed}}</p>
        </div>
      </div>
      <div class="words">
        <div class="img-containter">
          <img style="width:100%;"
               v-for="(i,index) in imgUrl"
               :key="index"
               :src="i"
               v-show="i">
        </div>
        <span v-html="article.content"></span>
      </div>
    </el-card>
    <div v-if="commentlist"
         style="width:100%;">
      <el-card class="
         comment">
        <div slot="header">
          <h2 style="display:inline-block;">全部评论</h2>
          <span v-if="article.commentlist"
                style="display:inline-block;margin-left:5px;">{{article.commentlist.length}}</span>
          <span style="display:inline-block;margin-left:5px;"
                v-else>0</span>
        </div>
        <el-card class="viewlist"
                 v-for="c in commentlist"
                 :key="c.id"
                 shadow="hover">
          <span class="comment-owner">{{c.owner}}:</span>
          <p class="comment-content">{{c.content}}</p>
        </el-card>
        <el-pagination small
                       v-if="commentlist"
                       :pageNo="pnum"
                       :page-size="psize"
                       @current-change="pageChange"
                       layout="prev, pager, next"
                       :total="total"
                       class="pagination">
        </el-pagination>
      </el-card>
    </div>

  </div>
</template>

<script>
export default {
  name: 'ViewArticle',

  data () {
    return {
      article: {},
      commentlist: [],
      user: {},
      role: {},
      imgUrl: [],
      pnum: 1,
      psize: 4,
      total: 0
    };
  },

  mounted () {


  },
  created () {
    // 获取路由参数并收集参数
    let res = this.$qs.parse(this.$route.query.datas);
    this.article = res.article;
    this.user = res.user
    this.role = res.role
    console.log(res.article.commentlist);
    // 封面图片处理
    if (res.article.cover) {
      this.imgUrl = this.article.cover.split(',')
    }
    // 分页处理
    if (res.article.commentlist != undefined) {
      this.commentlist = res.article.commentlist
      let cnum = (this.pnum - 1) * this.commentlist.length
      this.commentlist = this.article.commentlist.slice(cnum, cnum + this.psize)
      this.total = this.article.commentlist.length
    } else {
      this.commentlist = []
    }

    console.log(this.imgUrl);
  },
  methods: {
    // 分页处理
    pageChange (data) {
      this.pnum = data
      console.log(this.pnum);
      let cnum = (this.pnum - 1) * this.commentlist.length
      this.commentlist = this.article.commentlist.slice(cnum, cnum + this.psize)
    }
  },
};
</script>

<style scoped>
.content {
  width: 75%;
  margin: 10px auto;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
}
.content >>> .el-card__body {
  width: 100%;
}
.personal-content {
  width: 100%;
  padding: 0px;
  display: flex;
  flex-wrap: wrap;
  background-color: #f4f4f4;
}
.title {
  font-size: 20px;
  width: 50px;
  height: 50px;
  display: inline-block;
  line-height: 50px;
  text-align: center;
  color: #686273;
  font-weight: bold;
}
.personal-content > img {
  width: 30px;
  height: 30px;
  margin: 10px;
}
.personal-text {
  line-height: 50px;
  font-size: 15px;
  color: #ecb0c1;
  height: 50px;
  text-align: center;
}
.vts {
  font-size: 15px;
  display: flex;
  color: #ecb0c1;
}
.vts p {
  height: 100%;
  line-height: 20px;
}
.img-containter {
  width: 100%;
  margin: 20px 0px;
}
.img-containter img {
  width: 80%;
  margin: 0 auto;
}
.comment {
  width: 100%;
  float: left;
  margin: 30px 0px;
}
.viewlist {
  width: 90%;
  animation-name: fadeIn; /*fadeInLeft为要使用的动画效果名，在这里不需要加animate前缀*/
  animation-duration: 1s; /*这里设定完成该动画的时间*/
  margin-bottom: 15px;
  float: left;
}
.comment-owner {
  font-size: 18px;
  display: inline-block;
  width: 100%;
  font-weight: bold;
}
.comment-content {
  font-size: 13px;
  overflow: hidden;
  width: 100%;
}
.pagination {
  width: 100%;
  float: left;
}
</style>