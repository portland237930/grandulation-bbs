<template>
  <div>
    <el-card class="content">
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
  </div>
</template>

<script>
export default {
  name: 'ViewArticle',

  data () {
    return {
      article: {},
      user: {},
      role: {},
      imgUrl: []
    };
  },

  mounted () {
    // 获取路由参数并收集参数
    let res = this.$qs.parse(this.$route.query.datas);
    this.article = res.article;
    this.user = res.user
    this.role = res.role
    if (res.article.cover) {
      this.imgUrl = this.article.cover.split(',')
    }
    console.log(this.imgUrl);

  },

  methods: {

  },
};
</script>

<style scoped>
.content {
  width: 75%;
  margin: 10px auto;
  display: flex;
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
</style>