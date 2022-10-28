<template>
  <el-card class="edit_container">
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
               :file-list="imglist"
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
  </el-card>
</template>

<script>
import { quillEditor } from "vue-quill-editor"; //调用编辑器
import 'quill/dist/quill.core.css';
import 'quill/dist/quill.snow.css';
import 'quill/dist/quill.bubble.css';
export default {
  name: 'Editor',
  props: [
    'type'
  ],
  components: {
    quillEditor,
  },
  watch: {
    // 兄弟组件传值
    title: {
      handler (newval, oldval) {
        this.$bus.$emit('title', newval)
      },
      immediate: true
    },
    content: {
      handler (newval, oldval) {
        this.$bus.$emit('content', newval)
      },
      immediate: true
    },
    imgs: {
      handler (newval, oldval) {
        this.$bus.$emit('imgs', newval)
      },
      immediate: true
    },
  },
  computed: {
    editor () {
      return this.$refs.myQuillEditor.quill;
    },
  },
  data () {
    return {
      dialogImageUrl: '',
      imglist: [],
      dialogVisible: false,
      str: "",
      title: "",
      imgs: "",
      aid: 0,
      content: "",
      // 富文本选项
      editorOption: {
        placeholder: "请在这里输入",
        modules: {
          toolbar: [
            ['bold', 'italic', 'underline', 'strike'],    //加粗，斜体，下划线，删除线
            ['blockquote', 'code-block'],     //引用，代码块
            [{ 'header': 1 }, { 'header': 2 }],        // 标题，键值对的形式；1、2表示字体大小
            [{ 'list': 'ordered' }, { 'list': 'bullet' }],     //列表
            [{ 'script': 'sub' }, { 'script': 'super' }],   // 上下标
            [{ 'indent': '-1' }, { 'indent': '+4' }],     // 缩进
            [{ 'direction': 'rtl' }],             // 文本方向
            [{ 'size': ['small', false, 'large', 'huge'] }], // 字体大小
            [{ 'header': [1, 2, 3, 4, 5, 6, false] }],     //几级标题
            [{ 'color': [] }, { 'background': ['#fff'] }],     // 字体颜色，字体背景颜色
            [{ 'font': [] }],     //字体
            [{ 'align': [] }],    //对齐方式
            ['clean'],    //清除字体样式
            ['image', 'video', 'link']    //上传图片、上传视频
          ]
        }
      }
    };
  },

  mounted () {
    if (this.type == 'edit') {
      let data = this.$route.query.article
      console.log('article', data);
      this.content = data.content
      this.title = data.title
      this.aid = parseInt(data.id)
      // 获取封面数据并展示
      let list = data.cover.split(",").filter(item => item && item.trim())
      var that = this
      list.forEach(item => {
        that.imglist.unshift({
          'name': item,
          'url': item
        })
      })
      this.imgs = data.cover
    }
  },

  methods: {
    onEditorReady (editor) { // 准备编辑器

    },
    // 失去焦点事件
    onEditorBlur () {

    },
    onEditorFocus () { }, // 获得焦点事件
    // 内容改变事件
    onEditorChange () {
      this.str = this.escapeStringHTML(this.content)
    },
    // 转码
    escapeStringHTML (str) {
      str = str.replace(/&lt;/g, '<');
      str = str.replace(/&gt;/g, '>');
      return str;
    },
    handleRemove (file, fileList) {
      console.log(file, fileList);
      fileList.filter(item => item.url && item.url.trim()).forEach(item => {
        this.imgs += item.url + ''
      })
      this.imglist = fileList

    },
    handlePictureCardPreview (file) {
      console.log(file);
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    handleUploadSuccess (file, fileList) {
      console.log('success', file, fileList);
      this.dialogVisible = false
      this.imgs += file.data.url + ','
    },
    // 超出上传文件数量回调
    exceedUpload () {
      this.$message.error('封面数量以达上限')
      this.dialogVisible = false
    },
  },
};
</script>

<style scoped>
.edit_container {
  width: 70%;
  background-color: #fff;
  margin: 20px 0px;
  padding: 10px;
}
.edit_container >>> .el-card__body {
  width: 100%;
}
/* 样式穿透取消边框 */
.title >>> .el-input__inner {
  border: 0px;
}
.title {
  font-size: 35px;
  margin-bottom: 20px;
}
</style>