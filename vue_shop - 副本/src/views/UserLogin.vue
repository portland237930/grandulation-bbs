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
      <el-button type="primary"
                 @click="test">test</el-button>
      <wxlogin :appid="appid"
               :theme='black'
               scope="snsapi_login"
               :href="bast64css"
               rel="external nofollow"
               :redirect_uri="encodeURIComponent(redirect_uri)"></wxlogin>
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
      bast64css: 'data:text/css;base64,LmltcG93ZXJCb3ggLnFyY29kZSB7d2lkdGg6IDIwMHB4O2hlaWdodDoyMDBweH0NCi5pbXBvd2VyQm94IC5pbmZvIHt3aWR0aDogMjAwcHh9DQouc3RhdHVzX2ljb24ge2Rpc3BsYXk6IG5vbmV9DQouaW1wb3dlckJveCAuc3RhdHVzIHt0ZXh0LWFsaWduOiBjZW50ZXI7fQ0KLmltcG93ZXJCb3ggLnRpdGxlIHtkaXNwbGF5OiBub25lfQ0KaWZyYW1lIHtoZWlnaHQ6IDMyMnB4O30NCg==',
      appid: "wx7287a60bb700fd21",
      redirect_uri: "/user/wx_login"
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
    },
    async test () {
      const res = await this.$axios.get("/user/wx_login", {
        params: {
          'code': "123"
        }
      })
      console.log(res)
    }
  },
};
</script>

<style scoped>
.container {
  animation: zoomIn 0.5s ease;
}
</style>