<template>
  <div class="search-container">
    <div class="content"></div>
  </div>
</template>

<script>
export default {
  name: 'Search',

  data () {
    return {
      articlelist: {},
      searchContent: ""

    };
  },

  mounted () {
    // console.log('back',this.$qs.parse(this.$route.query.articlelist));
    this.articlelist = this.$qs.parse(this.$route.query.articlelist)
  },

  methods: {
  },
};
</script>

<style  scoped>
.search-container {
  position: relative;
  /* width: 100%; */
}
.search-content {
  width: 100%;
  background-color: #ececec;
  position: fixed;
  /* top: 0px;
  left: 0px; */
  height: 60px;
  line-height: 60px;
}
.search-input {
  width: 70%;
  height: 50px;
  padding: 0 auto;
}
</style>