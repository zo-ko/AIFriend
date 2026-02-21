<script setup>
import {ref, watch} from "vue";

const props = defineProps(['username'])
const myUsername = ref(props.username)

watch(() => props.username, newValue => {
  myUsername.value = newValue;
})

defineExpose({
  myUsername,
})
</script>

<template>
  <fieldset class="fieldset">
    <label class="label text-base">Username</label>
    <input v-model="myUsername" class="input w-108" type="text">
  </fieldset>
</template>

<style scoped>

</style>