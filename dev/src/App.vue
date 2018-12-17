<template>
  <v-app id="inspire">
    <!-- menu -->
    <v-navigation-drawer
        v-model="drawer"
        fixed
        app>
      <v-list dense>
        <!-- browsing sources -->
        <v-list-tile @click="drawer=false;content_source='public'">
          <v-list-tile-action>
            <v-icon>home</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <!-- logged users only -->
        <template v-if='pricosha.authed'>
          <v-list-tile @click="drawer=false;content_source='shared'">
            <v-list-tile-action>
              <v-icon>share</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Shared Content</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile @click="drawer=false;content_source='saved'">
            <v-list-tile-action>
              <v-icon>bookmark</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Saved Content</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <!-- groups -->
          <v-list-tile @click="drawer=false;groups_dialog=true">
            <v-list-tile-action>
              <v-icon>group</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Groups</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-dialog max-width="600px"
              v-model="groups_dialog">
            <Groups
                @end_dialog='groups_dialog=false'>
            </Groups>
          </v-dialog>
          <!-- friends -->
          <v-list-tile @click="drawer=false;friends_dialog=true">
            <v-list-tile-action>
              <v-icon>favorite</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Friends</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-dialog max-width="600px"
              v-model="friends_dialog">
            <Friends
                @end_dialog='friends_dialog=false'>
            </Friends>
          </v-dialog>
        </template>
        <!-- Login/out -->
        <v-list-tile
            @click='drawer=false;logout()'
            v-if='pricosha.authed'>
          <v-list-tile-action>
            <v-icon>meeting_room</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Logout</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile
            @click='drawer=false;login_dialog=true'
            v-if='!pricosha.authed'>
          <v-list-tile-action>
            <v-icon>meeting_room</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Login</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-dialog max-width="600px"
            v-model="login_dialog">
          <Login
              @end_dialog='login_dialog=false'
              @success='pricosha.authed=true'>
          </Login>
        </v-dialog>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color="indigo" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>PriCoSha</v-toolbar-title>
    </v-toolbar>
    <!-- content -->
    <v-content>
      <Posts :src='content_source'></Posts>
    </v-content>
    <!-- footer -->
    <v-footer color="indigo" app>
      <span class="white--text">@ 2018 // Maxwell Colin Reddy // Lucas Pollice // Khoa Nguyen // Andrew Hu</span>
    </v-footer>
  </v-app>
</template>
<script>
  import Login from './components/Login.vue'
  import Posts from './components/Posts.vue'
  import Friends from './components/Friends.vue'
  import Groups from './components/Groups.vue'
  import './api'
  export default {
    name: 'App',
    components: {
      Login,
      Posts,
      Friends,
      Groups
    },
    data() {
      return {
        groups_dialog: null,
        login_dialog: null,
        friends_dialog: null,
        drawer: null,
        content_source: 'public',
      }
    },
    methods: {
      logout() {
        this.pricosha.logout().then(response => {
          this.pricosha.authed=false
        })
      }
    }
  }
</script>
