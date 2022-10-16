<template>
	<div class="content">
	<el-card shadow="hover" class=" box-menu">
		<el-menu
      default-active="1"
      class="menu"
			@select="handleSelect"
      >
			  <el-menu-item index="1">
        <i class="el-icon-menu"></i>
        <span slot="title">个人设置</span>
      </el-menu-item>
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">我的帖子</span>
      </el-menu-item>
    </el-menu>
	</el-card>
	<router-view class="box-personal"></router-view>
	</div>
</template>

<script>
export default {
	name: 'Account',

	data() {
		return {
			
		};
	},

	mounted() {

	},
	created() {

	},
	methods: {
		// 根据导航更改子路由
		  handleSelect(key) {
				// console.log(key);
				switch (key) {
					case '1':
						this.$router.push('/account/personal')
						break;
					case '2':
						this.$router.push('/account/ownerarticle')
						break;
					default:
						break;
				}
				
      },
	},
};
</script>

<style scoped>
.content{
	position:relative;
	width:100%;
	height:100%;
}
.box-menu{
	position:absolute;
	height:300px;
	padding:0px;
	top:50px;
	border:1px solid #d5ebe1;
	left:200px;
}
.el-card__body{
	padding:0px;
}
.box-personal{
	position:absolute;
	left:400px;
	top:50px;
	width:60%;
	}

.menu{
	width:100%;
	border:none;
}
</style>