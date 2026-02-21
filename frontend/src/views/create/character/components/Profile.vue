<script setup>
import {ref, watch} from "vue";

const props =defineProps(['profile'])
const myProfile = ref(props.profile)

watch(() => props.profile,newVal =>{
  myProfile.value=newVal
})

defineExpose({
  myProfile,
})
</script>

<template>

</template>

<style scoped>

</style>