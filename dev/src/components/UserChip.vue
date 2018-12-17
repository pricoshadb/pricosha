<template lang="html">
  <v-dialog max-width="500">
    <v-chip slot='activator' :color='color' :text-color='textColor' :close='close'>
      <v-avatar v-if='user.avatar'>
        <img :src="user.avatar">
      </v-avatar>
      {{user.first_name}} {{user.last_name}}
    </v-chip>
    <v-card>
      <v-img :aspect-ratio='1' :src='user.avatar'></v-img>
      <v-card-title>
        <div>
          <div class="headline">{{user.first_name}} {{user.last_name}}</div>
          <span class="grey--text">{{email}}</span>
        </div>
      </v-card-title>
      <v-card-text>
        {{user.bio}}
      </v-card-text>
      <v-card-actions>
        <v-btn flat icon color="red"
          @click='toggleFriend()'>
          <v-icon v-if='user.friend'>heart</v-icon>
          <v-icon v-else>heart_border</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
// avatar and dialog profile
export default {
  name: 'UserChip',
  props: {
    email: {
      type: String,
      required: true
    },
    'text-color': String,
    color: String,
    close: Boolean
  },
  data() {
    return {
      user: {
        bio: '',
        avatar: '',
        first_name: '',
        last_name: '',
        friend: false,
      }
    }
  },
  watch: {
    email: {
      immediate: true,
      handler (val, old) {
        this.pricosha.getProfile(val).then(response => {
          this.user = response.data
        })
      }
    }
  },
  methods: {
    toggleFriend() {
      this.user.friend = !this.user.friend
      if (this.user.friend)
        this.pricosha.setFriend(this.email)
      else
        this.pricosha.removeFriend(this.email)
    },
  }
}
</script>

<style lang="css">
</style>
