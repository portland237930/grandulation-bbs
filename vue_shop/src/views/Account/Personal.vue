<template>
  <div>
    <el-card class="per-container">
      <div class="per-content">
        <el-upload class="avatar-uploader"
                   action="/user/upload_img"
                   :on-success="handleUpload"
                   :show-file-list="false">
          <el-avatar v-if="!editForm.avatar_url"
                     icon="el-icon-user-solid"></el-avatar>
          <img v-else
               class="avatar-img"
               :src="editForm.avatar_url"></img>
        </el-upload>
        <span class="username">{{editForm.nick_name?editForm.nick_name:'请先登录'}}</span>
        <span class="levelicon el-icon-user-solid">{{role.name}}</span>
      </div>
    </el-card>
    <el-card class="per-message">
      <h3>基本信息</h3>
      <el-form ref="editForm"
               :model="editForm"
               label-width="80px"
               style="border-top:1px solid #d5ebe1;">
        <el-form-item label="用户信息"
                      prop="name">
          <span class="showmsg"
                v-if="!editable">{{editForm.name}}</span>
          <el-input v-else
                    v-model="editForm.name"></el-input>
        </el-form-item>
        <el-form-item label="昵称"
                      prop="nick_name">
          <span class="showmsg"
                v-if="!editable">{{editForm.nick_name}}</span>
          <el-input v-else
                    v-model="editForm.nick_name"></el-input>
        </el-form-item>
        <el-form-item label="邮箱"
                      prop="email">
          <span class="showmsg"
                v-if="!editable">{{editForm.email}}</span>
          <el-input v-else
                    v-model="editForm.email"></el-input>
        </el-form-item>
        <el-form-item label="电话号码"
                      prop="phone">
          <span class="showmsg"
                v-if="!editable">{{editForm.phone}}</span>
          <el-input v-else
                    v-model="editForm.phone"></el-input>
        </el-form-item>
        <el-form-item label="个人简介"
                      prop="personal_info">
          <span class="showmsg"
                v-if="!editable">{{editForm.personal_info}}</span>
          <el-input type="textarea"
                    :rows="2"
                    v-else
                    v-model="editForm.personal_info"></el-input>
        </el-form-item>
        <el-button v-show="!editable"
                   type="primary"
                   size="mini"
                   @click="editable=true">编辑信息</el-button>
        <el-button v-show="editable"
                   type="primary"
                   size="mini"
                   @click="editUserInfo">完成</el-button>
      </el-form>
      </el-row>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "Personal",
  props: {

  },
  components: {

  },
  data () {
    return {
      editForm: {

      },
      role: {},
      editable: false,
      uid: 0,
    };
  },
  computed: {

  },
  watch: {

  },
  created () {

  },
  mounted () {
    // console.log(uid);
    this.getUser()
  },
  methods: {
    // 获取用户信息
    async getUser () {
      // 获取全局作用域
      var that = this
      this.uid = localStorage.getItem("uid")
      console.log(this.uid);
      let { data: res } = await this.$axios.get(
        '/user/user',
        { params: { 'id': that.uid } }
      )
      console.log(res);
      this.editForm = res.data
      this.role = res.data.role
    },
    // 修改用户信息
    async editUserInfo () {
      const res = await this.$axios.put(
        "/user/user",
        this.$qs.stringify(this.editForm)
      )
      console.log(res);
      if (res.status == 200) {
        this.$message.success(res.data.msg)
        this.editable = false
      } else {
        this.$message.error("修改失败")
      }
    },
    // 文件上传成功功能
    async handleUpload (res) {
      console.log('aa', res);
      // 上传头像
      await this.$axios.put(
        '/user/avatar_url',
        this.$qs.stringify({
          'id': this.uid,
          'url': res.data.url
        }
        )

      )
      // 重新获取用户列表
      this.getUser()
    }
  },
};
</script>

<style scoped>
.per-container {
  padding: 10px;
  margin-bottom: 20px;
}
.per-content {
  display: flex;
  padding: 10px;
}
.username {
  margin-left: 20px;
  display: inline-block;
  font-size: 32px;
}
.showmsg {
  font-size: 15px;
  margin-left: 10px;
}
.levelicon {
  font-size: 12px;
  margin: 20px 10px;
}
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
.avatar-img {
  width: 70px;
  height: 70px;
  border-radius: 50px;
}
</style>
