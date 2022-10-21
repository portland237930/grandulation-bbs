<template>
  <div id="home">
    <Carousle :imglist="imglist" />
  </div>
</template>

<script>
// @ is an alias to /src
// Import Swiper Vue.js components
// import { Swiper, SwiperSlide } from 'swiper/vue';
// Import Swiper styles
// import 'swiper/css';
import Carousle from "@/components/Carousle/Carousle.vue"
export default {
  name: 'HomeView',
  components: {

    Carousle
  },
  data () {
    return {
      uid: 0,
      imglist: [
        require("../assets/hand.jpg"),
        require("../assets/HomeBackground.jpg"),
      ],
    }
  },
  mounted () {

  },
}
</script>
<style scoped>
#home {
  width: 80%;
  margin: auto;
}
.carousle {
  width: 100%;
  height: 500px;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 18px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}
.el-carousel__container {
  height: 400px;
}
.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
