<template>
  <div class="contains">
    <Editor type="edit" />
    <Menu type="edit" />
  </div>
</template>

<script>
import Menu from '../../components/Menu.vue'
import Editor from '../../components/Editor.vue'
export default {
  name: 'EditArticle',
  props: {},
  components: {
    Menu,
    Editor,
  },
  data() {
    return {}
  },
  computed: {},
  watch: {},
  created() {},
  mounted() {},
  methods: {},
}
</script>

<style lang="less" scoped>
.contains {
  display: flex;
  justify-content: center;
  position: relative;
}
</style>
