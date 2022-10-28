<template>
  <!-- 轮播图模块 -->
  <el-carousel :interval="5000"
               class="carousle"
               arrow="always">
    <el-carousel-item v-for="item in imglist"
                      :key="item">
      <img class="carousle-img"
           style="  width: 100%;
  height: 100%;"
           :src="item" />
    </el-carousel-item>
  </el-carousel>
</template>

<script>
import Swiper from "swiper"
export default {
  name: "Carousle",
  props: ["imglist"],
  // 监听数据改变时创建Swiper实例
}
</script>

<style>
.carousle .el-carousel__container {
  width: 100%;
  height: 270px;
}
</style>