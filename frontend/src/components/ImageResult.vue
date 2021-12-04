<template>
  <b-card
      :title="cDisplayTitle"
      :img-src="imgSrc"
      :img-alt="cDisplayTitle"
      img-top
      tag="article"
      style="max-width: 20rem;"
      class="mb-2 my-card">
    <b-card-text>
      <div v-if="!isOk" class="text-center">
        <b-button variant="primary" disabled>
          <b-spinner small></b-spinner>
          Recognizing...
        </b-button>
      </div>
      <div v-else>
        <hr class="my-4">
        {{ cResultValue }}
      </div>
    </b-card-text>

  </b-card>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

const imgResultProps = Vue.extend({
  props: {
    display: String,
    imgSrc: String,
    ok: Boolean,
    value: String,
  }
});

@Component
export default class ImageResult extends imgResultProps {
  get cDisplayTitle(): string {
    return this.display ?? "<No Picture Filename>";
  }

  get isOk(): boolean {
    return this.ok ?? false;
  }

  get cResultValue(): string {
    return this.value ?? "No result to show.";
  }
}
</script>

<style>
.my-card {
  box-shadow: 5px 5px 8px rgba(0,0,0,0.75);
  margin: 0 15px 15px 0;
}
</style>