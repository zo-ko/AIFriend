<script setup>

</script>

<template>
  <div class="flex justify-center mt-30">
    <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
      <legend class="fieldset-legend">Login</legend>

      <label class="label">用户名</label>
      <input type="text" class="input" placeholder="Email"/>

      <label class="label">密码</label>
      <input type="password" class="input" placeholder="Password"/>

      <button class="btn btn-neutral mt-4">登录</button>
      <div class="flex justify-center">
        <router-link :to="{name:'user-account-register-pageindex'}" class="btn btn-sm btn-ghost">注册</router-link>
      </div>
    </fieldset>
  </div>
</template>

<style scoped>

</style>