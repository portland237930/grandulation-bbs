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
            <i :style="isviewed?'margin:0px 2px;color:#e74c3c':'margin:0px 2px;'"
               class="el-icon-view"></i>{{article.viewed}}</p>
        </div>
        <div class="vts">
          <p style="margin-left:5px;">
            <span>点赞</span>
            <i style="margin:0px 2px;"
               class="el-icon-thumb"></i>{{article.thumb}}</p>
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
        <div slot="header"
             class="comment-top">
          <h2 style="display:inline-block;">全部评论</h2>
          <span class="comment-num"
                v-if="article.commentlist">{{article.commentlist.length}}</span>
          <span class="comment-num"
                v-else>0</span>

          <el-button class="el-icon-s-comment comment-btn"
                     type="info"
                     style="float:right;margin-top:20px"
                     circle
                     @click="dialogVisible=true"></el-button>
          <div class="thumb-content">
            <vue-star animate="animated bounceIn"
                      color="#F05654">
              <img @click="thumb"
                   slot="icon"
                   v-show="!isThumb"
                   src="@/assets/icon/unlike.png" />
              <img @click="thumb"
                   slot="icon"
                   v-show="isThumb"
                   src="@/assets/icon/like.png" />
            </vue-star>
          </div>

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
        <el-dialog title="提示"
                   :visible.sync="dialogVisible"
                   width="30%"
                   :before-close="handleClose">
          <el-input v-model="content"
                    placeholder="请输入评论"></el-input>
          <span slot="footer"
                class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary"
                       @click="pubComment">确 定</el-button>
          </span>
        </el-dialog>
      </el-card>
    </div>

  </div>
</template>

<script>
import VueStar from 'vue-star'
import { getUid } from "@/utils/Token.js"
export default {
  name: 'ViewArticle',
  components: {
    VueStar
  },
  data () {
    return {
      article: {},
      commentlist: [],
      user: {},
      role: {},
      imgUrl: [],
      pnum: 1,
      psize: 4,
      total: 0,
      isThumb: true,
      content: "",
      dialogVisible: false,
      isviewed: false
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
    this.getThumbStatus()
    this.ViewedStatus()
    console.log(this.imgUrl);
  },
  methods: {
    // 分页处理
    pageChange (data) {
      this.pnum = data
      console.log(this.pnum);
      let cnum = (this.pnum - 1) * this.commentlist.length
      this.commentlist = this.article.commentlist.slice(cnum, cnum + this.psize)
    },
    // 关闭对话框
    handleClose () {
      this.dialogVisible = false
      this.content = ''
    },
    // 获取评论列表
    async getCommentList () {
      const { data: res } = await this.$axios.get("/getArticleToComment", {
        params: {
          'id': this.article.id
        }
      })
      if (res.status == 200) {
        this.article.commentlist = res.data
        this.total = this.article.commentlist.length
        this.pageChange(1)
      }
    },
    // 发布评论
    async pubComment () {
      if (!this.content) return this.$message.error('请输入评论')
      var that = this
      console.log(that.article.id, that.content);

      const { data: res } = await this.$axios.post("/publishComment", this.$qs.stringify({ 'id': that.article.id, 'content': that.content }))
      console.log(res);
      if (res.status == 200) {
        this.$message.success(res.msg)
        this.dialogVisible = false
        this.getCommentList()
      }
    },
    // 点赞
    async thumb () {
      let uid = getUid()
      let aid = this.article.id
      let datas = this.$qs.stringify({
        'aid': aid,
        'uid': uid,
        'type': 'thumb'
      })
      console.log(datas)
      const { data: res } = await this.$axios.post("/addart", datas)
      if (res.status == 200) {
        this.isThumb = res.data
        this.getArticle(uid, aid)
        this.$message.success(res.msg)

      }
    },
    // 获取点赞状态
    async getThumbStatus () {
      let uid = getUid()
      let aid = this.article.id
      const { data: res } = await this.$axios.get('/thumbAndviewedstatus', {
        params: {
          'uid': uid,
          'aid': aid,
          'type': 'thumb'
        }
      })
      if (res.status == 200) {
        this.isThumb = res.data
      }
    },
    // 重新获取文章数据
    async getArticle (uid, aid) {
      const { data: res } = await this.$axios.get('/article', {
        params: {
          'type': 'only',
          'uid': uid,
          'aid': aid
        }
      })
      if (res.status == 200) {
        this.article = res.data
      }
    },
    // 获取浏览状态
    async ViewedStatus () {
      let uid = getUid()
      let aid = this.article.id
      // 获取浏览状态
      const { data: res } = await this.$axios.get('/thumbAndviewedstatus', {
        params: {
          'uid': uid,
          'aid': aid,
          'type': 'viewed'
        }
      })
      if (res.status == 200) {
        // 未浏览则设置浏览状态为已浏览
        if (res.data == false) {
          let datas = this.$qs.stringify(
            {
              'uid': uid,
              'aid': aid,
              'type': "viewed"
            }
          )
          const { data: res1 } = await this.$axios.post('/addart', datas)
          if (res1.status == 200) {
            this.isviewed = true
          }
        }else{
          this.isviewed=res.data
        }
      }
      // 重新获取文章数据
      this.getArticle(uid, aid)
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

/** 动画进行时的class **/
.zoom-enter-active,
.zoom-leave-active {
  transition: all 0.5s cubic-bezier(0.42, 0, 0.34, 1.55);
}

/** 设置进场开始的状态和离场结束的状态，都是缩放到0 **/
.zoom-enter,
.zoom-leave-to {
  transform: scale(0);
}

/** 设置进场结束的状态和离场开始的状态, 都是缩放到1 **/
.zoom-enter-to,
.zoom-leave {
  transform: scale(1);
}
.comment >>> .el-card__header {
  height: 100px;
}
.comment-top {
  float: left;
  width: 100%;
  height: 100px;
}
.comment-num {
  margin-top: 30px;
  margin-left: 5px;
}

.thumb-content {
  position: relative;
  width: 100px;
  float: right;
}
.thumb-content img {
  width: 30px;
  height: 30px;
  margin-bottom: 15px;
}
.comment-btn {
  float: right;
  margin-right: 70px;
}
.isviewed {
  color: #e74c3c;
}
</style>