<template>
  <div id="app">
    <b-container fluid="sm">
      <ImageSelector
          caption="CS655: Image Recognition Network Simulator"
          subTitle="Select image files, then click Upload to start running the simulation."
      />
    </b-container>
    <b-container class="displayField" fluid="sm">
      <ImageResult v-for="picItem in mainDataList" :key="picItem.requestId"
                   :display="picItem.displayName" :img-src="picItem.imageUrl" :ok="picItem.result !== undefined"
                   :value="picItem.result ? picItem.result.value : ''"
      />
    </b-container>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import ImageSelector from './components/ImageSelector.vue';
import ImageResult from './components/ImageResult.vue';

// 存放自定义的结果的类型
interface RecognitionDataType {
  value: string
}

interface MainPageElement {
  imageUrl: string
  requestId: string
  displayName: string
  result: RecognitionDataType | undefined
}

interface MainPageElementIndex {
  [requestId: string]: MainPageElement
}

@Component({
  components: {
    ImageSelector,
    ImageResult
  },
})
export default class App extends Vue {
  mainDataList: MainPageElement[] = [];
  mainDataIndex: MainPageElementIndex = {};

  constructor() {
    super();
    this.mainDataList.push({
      imageUrl: "https://picsum.photos/600/300/?image=25",
      requestId: "1231212123",
      displayName: "test1.png",
      result: undefined,
    });
    this.mainDataList.push({
      imageUrl: "https://placekitten.com/300/300",
      requestId: "456456456",
      displayName: "test2.png",
      result: { value: "123"},
    });
    this.mainDataList.push({
      imageUrl: "https://picsum.photos/400/400/?image=20",
      requestId: "789789789",
      displayName: "test3.png",
      result: { value: "456"},
    });
    this.mainDataList.push({
      imageUrl: "https://picsum.photos/400/400/?image=20",
      requestId: "78978978119",
      displayName: "test3.png",
      result: { value: "456"},
    });
    this.mainDataList.push({
      imageUrl: "https://picsum.photos/400/400/?image=20",
      requestId: "78978978111119",
      displayName: "test3.png",
      result: { value: "456"},
    });
    this.mainDataList.push({
      imageUrl: "https://picsum.photos/400/400/?image=20",
      requestId: "789789781111111119",
      displayName: "test3.png",
      result: { value: "456"},
    });
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}

.displayField {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
}
</style>
