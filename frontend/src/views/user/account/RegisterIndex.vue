<script setup>
import {ref} from "vue";
import api from "@/js/http/api.js";
import {useUserStore} from "@/stores/user.js";
import {useRouter} from "vue-router";

const username = ref("");
const password = ref("");
const passwordConfirmed = ref("");
const errorMessage = ref("");

const user=useUserStore()
const router = useRouter();

async function handleRegister() {
  errorMessage.value = ''
  if(!username.value.trim()){
    errorMessage.value='用户名不能为空'
  } else if(!password.value.trim()){
    errorMessage.value='密码不能为空'
  } else if(password.value.trim() !== passwordConfirmed.value.trim()){
    errorMessage.value='两次密码输入不相同'
  } else {
    try {
      const res = await api.post("api/user/account/register/", {username:username.value,password:password.value})
      const data = res.data
      if(data.result === 'success') {
        user.setAccessToken(data.access)
        user.setUserInfo(data)
        await router.push({
          name: 'home-pageindex'
        })
      }else{
        errorMessage.value = data.result
      }
    }catch(err){
      console.log(err)
    }
  }
}
</script>


<template>
  <div class="flex justify-center mt-30">
    <form @submit.prevent="handleRegister" class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
      <h2 class="text-xl font-bold mb-4 text-center">用户注册</h2>

      <label class="label">用户名</label>
      <input v-model="username" type="text" class="input" placeholder="请输入用户名"/>


      <label class="label">密码</label>
      <input v-model="password" type="password" class="input" placeholder="请输入密码"/>

      <label class="label">确认密码</label>
      <input v-model="passwordConfirmed" type="password" class="input" placeholder="请再次输入密码"/>

      <p v-if="errorMessage" class="text-sm text-red-500 mt-1">{{ errorMessage }}</p>

      <button type="submit" class="btn btn-primary mt-4">注册</button>

      <div class="flex justify-center mt-4">
        <router-link :to="{name:'user-account-login-pageindex'}" class="btn btn-sm btn-ghost">已有账号？去登录</router-link>
      </div>
    </form>
  </div>
</template>


<style scoped>

</style>