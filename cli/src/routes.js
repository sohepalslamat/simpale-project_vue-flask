import users from './components/users'
import addUser from './components/addUser'
import home from './components/home'
const routes = [
    {path:'/', component: home, name: 'home'},
    {path:'/users', component: users, name: 'users'},
    {path:'/adduser', component: addUser, name: 'adduser'},

]
export default routes