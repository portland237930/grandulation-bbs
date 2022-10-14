<template>
<div class="container">
        <div class="login-wrapper">
            <div class="header" style="line-height:100px;">注册</div>
            <div class="form-wrapper">
                <input type="text" v-model="user.username" placeholder="用户名" class="input-item">
                <input type="password" v-model="user.password" placeholder="密码" class="input-item">
				<input type="text" v-model="user.real_pwd" placeholder="重复一次密码" class="input-item">
                <input type="password" v-model="user.nick_name" placeholder="昵称" class="input-item">
                <input type="text" v-model="user.email" placeholder="电子邮箱" class="input-item">
                <input type="password" v-model="user.phone" placeholder="电话号码" class="input-item">
                <div class="btn">Login</div>
            </div>
            <div class="msg">
                Don't have account?
                <a href="#">Sign up</a>
            </div>
        </div>
    </div>
</template>

<script>
// 
import "../assets/css/user.css"
export default {
	name: 'UserRegister',

	data() {
		return {
			user:{
				username:'',
				pwd:"",
				real_pwd:"",
				nick_name:"",
				email:"",
				phone:"",
			}
		};
	},

	mounted() {
		
	},

	methods: {
		
	},
};
</script>

<style scoped>

</style>