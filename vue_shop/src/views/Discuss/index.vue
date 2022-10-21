<template>
  <div>
    <section id="main">
      <!--主体的左边-->
      <div class="main-left">
        <!--焦点图-->
        <el-card class="main-left-top">
          <ChinaMap />

        </el-card>
        <!--文章列表-->
        <div class="main-left-cell infinite-list-wrapper">
          <!-- <div class="cell" v-for="a in articleList" :key="a.id">
            <dl>
              <dt>
              	  <img v-if="a.cover.split(',')[0]" :src="a.cover.split(',')[0]"
                     alt="">
									<img v-else src="@/assets/hand.jpg">
							</dt>
              <dd>
                <h3>{{a.title}}</h3>
                <p v-html="a.content" class="content"></p>
                <a href="#">
                  <span>远方不会远</span>
                </a>
                <a href="#">
                  <span class="el-icon-view">999</span>
                </a>
                <a href="#">
                  <img src="images/like_icon.png"
                       alt="">
                  <span>8989</span>
                </a>
              </dd>
            </dl>
          
          
          </div> -->
          <el-card class="cell list"
                   v-infinite-scroll="load"
                   infinite-scroll-disabled="disabled"
                   @click.native="ViewArticle(a)"
                   v-for="a in articleList"
                   :key="a.id">
            <div class="cell-left">
              <h3>{{a.title}}</h3>
              <div class="content"
                   v-html="a.content.replace(/<[^>]*>/g,'').slice(1,20)+'...'"></div>
              <!-- <p>{{a.user.name}}</p> -->
              <p class="el-icon-thumb"
                 style="margin-right:5px"> {{a.thumb}} </p>
              <p class="el-icon-view"> {{a.viewed}} </p>
            </div>
            <div class="cell-right">
              <img v-if="a.cover.split(',')[0]"
                   :src="a.cover.split(',')[0]">
              <img v-else
                   src="@/assets/hand.jpg">
            </div>
          </el-card>
          <div class="loading-container">
            <p class="el-icon-loading "
               v-if="loading"></p>
            <p v-if="noMore">没有更多了</p>
          </div>

        </div>
      </div>
      <!--主体的右边-->
      <div class="main-right">
        <!--第一部分-->
        <div class="main-right-top">
          <Carousle :imglist="imglist" />
        </div>

        <!--第三部分-->
        <div class="main-right-bottom">
          <!-- <div class="main-right-bottom-head">
            <!-- <el-autocomplete v-model="state"
                             :fetch-suggestions="querySearchAsync"
                             placeholder="请输入标题"
                             @select="handleSelect"></el-autocomplete>
            <el-button type="primary"
                       @click="GoSearch"
                       icon="el-icon-search"
                       circle></el-button> -->
          <!-- </div> -->
          <ul>
            <li>
              <div>
                <a href="#"
                   class="title">今日公告</a>
                <p>小程序发布于xxxx</p>
              </div>
              <a href="#"
                 class="focus">敬请期待</a>
            </li>
            <li>
              <div>
                <a href="#"
                   class="title">开发进程</a>
                <p>开发文档全公布</p>
              </div>
              <a href="#"
                 class="focus">敬请期待</a>
            </li>
            <li>
              <div>
                <a href="#"
                   class="title">关于我们</a>
                <p>站长的信息噢</p>
              </div>
              <a href="#"
                 class="focus">敬请期待</a>
            </li>
            <li>
              <div>
                <a href="#"
                   class="title">开发日志</a>
                <p>毕业设计记录</p>
              </div>
              <a href="#"
                 class="focus">敬请期待</a>
            </li>
            <li>
              <!-- <a class="author-icon"
                 href="#"><img src="@/assets/wechat.png"
                     alt=""></a> -->
              <div>
                <a href="#"
                   class="title">扫码下载蓝牙小程序</a>
                <p>蓝牙控制端小程序</p>
              </div>
              <a href="#"
                 class="focus">关注我们</a>
            </li>
          </ul>
          <a href="#"
             class="main-right-bottom-footer">
            查看全部
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// 引入组件
import Carousle from "@/components/Carousle/Carousle.vue"
import ChinaMap from "@/components/ChinaMap.vue"
export default {
  name: 'Discuss',

  data () {
    return {
      // 轮播图图片
      imglist: [
        require("@/assets/wechat.png"),
        require("@/assets/HomeBackground.jpg")
      ],
      articleList: [], // 显示的文章列表
      state: "",
      restaurants: {},
      loading: false, // 加载标志位
      pnum: 1,
      psize: 4,
      searchlist: [] // 搜索结果
    };
  },
  computed: {
    noMore () {
      return this.articleList.length >= this.restaurants.length - 2
    },
    disabled () {
      return this.loading || this.noMore
    }
  },
  mounted () {
    this.loadAll()

  },

  methods: {
    // 查看文章功能
    ViewArticle (article) {
      console.log(article)
      var datas = {
        'article': article,
        'role': article.user.role,
        'user': article.user
      }
      // 进入查看页
      this.$router.push({
        path: "/viewarticle",
        query: {
          'datas': this.$qs.stringify(datas)
        }
      })
    },
    // 获取所有文章接口
    async loadAll () {
      let { data: res } = await this.$axios.get(
        '/getAllArticle',
        {
          params: {
            'type': 'all'
          }
        }
      )
      console.log(res);
      if (res.status == 200)
        this.restaurants = res.data
      this.articleList = res.data.slice(this.pnum, this.psize)
    },
    // 异步搜索
    querySearchAsync (queryString, cb) {
      var that = this
      var restaurants = this.restaurants;
      var results = queryString ? restaurants.filter(this.createStateFilter(queryString)) : restaurants;
      var reslist = []
      // this.searchlist = results
      console.log(results);
      // 每隔一段时间进行搜索
      clearTimeout(this.timeout);
      this.timeout = setTimeout(() => {
        results.forEach(item => {
          that.searchlist.unshift(item)
          reslist.unshift({
            'value': item.title
          })
        })
        cb(reslist)
      }, 1000 * Math.random());
    },
    // 闭包查找相关信息
    createStateFilter (queryString) {
      return (state) => {
        return (state.title.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
      };
    },
    handleSelect (item) {
      console.log('select', item);
    },
    // 加载数据
    load () {
      this.loading = true
      setTimeout(() => {
        this.psize += 2
        this.articleList = this.restaurants.slice(this.pnum, this.psize)
        this.loading = false
      }, 500)
    },
    // 去搜索页
    GoSearch () {
      console.log("front", this.searchlist);
      this.$router.push(
        {
          path: "/search",
          query: {
            'articlelist': this.$qs.stringify(this.searchlist)
          }        }
      )
    },
  },
  components: {
    Carousle,
    ChinaMap
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  border: none;
}

ul,
ol {
  list-style: none;
}

a {
  text-decoration: none;
  color: #000;
}

img {
  vertical-align: middle;
}

input {
  outline: none;
}

/************************通用样式-end***********************/

/************************内容样式-start***********************/
#main {
  width: 1000px;
  /* height: 2000px; */
  overflow: auto;
  /* overflow-y: hidden; */
  margin: 30px auto;
  /* height: 100vh; */
  /* position: absolute; */
  /* background-color:#fcfcfc; */
}
#main::-webkit-scrollbar {
  display: none;
}
#main .main-left {
  width: 688px;
  height: 100vh;
  float: left;
}

#main .main-left .main-left-top {
  width: 550px;
  height: 270px;
  margin: 10px 0px;
  /* padding: 10px; */
}
#main .main-left .main-left-top >>> .el-card__body {
  padding: 0px;
  line-height: 270px;
}
#main .main-left .main-left-top img {
  width: 688px;
  height: 270px;
  border-radius: 10px;
}

#main .main-left-center {
  width: 100%;
  height: 110px;
  margin-top: 20px;
}

#main .main-left-center a {
  display: inline-block;
  height: 32px;
  border: 1px solid #dcdcdc;
  background-color: #e7e7e7;
  margin: 0 18px 18px 0;
  padding-right: 15px;
  border-radius: 5px;
  font-size: 14px;
  vertical-align: top;
}

#main .main-left-center a:last-child {
  background-color: transparent;
  border: none;
  line-height: 32px;
  font-size: 16px;
  color: #787878;
}

#main .main-left-center a img {
  width: 30px;
  height: 30px;
  vertical-align: middle;
  margin-right: 15px;
  border-radius: 5px 0 0 5px;
}

/*文章列表*/
#main .main-left-cell {
  /* overflow:auto; */
  /* margin: 10px 0px; */
  width: 80%;

  /* overflow: auto; */
}

#main .main-left-cell .cell {
  height: 120px;
  padding: 18px;
  margin: 8px 0px;
}
#main .main-left-cell .cell .cell-left {
  width: 80%;
  height: 100%;
  float: left;
}
.content {
  width: 100%;
  height: 30px;
  font-size: 14px;
  font-weight: 400;
  color: #86909c;
  line-height: 30px;
}
.#main .main-left-cell .cell .cell-left p {
  font-size: 12px;
  color: #dbe8e4;
  display: inline-block;
  margin: 0px 4px;
}
#main .main-left-cell .cell .cell-right {
  width: 20%;
  height: 97.43px;
  float: right;
}

.cell >>> .el-card__body,
.el-main {
  width: 100%;
  height: 100%;
  padding: 0px;
}
#main .main-left-cell .cell img {
  width: 100%;
  height: 92%;
  border-radius: 5px;
}

#main .main-right {
  width: 300px;
  height: 800px;
  position: fixed;
  right: 300px;

  float: right;
}

#main .main-right .main-right-top {
  height: 290px;
}

#main .main-right .main-right-top img {
  width: 300px;
  height: 50px;
  margin-bottom: 5px;
}

#main .main-right .main-right-center {
  height: 90px;
  border: 1px solid #f0f0f0;
  border-radius: 5px;
  padding: 15px 25px;
}

#main .main-right .main-right-center dl dt {
  float: left;
  margin-right: 10px;
}

#main .main-right .main-right-center dl dd {
  float: left;
  margin-top: 8px;
}

#main .main-right .main-right-center dl dd p {
  font-size: 14px;
  margin-top: 3px;
}

#main .main-right .main-right-center dl dd p:last-child {
  color: #b4b4b4;
}

#main .main-right .main-right-center dl dt img {
  width: 60px;
  height: 60px;
}

#main .main-right .main-right-bottom {
  height: 300px;
}

#main .main-right .main-right-bottom .main-right-bottom-head {
  height: 45px;
  line-height: 45px;
  padding: 5px 10px;
  font-size: 14px;
  color: #b8b8b8;
  margin-bottom: 10px;
}

#main .main-right .main-right-bottom .main-right-bottom-head span:first-child {
  float: left;
  font-size: 14px;
}

#main .main-right .main-right-bottom .main-right-bottom-head span:last-child {
  float: right;
  font-size: 14px;
}

#main .main-right .main-right-bottom .main-right-bottom-head span:last-child a {
  color: #b8b8b8;
}

#main .main-right .main-right-bottom ul li {
  width: 300px;
  height: 50px;
  margin-bottom: 10px;
  position: relative;
}

#main .main-right .main-right-bottom ul li img {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: 1px solid #cccccc;
  margin-right: 10px;
}

#main .main-right .main-right-bottom ul li .author-icon {
  float: left;
}

#main .main-right .main-right-bottom ul li a.focus {
  position: absolute;
  right: 0;
  top: 0;
  color: #1c94fc;
  font-size: 12px;
}

#main .main-right .main-right-bottom ul li > div {
  float: left;
  height: 50px;
  line-height: 25px;
}

#main .main-right .main-right-bottom ul li > div > p {
  color: #b4b4b4;
}

#main .main-right .main-right-bottom-footer {
  display: inline-block;
  width: 300px;
  border: 1px solid #cccccc;
  padding: 7px 10px;
  text-align: center;
  border-radius: 5px;
  color: #b4b4b4;
  margin-top: 10px;
}
/* *Loading样式 */
.loading-container {
  width: 100%;
  text-align: center;
  height: 30px;
  margin: 10px 0px;
}
.loading-container p {
  /* margin: 10px auto; */
  color: #2f3542;
  /* display: inline-block; */
}
/************************内容样式-end***********************/
</style>