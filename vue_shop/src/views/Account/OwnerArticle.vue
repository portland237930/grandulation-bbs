<template>
  <div>
    <el-card>
      <div class="search">
        <span>搜索</span>
        <el-input v-model="searchContent"
                  @change="ArticleChange"
                  suffix-icon="el-icon-search"
                  placeholder="搜索关键字"></el-input>
        <!-- <el-radio v-model="order"
                  @change="OrderArticle"
                  class="orderText"
                  label="1">按照创建时间排序</el-radio>
        <el-radio text-color="#fc6d4f"
                  @change="OrderArticle"
                  v-model="order"
                  class="orderText"
                  label="2">按照访问量排序</el-radio> -->
      </div>
      <div class="article-content">
        <el-card class="article"
                 v-for="(a,index) in viewlist"
                 :key="index">
          <h3>{{a.title}}</h3>
          <span class="ctime">创建时间:{{a.create_time}}</span>
          <p class="utime">最近修改时间:{{a.update_time}}</p>
          <p class="vts">阅读:{{a.viewed}} 点赞:{{a.thumb}}</p>
          <el-button class="el-icon-edit"
                     plain
                     size="mini"
                     type="primary"
                     style="margin:0px 5px 0px 100px;"
                     @click="editArticle(a)"></el-button>
          <el-button type="info"
                     plain
                     class="el-icon-view"
                     size="mini"
                     @click="viewArticle(a)"></el-button>
          <el-dropdown trigger="click"
                       style="margin-left:20px;">
            <span class="el-dropdown-link">
              ...<i class="el-icon-caret-bottom el-icon--right"></i>
            </span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item class="clearfix">
                评论
                <el-badge class="mark"
                          :value="12" />
              </el-dropdown-item>
              <el-dropdown-item class="clearfix">
                回复
                <el-badge class="mark"
                          :value="3" />
              </el-dropdown-item>
              <el-dropdown-item @click.native="deleteArticle(a)"
                                class="clearfix">
                删除

              </el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </el-card>
      </div>
      <el-pagination small
                     :pageNo="pnum"
                     :page-size="4"
                     @current-change="pageChange"
                     layout="prev, pager, next"
                     :total="total"
                     class="pagination">
      </el-pagination>
    </el-card>
  </div>
</template>

<script>
import { getUid } from "@/utils/Token"
import { sortBy } from "@/utils/util"
export default {
  props: {

  },
  components: {

  },
  data () {
    return {
      searchContent: '', // 搜索栏
      articleList: [], // 文章总列表
      viewlist: [],
      userlist: {}, // 用户信息
      rolelist: {},// 角色信息
      // 分页参数
      pnum: 1,
      psize: 5,
      cpage: 1,
      total: 10,
      order: "1",
    };
  },
  computed: {

  },
  watch: {

  },
  created () {

  },
  mounted () {
    this.getArticleList()
  },
  methods: {
    // 获取文章列表
    async getArticleList () {
      var uid = getUid()
      var type = "list"
      let { pnum, psize } = this
      let { data: res } = await this.$axios.get(
        "/article",
        {
          params: {
            'uid': uid,
            'type': type,
          }
        }
      )
      // let { data: res2 } = await this.$axios.get(
      //   '/user/user',
      //   {
      //     params: {
      //       'id': uid
      //     }
      //   }
      // )
      console.log('user', res);
      // 请求成功
      if (res.status==200) {
        // 收集参数
        this.articleList = res.data
        this.userlist = res.data[0].user
        this.rolelist = res.data[0].user.role
        // 分页处理
        this.total = res.data.length - 1
        let cnum = (this.pnum - 1) * this.viewlist.length
        this.viewlist = res.data.slice(cnum, psize + cnum)
      }
      console.log(this.total);
    },
    // 编辑文章功能
    editArticle (data) {
      console.log(data);
      // 跳转至编辑文章页并传递参数
      this.$router.push({
        path: "/editarticle",
        query: {
          'article': data
        }
      })
    },
    // 浏览文章功能
    viewArticle (data) {
      // 封装参数
      let { rolelist, userlist } = this
      var datas = {
        'article': data,
        'role': rolelist,
        'user': userlist
      }
      this.$router.push({
        path: "/viewarticle",
        query: {
          'datas': this.$qs.stringify(datas)
        }
      })
    },
    // 改变页码功能
    pageChange (data, aa) {
      // 改变页码
      // console.log(data);
      this.pnum = data
      console.log(this.pnum);
      let cnum = (this.pnum - 1) * this.viewlist.length
      this.viewlist = this.articleList.slice(cnum, cnum + this.psize)
    },
    // 搜索功能
    ArticleChange () {
      // 存储实例指向
      var that = this
      if (that.searchContent) {
        // 模糊查询
        that.viewlist = that.articleList.filter(function (a) {
          // console.log(a);
          return Object.keys(a).some(function (key) {
            // console.log(key);
            if (key == 'title')
              return String(a[key]).toLowerCase().indexOf(that.searchContent) > -1
          })
        })
        that.viewlist = that.viewlist.slice((that.pnum - 1) * that.viewlist.length, that.psize)
        that.total = that.viewlist.length

      } else {
        // 返回首页
        that.pnum = 1
        that.total = that.articleList.length
        that.viewlist = that.articleList.slice(that.pnum, that.psize)
      }
    },
    OrderArticle () {
      var that = this
      that.viewlist = that.articleList.sort((a, b) => {
        console.log('a', a.create_time);
        console.log('b', b.create_time);
        console.log(a.create_time < b.create_time);
        return a.create_time > b.create_time
      })
      that.viewlist = that.viewlist.slice((that.pnum - 1) * that.viewlist.length, that.psize)
      that.total = that.viewlist.length
    },
    // 删除文章
    async deleteArticle (datas) {
      console.log(datas);
      var uid = getUid()
      let { data: res } = await this.$axios.delete(
        '/article',
        {
          params: {
            'uid': uid,
            'aid': datas.id
          }
        }
      )
      console.log(res);
      if (res.status != 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.getArticleList()
    }
  },
};
</script>

<style scoped>
.search {
  display: flex;
  width: 100%;
}
.search span {
  width: 70px;
  text-align: center;
  line-height: 40px;
}
.search >>> .el-input {
  width: 200px;
}
.article-content {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
}
.article {
  margin: 10px 10px;
  width: 100%;
  animation-name: fadeIn; /*fadeInLeft为要使用的动画效果名，在这里不需要加animate前缀*/
  animation-duration: 2s; /*这里设定完成该动画的时间*/
}
.article h3 {
  width: 100%;
  display: inline-block;
  margin: 0px;
  font-size: 17px;
  color: #605d6f;
}
.utime {
  font-size: 13px;
  text-align: right;
  display: inline-block;
  margin: 0px;
  width: 50%;
  color: #9cb4d4;
}
.ctime {
  font-size: 13px;
  display: inline-block;
  width: 50%;
  color: #b4b0b4;
}
.vts {
  font-size: 12px;
  display: inline-block;
  width: 50%;
  color: #9fa8be;
}
.orderText {
  line-height: 40px;
  text-align: right;
}
</style>
