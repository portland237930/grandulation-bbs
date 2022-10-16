<template>
  <div id="app">
    <Header v-show="$route.meta.showHeader"/>
    <router-view/>
  </div>
</template>
<script>
import Header from './components/Header.vue'
export default {
  components:{
    Header
  }
}
</script>
<style>
</style>
