<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      fixed
      app>
      <v-list dense>
        <v-list-tile @click="">
          <v-list-tile-action>
            <v-icon>home</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile @click='login_form=true'>
          <v-list-tile-action>
            <v-icon>person</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Login</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-dialog
        v-model="login_form">
          <Login @end_dialog='login_form=false'></Login>
        </v-dialog>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color="indigo" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>PriCoSha</v-toolbar-title>
    </v-toolbar>
    <v-content>
      <!-- {item_id, email_post, post_time, file_path, and item_name} -->
        <Posts></Posts>
    </v-content>
    <v-footer color="indigo" app>
      <span class="white--text">&copy; 2018 // Maxwell Colin Reddy // Lucas Pollice // Khoa Nguyen // Andrew Hu</span>
    </v-footer>
  </v-app>
</template>

<script>
  import Login from './components/Login.vue'
  import Posts from './components/Posts.vue'
  import './api'

  export default {
    name: 'App',
    components: {
      Login,
      Posts
    },
    data() {
      return {
        login_form: null,
        drawer: null,
      }
    }
  }
</script>
