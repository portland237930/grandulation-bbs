<template>
  <div class="contains">
    <!-- <el-card class="edit_container">
        <div class="title-container">
          <el-input placeholder="请输入标题"
                    class="title"
                    v-model="title"></el-input>
        </div>
        <quill-editor v-model="content"
                      ref="myQuillEditor"
                      :options="editorOption"
                      @blur="onEditorBlur($event)"
                      @focus="onEditorFocus($event)"
                      @change="onEditorChange($event)">
        </quill-editor>
        <h1>上传封面</h1>
        <el-upload :on-exceed="exceedUpload"
                   :limit=3
                   action="/user/upload_img"
                   list-type="picture-card"
                   :on-success="handleUploadSuccess"
                   :on-preview="handlePictureCardPreview"
                   :on-remove="handleRemove">
          <i class="el-icon-plus"></i>
        </el-upload>
        <el-dialog :visible.sync="dialogVisible">
          <img width="100%"
               :src="dialogImageUrl"
               alt="">
        </el-dialog>
      </el-card> -->
    <Editor type="publish" />
    <!-- <i class="el-icon-s-operation menu-item"
         @click="drawer = true"></i>
      <el-drawer title="我是标题"
                 direction="btt"
                 class="drawer"
                 size="15%"
                 :visible.sync="drawer"
                 :with-header="false">
        <span class="el-icon-menu"></span>
        <el-button class="pub-btn"
                   type="primary"
                   @click="pubArticle">发布博客</el-button>
        <el-button class="pub-btn"
                   type="primary"
                   @click="BackHome">取消发布</el-button>
      </el-drawer> -->
    <!-- :content="content"
            :imgs="imgs"
            :title="title"			 -->
    <Menu type="publish" />
  </div>
</template>

<script>
import Menu from '../../components/Menu.vue'
import Editor from '../../components/Editor.vue'
import { getUid } from '@/utils/Token'
export default {
  name: 'PublishArt',

  data() {
    return {
      content: ``, //文本内容
      str: '',
      title: '', // 标题
      dialogImageUrl: '', // 上传弹窗路径
      drawer: false,
      dialogVisible: false, //上传弹窗是否显示
      checklist: [], // 选中封面列表
      imgs: '',
    }
  },

  mounted() {
    let content = '' // 请求后台返回的内容字符串
    this.str = this.escapeStringHTML(this.content)
  },
  computed: {},
  methods: {
    onEditorReady(editor) {
      // 准备编辑器
    },
    // 失去焦点事件
    onEditorBlur() {},
    onEditorFocus() {}, // 获得焦点事件
    // 内容改变事件
    onEditorChange() {
      this.str = this.escapeStringHTML(this.content)
    },
    // 转码
    escapeStringHTML(str) {
      str = str.replace(/&lt;/g, '<')
      str = str.replace(/&gt;/g, '>')
      return str
    },
    handleRemove(file, fileList) {
      console.log(file, fileList)
    },
    handlePictureCardPreview(file) {
      console.log(file)
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    handleUploadSuccess(file, fileList) {
      console.log('success', file, fileList)
      this.dialogVisible = false
      this.imgs += file.data.url + ','
    },
    // 超出上传文件数量回调
    exceedUpload() {
      this.$message.error('封面数量以达上限')
      this.dialogVisible = false
    },
  },
  // 引入组件
  components: {
    Menu,
    Editor,
  },
}
</script>

<style scoped>
.contains {
  display: flex;
  justify-content: center;
  position: relative;
}
</style>
