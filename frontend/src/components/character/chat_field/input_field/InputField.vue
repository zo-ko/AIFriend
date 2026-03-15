<script setup>

import SendIcon from "@/components/character/icons/SendIcon.vue";
import MicIcon from "@/components/character/icons/MicIcon.vue";
import {ref, useTemplateRef} from "vue";
import api from "@/js/http/api.js";
import streamApi from "@/js/http/streamApi.js";
import Mircophone from "@/components/character/chat_field/input_field/Mircophone.vue";


const inputRef = useTemplateRef('input-ref')
const message = ref('')
const props = defineProps(['friendId'])
const emit = defineEmits(['pushBackMessage', 'addToLastMessage']);
const showMic = ref(false)
let isProcessing = false
let processId = 0

function focus(){
  inputRef.value.focus()
}

async function handleSend(event,audio_msq){
  let content
  if(audio_msq){
    content=audio_msq.trim()
  } else{
     content = message.value.trim()
  }
  if(!content) return

  const curId = ++processId

  message.value = ''

  emit('pushBackMessage', {role: 'user',content: content,id: crypto.randomUUID()})
  emit('pushBackMessage', {role: 'ai',content: '',id: crypto.randomUUID()})

  try {
    await streamApi('/api/friend/message/chat/', {
      body: {
        friend_id: props.friendId,
        message: content
      },
      onmessage(data, isDone) {
        if(curId !== processId) return
        if (data.content) {
          emit('addToLastMessage', data.content)
        }
      },
      onerror(err) {

      },
    })
  } catch (err) {
    console.log(err)

  }
}

function close(){
  ++ processId
  showMic.value = false
}

function handleStop(){
  ++ processId
}

defineExpose({
  focus,
  close,
})
</script>

<template>
  <form v-if="!showMic" @submit.prevent="handleSend" class="absolute bottom-4 left-2 h-12 w-86 flex items-center">
    <input v-model="message" ref="input-ref" class="input bg-black/30 text-white text-base backdrop-blur-sm w-full h-full rounded-2xl pr-20"
            type="text"
            placeholder="文本输入......"
    >
    <div @click="handleSend" class="absolute right-2 w-8 h-8 flex justify-center items-center cursor-pointer">
      <SendIcon/>
    </div>
    <div @click="showMic = true" class="absolute right-8 w-8 h-8 flex justify-center items-center cursor-pointer">
      <MicIcon/>
    </div>
  </form>
  <Mircophone
      v-else
      @close="showMic = false"
      @send="handleSend"
      @stop="handleStop"
  />
</template>

<style scoped>

</style>