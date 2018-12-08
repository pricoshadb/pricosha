<template>
  <v-card class='sm-12 md-8 lg-6'>
    <v-toolbar dark color="primary">
      <v-toolbar-title>Friends</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-list>
        <v-list-tile
        v-for="friend, index in friends"
        :key="friend.email">
          <v-list-tile-content>
            <v-list-tile-title>{{friend.first_name}} {{friend.last_name}}</v-list-tile-title>
            <v-list-tile-sub-title>{{friend.email}}</v-list-tile-sub-title>
          </v-list-tile-content>
          <v-btn round outline color="error" dark
          @click='friends.splice(index,1);pricosha.removeFriend(friend.email)'>unfriend</v-btn>
        </v-list-tile>
        <v-list-tile v-if='friends.length==0'>
          <v-layout justify-center>
            <span class="headline grey--text">:(</span>
          </v-layout>
        </v-list-tile>
      </v-list>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: 'Login',
    data() {
      return {
        friends: [
          {
            email: 'example@gmail.com',
            first_name: 'Lucas',
            last_name: 'OhZia'
          }
        ]
      }
    }
  }
</script>
