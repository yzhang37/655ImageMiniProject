<template>
  <b-jumbotron>
    <template #header>
      <div class="header">{{ cSelectorTitle }}</div>
    </template>
    <template #lead>
      <div class="lead">{{ cSelectorSubTitle }}</div>
    </template>
    <hr class="my-4">
    <b-form-file
        v-model="dataFileList"
        :state="cIsFileSelected" multiple
        accept="image/*"
        :placeholder="cPlaceHolder"
        :drop-placeholder="cDropPlaceHolder"
    ></b-form-file>
    <div class="mt-3">Selected file: {{ file1 ? file1.name : '' }}
      <b-badge class="file-badge" :key="item.name"
               variant="info" v-for="(item) in dataFileList">
        <img class="icon" src="../assets/imgicon.png" alt=""/>{{ item.name }}
      </b-badge>
    </div>
    <b-button variant="primary">{{ cUploadTitle }}</b-button>
    <b-button variant="outline-primary">{{ cAboutTitle }}</b-button>
  </b-jumbotron>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

const ImageSelectorProps = Vue.extend({
  props: {
    caption: String,
    subTitle: String,
    placeholder: String,
    dropPlaceholder: String,
    uploadTitle: String,
    aboutTitle: String,
  }
})

@Component
export default class ImageSelector extends ImageSelectorProps {
  dataFileList: File[] = [];

  get cSelectorTitle(): string {
    return (this.caption !== undefined) ? this.caption : "CS655: 图像识别网络模拟器";
  }

  get cSelectorSubTitle(): string {
    return (this.subTitle !== undefined) ? this.subTitle : "请选择图片文件，然后点击“上传图片”，即可开始图片运行。";
  }

  get cPlaceHolder(): string {
    return (this.placeholder !== undefined) ? this.placeholder : "Select pictures or drop it here...";
  }

  get cDropPlaceHolder(): string {
    return (this.dropPlaceholder !== undefined) ? this.dropPlaceholder : "Drop pictures here...";
  }

  get cUploadTitle(): string {
    return (this.uploadTitle !== undefined) ? this.uploadTitle : "Upload";
  }

  get cAboutTitle(): string {
    return (this.aboutTitle !== undefined) ? this.aboutTitle : "About";
  }

  get cIsFileSelected(): boolean {
    return this.dataFileList.length > 0;
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header {
  font-size: 28px;
}

.lead {
  font-size: 20px;
}

.file-badge {
  font-size: 14px;
  margin-bottom: 4px;
  margin-right: 4px;
  cursor: default;
}

.icon {
  width: 14px;
  margin: 2px;
}

</style>
