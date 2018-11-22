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

      <v-layout row>
        <v-flex xs12 sm10 offset-sm1>
        <!-- {item_id, email_post, post_time, file_path, and item_name} -->
          <v-card>
            <v-list two-line>
              <template v-for="item in content">
                <v-list-tile
                  :key="item.item_id"
                  @click="">
                  <v-list-tile-content>
                    <v-list-tile-title>{{item.item_name}}</v-list-tile-title>
                    <v-list-tile-sub-title>{{item.email_post}}</v-list-tile-sub-title>
                  </v-list-tile-content>
                  <v-list-tile-action>
                    <v-list-tile-action-text>{{ item.post_time }}</v-list-tile-action-text>
                    <v-icon>
                      chat
                    </v-icon>
                  </v-list-tile-action>
                </v-list-tile>
              </template>
            </v-list>
          </v-card>
        </v-flex>
      </v-layout>

    </v-content>
    <v-footer color="indigo" app>
      <span class="white--text">&copy; 2018 // Maxwell Colin Reddy // Lucas Pollice // Khoa Nguyen // Andrew Hu</span>
    </v-footer>
  </v-app>
</template>

<script>
  import Login from './components/Login.vue'
  import './api'

  export default {
    name: 'App',
    components: {
      Login
    },
    data() {
      return {
        login_form: null,
        content: [],
        drawer: null,
      }
    },
    created() {
      pricosha.getPublicPosts().then(
        response => {
          this.content = response.data;
        });
    }
  }
</script>
