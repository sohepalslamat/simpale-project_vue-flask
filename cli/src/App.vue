<template>
  <div id="app">
    <NavBar></NavBar>
    <router-view></router-view>
  </div>
</template>

<script>

import NavBar from './components/NavBar'
export default {
  name: 'app',
  components: {
    NavBar
    
    
  }
}
</script>

<style>

</style>
