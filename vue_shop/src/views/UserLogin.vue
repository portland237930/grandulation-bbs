<template>
  <div class="container">
    <div class="login-wrapper"
         style="height:588px">
      <kinesis-container>
        <kinesis-element type="translate"
                         :strength="20">
          <div class="header">Login</div>
        </kinesis-element>
      </kinesis-container>
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
      <!-- <wxlogin href='data:text/css;base64,LmltcG93ZXJCb3ggLnFyY29kZSB7CiAgICB3aWR0aDogMTUwcHg7Cn0KLmltcG93ZXJCb3ggLnRpdGxlIHsKICAgIHRleHQtYWxpZ246IGxlZnQ7CiAgICBmb250LXNpemU6IDE2cHg7CiAgICBmb250LXdlaWdodDogYm9sZDsKfQ=='
               id="wxcode"
               theme=''
               appid="wxd4ac0386fed8e63b"
               scope="snsapi_login"
               :redirect_uri="encodeURIComponent(redirect_uri)"></wxlogin> -->
      <!-- <wxlogin :appid="appid"
               :scope="scope"
               :redirect_uri="redirect_uri"></wxlogin> -->
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
import wxlogin from 'vue-wxlogin';
import { KinesisContainer, KinesisElement } from 'vue-kinesis'
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
      isloading: false,
      appid: "",
      scope: "",
      redirect_uri: "http://localhost:8080/home"
    };
  },
  components: {
    wxlogin,
    KinesisContainer,
    KinesisElement

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
        this.$router.push("/")
      })
    }
  },
};
</script>

<style scoped>
.container {
  animation: zoomIn 0.5s ease;
}
</style>