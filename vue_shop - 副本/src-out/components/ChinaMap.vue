<template>
  <div>
    <div ref="mapbox" style="width: 570px; height: 270px; margin: 0 auto"></div>
  </div>
</template>

<script>
import echarts from 'echarts'
import 'echarts/map/js/china.js'
import jsonp from 'jsonp'
const option = {
  title: {
    text: '全国疫情地图',
    link: 'https://blog.csdn.net/image_fzx',
    subtext: '防疫工作,人人有责',
    sublink: 'https://blog.csdn.net/image_fzx',
  },
  // ----------   series：地图数据可视化，添加data数据    ---------------------
  series: [
    {
      name: '确诊人数',
      type: 'map', // 告诉echarts 要去渲染的是一个地图
      map: 'china', // 告诉echarts  要去渲染中国地图
      label: {
        // 控制对应地区的汉字
        show: true,
        color: '#333', // 控制地区名的字体颜色---黑色，省名字
        fontSize: 6,
      },
      itemStyle: {
        // 地图板块的颜色和边框---灰色，各个省界线
        areaColor: '#eee',
        // borderColor:'blue'
      },
      roam: true,
      zoom: 1.2, // 控制地图的放大和缩小
      emphasis: {
        // 控制鼠标滑过之后的背景色和字体颜色--白色
        label: {
          color: '#fff',
          fontSize: 12,
        },
        itemStyle: {
          areaColor: '#83b5e7', //  滑动到哪个地区就显示蓝色
        },
      },
      data: [], // 用来展示后台给的数据的 {name:xx,value:xxx}
    },
  ],

  //-----------    visualMap：视觉映射，每个颜色代表什么含义   -----------------------------
  visualMap: [
    {
      type: 'piecewise',
      show: true,
      // splitNumber:4
      pieces: [
        // 分段
        { min: 10000 },
        { min: 1000, max: 9999 },
        { min: 100, max: 999 },
        { min: 10, max: 99 },
        { min: 1, max: 9 },
      ],
      // align:'right',// 默认left
      // orient:'horizontal' 默认竖直
      // left right 这些属性控制 分段坐在的位置
      // showLabel:false
      // textStyle:{}
      inRange: {
        symbol: 'rect',
        color: ['#fce4bc', '#f44444'], //   浅红~~深红色
      },
      itemWidth: 20,
      itemHeight: 10,
    },
  ],

  //-------------------------------------------------------------------
  tooltip: {
    trigger: 'item',
  },
  toolbox: {
    show: true,
    orient: 'vertical',
    left: 'right',
    top: 'center',
    feature: {
      // dataView: {readOnly: false},
      // restore: {},
      // saveAsImage: {}
    },
  },
}

export default {
  name: 'Chinamap',

  data() {
    return {}
  },

  mounted() {
    this.getData() // 为什么不再created
    this.mychart = echarts.init(this.$refs.mapbox)
    this.mychart.setOption(option)
  },

  methods: {
    getData() {
      jsonp(
        'https://interface.sina.cn/news/wap/fymap2020_data.d.json?_=1580892522427',
        {},
        (err, data) => {
          if (!err) {
            // 代表请求数据成功
            console.log(data)
            let list = data.data.list.map((item) => ({
              name: item.name,
              value: item.value,
            }))
            console.log(list)
            option.series[0].data = list
            this.mychart.setOption(option)
            // 这行代码能执行的前提是 DOM已经渲染完成，只有DOM渲染完成才能够执行 echarts初始化
          }
        }
      )
    },
  },
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
