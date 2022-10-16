<template>
	<div>
		<el-card class="per-container">
			<div class="per-content">
				<el-avatar icon="el-icon-user-solid"></el-avatar>
				<span class="username">{{this.editForm.nick_name?this.editForm.nick_name:'请先登录'}}</span>
				<span class="levelicon el-icon-user-solid">{{this.editForm.permission==1?'会员':'普通用户'}}</span>
			</div>
		</el-card>
		<el-card class="per-message">
				<h3>基本信息</h3>
				<el-form 
						ref="editForm" 
						:model="editForm" 
						label-width="80px"
						style="border-top:1px solid #d5ebe1;">
						<el-form-item label="用户信息" prop="name">
							<span class="showmsg" v-if="!editable">{{editForm.name}}</span>
							<el-input v-else v-model="editForm.name"></el-input>
						</el-form-item>
						<el-form-item label="昵称" prop="nick_name">
							<span class="showmsg" v-if="!editable">{{editForm.nick_name}}</span>
							<el-input v-else v-model="editForm.nick_name"></el-input>
						</el-form-item>
						<el-form-item label="邮箱" prop="email">
							<span class="showmsg" v-if="!editable">{{editForm.email}}</span>
							<el-input v-else v-model="editForm.email"></el-input>
						</el-form-item>
						<el-form-item label="电话号码" prop="phone">
							<span class="showmsg" v-if="!editable">{{editForm.phone}}</span>
							<el-input v-else v-model="editForm.phone"></el-input>
						</el-form-item>
						<el-form-item label="个人简介" prop="personal_info">
							<span class="showmsg" v-if="!editable">{{editForm.personal_info}}</span>
							<el-input 
							type="textarea"
						  :rows="2" 
							v-else v-model="editForm.personal_info"></el-input>
						</el-form-item>
						<el-button type="primary" size="mini" @click="editable=true">编辑信息</el-button>
						<el-button v-show="editable" type="primary" size="mini" @click="editUserInfo">完成</el-button>
				</el-form>
			</el-row>
		</el-card>
	</div>
</template>

<script>
export default {
	name:"Personal",
	props: {

	},
	components: {

	},
	data() {
		return {
			editForm:{
				
			},
			editable:false,
			uid:0
		};
	},
	computed: {
		
	},
	watch: {

	},
	created() {

	},
	mounted() {
		// console.log(uid);
		this.getUser()
	},
	methods: {
		// 获取用户信息
		async getUser(){
			// 获取全局作用域
			var that=this
			this.uid=localStorage.getItem("uid")
			console.log(this.uid);
			let {data:res}=await this.$axios.get(
					'/user/user',
					{params:{'id':that.uid}}
				)
				this.editForm=res.data
		},
		// 修改用户信息
		async editUserInfo(){
			const res=await this.$axios.put(
				"/user/user",
				this.$qs.stringify(this.editForm)
			)
			console.log(res);
			if(res.status==200){
				this.$message.success(res.data.msg)
				this.editable=false
			}else{
				this.$message.error("修改失败")
			}
		}
	},
};
</script>

<style scoped>
.per-container{
	padding:10px;
	margin-bottom:20px;
}
.per-content{
	display:flex;
	padding:10px;
}
.username{
	margin-left:20px;
	display:inline-block;
	font-size:32px;
}
.showmsg{
	font-size:15px;
	margin-left:10px;
}
.levelicon{
	font-size:12px;
	margin:20px 10px;
}
</style>
