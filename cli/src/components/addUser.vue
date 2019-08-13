<template>
    <div  @keyup.enter="sendData">
        <div class="form-group">
            <label for="staticEmail2" >name: </label>
            <input v-model="user.name" type="text" class="form-control" id="staticEmail2" >
        </div>
        <div class="form-group">
            <label for="inputPassword2">age: </label>
            <input v-model="user.age" type="number"  class="form-control" id="inputPassword2">
        </div>
        <button type="submit" @click.prevent="sendData" class="btn btn-primary mb-2">add</button>
        
    </div>
</template>
<script>
export default {
    
    data: function(){
        return{
            user : {
                name: '',
                age : null
            },
            
            
        }
    },
    methods: {
        
        sendData() {
             let data = this.user;
           return this.$http.post('http://localhost:5000/users', data)
                    .then(response => {
                        /* eslint-disable no-console */
                        console.log(response);
                        data.name = "";
                        data.age = null;
                                                               
                        }, error => {
                        
                        console.error(error);
                        
                         });
                    
        
        }
    }}
    
</script>