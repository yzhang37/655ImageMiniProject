<template>
  <div id="app">
    <b-container fluid="sm">
      <ImageSelector
          caption="CS655: Image Recognition Network Simulator"
          subTitle="Select image files, then click Upload to start running the simulation."
          @click-upload="uploadFiles"
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
import SocketioService from './services/socketio.service';

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

interface ApiTaskCallReturn {
  code: number,
  result: string,
  data: {
    task_id: string,
  }
}

interface WsResultReturn {
  task_id: string,
  result: string,
}

@Component({
  components: {
    ImageSelector,
    ImageResult
  },
})
export default class App extends Vue {
  mainDataList: MainPageElement[] = [];
  mainDataDictionary: MainPageElementIndex = {};

  constructor() {
    super();
  }

  created(): void {
    SocketioService.setupSocketConnection();

    SocketioService.Socket.on("result", (data: WsResultReturn): void => {
      if (data.task_id in this.mainDataDictionary) {
        const obj = this.mainDataDictionary[data.task_id];
        Vue.set(obj, "result", {
          value: data.result
        })
      }
    })

  }

  beforeUnmount(): void {
    SocketioService.disconnect();
  }

  generalError(level: number, message: string): void {
    alert(level + ", " + message);
  }

  uploadFiles(fileList: File[]): void {
    for (const file of fileList) {
      this.uploadSingleFile(file);
    }
  }

  async uploadSingleFile(file: File): Promise<void> {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const result = await this.$axios.post('api/task', formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          })
      const data = result.data;
      if (!data['code'] || !data['result']) {
        this.generalError(2, "Unexpected error when calling the manager API.");
        return;
      }
      const callData = data as ApiTaskCallReturn;

      if (callData.code != 100) {
        this.generalError(1, callData.result);
      } else {
        const requestId = callData.data.task_id;

        const element: MainPageElement = {
          imageUrl: `upload/${requestId}`,
          requestId: requestId,
          displayName: file.name,
          result: undefined,
        };
        this.mainDataList.push(element);
        this.mainDataDictionary[requestId] = element;
      }
    } catch (e) {
      this.generalError(1, e.message);
    }
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
