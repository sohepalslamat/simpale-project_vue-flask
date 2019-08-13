<template>
    <ul class="nav nav-pills">
    <li class="nav-item">
      <router-link :to="{name: 'home'}" class="nav-link" active-class='active' exact >Home</router-link>
    </li>
    <li class="nav-item">
      <router-link :to="{name: 'users'}" class="nav-link" active-class='active' href="#">users</router-link>
    </li>
    <li class="nav-item">
      <router-link :to="{name: 'adduser'}" class="nav-link" active-class='active' href="#">adduser</router-link>
    </li>
    
    
  </ul>
</template>

<script>
export default {
    
}
</script>

