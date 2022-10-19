<template>
  <div class="container">
    <div class="login-wrapper">
      <div class="header">Login</div>
      <div class="form-wrapper">
        <el-form :rule="LoginRule"
                 ref="Loginform"
                 :model="userinfo"
                 label-width="80px">
          <el-form-item label="账号"
                        prop="name">
            <el-input placeholder="请输入用户名"
                      v-model="userinfo.name"
                      type="primary"></el-input>
          </el-form-item>
          <el-form-item label="密码"
                        prop="pwd">
            <el-input type="primary"
                      show-password
                      placeholder="请输入密码"
                      v-model="userinfo.pwd"></el-input>
          </el-form-item>
        </el-form>
        <el-button @click="UserLogin"
                   type="primary"
                   :loading="isloading"
                   class="btn">Login</el-button>
      </div>
      <div class="msg">
        No account yet
        <router-link to="/userregister">Register</router-link>
      </div>
    </div>
  </div>
</template>

<script>
// 引用用户样式
import "../assets/css/user.css"
// 引入token
import { setToken, setUid } from "../utils/Token"
export default {
  name: 'UserLogin',

  data () {
    return {
      userinfo: {
        name: "",
        pwd: ""
      },
      LoginRule: {
        name: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { min: 2, max: 10, message: "长度在 2~10 字符之间", trigger: "blur" },
        ],
        pwd: [
          { required: true, message: "请输入密码", trigger: "blur" },
          { min: 2, max: 15, message: "长度在 2~15 字符之间", trigger: "blur" },
        ],
      },
      isloading: false
    };
  },

  mounted () {
  },

  methods: {
    UserLogin () {
      this.$refs.Loginform.validate(async valid => {
        if (!valid) return
        this.isloading = true
        let res = await this.$axios.post(
          '/user/login',
          this.$qs.stringify(this.userinfo)
        )
        console.log(res);
        if (res.data.status != 200) return this.$message.error(res.data.msg)
        // 全局存储
        console.log('uid', res.data.data.uid);
        // 设置Token
        setToken(res.data.data.token)
        setUid(res.data.data.uid)
        this.isloading = false
        this.$message.success(res.data.msg)
        this.$router.push("/home")
      })
    }
  },
};
</script>

<style scoped>
.container {
  animation: zoomIn 0.5s ease; /* referring directly to the animation's @keyframe declaration */
}
</style>