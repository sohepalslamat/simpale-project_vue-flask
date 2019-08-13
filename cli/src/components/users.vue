<template >
    <div>
        
        <ul>
            <li v-for="user in users" :key="user.id" >id: {{user.id}} // name : {{user.name}} // age : {{user.age}} 
              <button class="btn btn-outline-dark" @click="deleteUser(user.id)">x</button>
            </li>
        </ul>
    </div>
</template>

<script>

export default {
  
    data: function() {
        return{
        users : []
    }},
    created : function() {
        this.getUsers()  
      },

    methods:{
    getUsers() {
      // GET /someUrl
      this.$http.get('http://127.0.0.1:5000/users').then(response => {
    
        /* eslint-disable no-console */
        this.users = response.body;
        }, error => {
         console.error(error); })    
    },
    deleteUser(id){
    this.$http.delete('http://127.0.0.1:5000/users/'+id).then(response => {
      this.getUsers();    
        /* eslint-disable no-console */
        console.log(response);
        }, error => {
         console.error(error); })   
    }}
    
}
</script>


<style>

</style>

