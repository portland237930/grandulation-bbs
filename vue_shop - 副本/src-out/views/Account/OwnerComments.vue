<template>
  <div>
    <el-card>
      <el-card class="box-card" v-for="c in commentList" :key="c.comment.id">
        <template v-slot:header>
          <div class="clearfix">
            <span>{{ c.publisher }}</span>
            <el-button style="float: right; padding: 3px 0" type="text"
              >编辑</el-button
            >
            <el-button
              style="float: right; padding: 3px 0; margin-right: 10px"
              type="text"
              >查看</el-button
            >
          </div>
        </template>
        <div class="text item">
          <div class="content-area">
            评论内容:
            {{ c.comment.content }}
          </div>
          <div class="time-area">
            <span>评论时间:{{ c.comment.create_time }}</span>
          </div>
        </div>
      </el-card>
    </el-card>
  </div>
</template>

<script>
import { getUid } from '../../utils/Token'
export default {
  name: 'OwnerComments',

  data() {
    return {
      commentList: [],
    }
  },

  mounted() {
    this.getAllCommentList()
  },

  methods: {
    async getAllCommentList() {
      let uid = getUid()
      let { data: res } = await this.$axios.get('/GetAllComments', {
        params: {
          uid: uid,
        },
      })
      if (res.status != 200) this.$message.error(res.msg)
      console.log(res)
      this.commentList = res.data
    },
  },
}
</script>

<style scoped>
.item {
  margin-bottom: 18px;
  width: 100%;
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: '';
}
.clearfix:after {
  clear: both;
}
.box-card {
  margin-bottom: 20px;
}
.content-area {
  width: 50%;
  font-size: 12px;
  font-weight: bold;
  height: 20px;
  overflow: hidden;
}
.time-area {
  width: 50%;
  color: #b1d5c8;
  font-size: 13px;
}
</style>
