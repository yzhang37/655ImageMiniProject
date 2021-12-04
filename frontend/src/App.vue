<template>
  <div id="app">
    <b-container fluid="sm">
      <ImageSelector
          caption="CS655: Image Recognition Network Simulator"
          subTitle="Select image files, then click Upload to start running the simulation."
      />
    </b-container>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import ImageSelector from './components/ImageSelector.vue';

@Component({
  components: {
    ImageSelector
  },
})
export default class App extends Vue {}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
