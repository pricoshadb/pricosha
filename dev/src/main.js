
import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import Api from './api'
// import router from './router'


Vue.config.productionTip = false
Vue.prototype.$pricosha = Api

new Vue({
  // router,
  render: h => h(App)
}).$mount('#app')
