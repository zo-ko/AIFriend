<script setup>
import {ref, watch} from "vue";

const props = defineProps(['profile'])
const myProfile = ref(props.profile)

watch(() => props.profile, newValue => {
  myProfile.value = newValue;
})

defineExpose({
  myProfile,
})
</script>

<template>
  <fieldset class="fieldset">
    <label class="label text-base">Profile</label>
    <textarea rows="6" class="textarea w-108" v-model="myProfile"></textarea>
  </fieldset>
</template>

<style scoped>

</style>