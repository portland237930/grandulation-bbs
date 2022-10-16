<template>
  <div class="container">
    <div class="login-wrapper">
      <div class="header" style="line-height: 100px">注册</div>
      <div class="form-wrapper">
        <el-form
          ref="RegForm"
          :model="userlist"
          label-width="80px"
          :rules="RegFormRules"
        >
          <el-form-item label="用户名" prop="name">
            <el-input
              v-model="userlist.name"
              placeholder="请输入用户名"
            ></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="pwd">
            <el-input
              v-model="userlist.pwd"
              placeholder="请输入密码"
            ></el-input>
          </el-form-item>
          <el-form-item label="重复密码" prop="real_pwd">
            <el-input
              v-model="userlist.real_pwd"
              placeholder="重复一次密码"
            ></el-input>
          </el-form-item>
          <el-form-item prop="nick_name" label="昵称">
            <el-input
              v-model="userlist.nick_name"
              placeholder="请输入昵称"
            ></el-input>
          </el-form-item>
          <el-form-item prop="email" label="电子邮箱">
            <el-input
              v-model="userlist.email"
              placeholder="请输入电子邮箱"
            ></el-input>
          </el-form-item>
          <el-form-item prop="phone" label="电话号码">
            <el-input
              v-model="userlist.phone"
              placeholder="请输入电话号码"
            ></el-input>
          </el-form-item>
        </el-form>
        <el-button type="primary" class="btn" @click="UserRegister"
          >注册</el-button
        >
      </div>
      <div class="msg">
        Do you have account?
        <router-link to="/UserLogin">SignUp</router-link>
      </div>
    </div>
  </div>
</template>

<script>
//
import "../assets/css/user.css";
import {reqUserRegister} from "../api"
export default {
  name: "UserRegister",

  data() {
    const validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.userlist.pwd) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
    const validatePhone = (rule, value, callback) => {
      // 定义一个正则来验证手机号是否是有效的
      const phoneReg = /^0?(13|14|15|18|17)[0-9]{9}$/;
      if (phoneReg.test(value)) {
        return callback();
      }
      return callback(new Error("请输入有效的手机号"));
    };
    const validateEmail = (rule, value, callback) => {
      // 定义一个正则来验证邮箱是否是有效的
      const emailReg = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
      if (emailReg.test(value)) {
        return callback();
      }
      return callback(new Error("请输入有效的手机号"));
    };
    return {
	//   存储用户信息
      userlist: {
        name: "",
        pwd: "",
        real_pwd: "",
        nick_name: "",
        email: "",
        phone: "",
	  },
	//   表单校验
      RegFormRules: {
        name: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { min: 2, max: 10, message: "长度在 2~10 字符之间", trigger: "blur" },
        ],
        nick_name: [
          { required: true, message: "请输入昵称", trigger: "blur" },
          { min: 2, max: 15, message: "长度在 2~15 字符之间", trigger: "blur" },
        ],
        pwd: [
          { required: true, message: "请输入密码", trigger: "blur" },
          { min: 2, max: 15, message: "长度在 2~15 字符之间", trigger: "blur" },
        ],
        real_pwd: [
          { required: true, message: "请重新输入密码", trigger: "blur" },
          { validator: validatePass2, trigger: "blur" },
        ],
        phone: [{ validator: validatePhone, trigger: "blur" }],
        email: [{ validator: validateEmail, trigger: "blur" }],
      },
    };
  },

  mounted() {},

  methods: {
	//   用户注册功能
	UserRegister() {
      // 发送请求之间，验证是数据是否规范
      this.$refs.RegForm.validate(async valid => {
        if (!valid) return
        // 发送请求
        console.log(         this.$qs.stringify(this.userlist)
);
        const { data: res } = await this.$axios.post(
          '/user/user',
          this.$qs.stringify(this.userlist)
        )
        console.log(res);
        
        // 验证结果
        if (res.status !== 200) return this.$msg.error(res.msg)
        this.$message.success(res.msg)
        // 重置增加用户表单
		    this.$refs.RegForm.resetFields()	
		    this.$router.push("/userlogin")
      })
    },
  },
};
</script>

<style scoped></style>
