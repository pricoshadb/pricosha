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
            {{friend.email}}
          </v-list-tile-content>
          <v-btn round outline color="error" dark
          @click='removeFriend(index)'>unfriend</v-btn>
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
    name: 'Friends',
    data() {
      return {
        friends: []
      }
    },
    methods: {
      removeFriend(index) {
        this.pricosha.removeFriend(friend.email)
        this.friends.splice(index,1)
      }
    },
    created() {
      this.pricosha.getFriends().then(response => {
        this.friends = response.data
      })
    }
  }
</script>
