<template>
  <v-card>
    <v-img
      :src="item.file_path">
    </v-img>
    <v-card-title class="pt-1 pb-0">
      <div>
        <v-layout row>
          <h3 class="headline mb-0">{{item.item_name}}</h3>
          <EmojiBar @emoji='rate($event)' :emotes='ratings'></EmojiBar>
        </v-layout>
        <UserChip :email='item.email' color='primary' text-color='white'></UserChip>
        <v-layout row  v-if='item.tagged'>
          <!-- <span v-if='item.tagged'> &mdash; </span> -->
          <v-subheader class='px-0' v-for='tag_email in item.tagged'>
            <UserChip :email='tag_email'></UserChip>
          </v-subheader>
          <v-text-field
          v-model='tag_value'
          label='+'
          hide-details
          @keyup.enter='addTag(item, $event)' solo flat>
          </v-text-field>
        </v-layout>
      </div>
    </v-card-title>
    <v-card-actions>
      <v-btn flat icon color="yellow"
        @click='toggleSave()'>
        <v-icon v-if='saved'>bookmark</v-icon>
        <v-icon v-else>bookmark_border</v-icon>
      </v-btn>
      <v-menu>
        <v-btn flat icon @click='share_state=true'
        slot='activator'>
          <v-icon>share</v-icon>
        </v-btn>
        <v-card>
          <v-select
            :items='group_names'
            label='groups'
            @input='sharePost($event)'>
          </v-select>
        </v-card>
      </v-menu>
      <v-btn flat icon color="primary"
      @click='show_comments=!show_comments'>
        <v-icon>chat</v-icon>
      </v-btn>
    </v-card-actions>
    <v-divider></v-divider>
    <v-card-text v-show='show_comments'>
      <div class='commentdrop'>
        <v-card outline flat color='grey lighten-5'
        class='ma-1 textwrap'
        v-for='comment in comments' :key='comment.email'>
          <v-card-text class='pa-1'>
            <!-- <UserChip :email='comment.email'></UserChip> -->
            <br>
            {{comment.content}}
          </v-card-text>
        </v-card>
      </div>
      <v-text-field single-line
      label="comment"
      @keyup.enter='comment()'
      v-model="comment_value">
      </v-text-field>
    </v-card-text>
  </v-card>
</template>

<script>
import EmojiBar from './EmojiBar.vue'
import UserChip from './UserChip.vue'

export default {
  name: 'Post',
  components: {
    EmojiBar,
    UserChip
  },
  data() {
    return {
      show_comments: false,
      tag_value: '',
      comment_value: '',
      share_state: false,
      saved: false,
      comments: [],
      ratings: []
    }
  },
  props: {
    group_names: Array,
    item: {
      type: Object,
      required: true
    }
  },
  methods: {
    addTag() {
      this.pricosha.setTagged(this.item.item_id, this.tag_value)
      this.tag_value=''
      this.$emit('dirty')
    },
    toggleSave() {
      this.saved = !this.saved
      if (this.saved)
        this.pricosha.setSaved(this.item.item_id)
      else
        this.pricosha.removeSaved(this.item.item_id)
    },
    sharePost(group) {
      this.pricosha.setShare(this.item.item_id, group)
    },
    comment() {
      this.pricosha.setComment(this.item.item_id, this.comment_value).then(response=> {
        this.comments.push({
          content: this.comment_value
        })
        this.comment_value=''
      })
    },
    rate(emoji) {
      this.pricosha.setRating(this.item.item_id, emoji)
    }
  },
  created() {
    this.pricosha.getComments(this.item.item_id).then(response => {
      this.comments = response.data
    })
    this.pricosha.getRatings(this.item.item_id).then(response => {
      this.ratings = response.data
    })
  }
}
</script>

<style lang="css">
.textwrap {
  overflow-wrap: break-word;
  word-wrap: break-word;
  hyphens: auto;
}
.groups_picker  {
  width: 20rem;
  height: 30rem;
  position: absolute;
}
.commentdrop {
  max-height: 30em;
  overflow-y: auto;
  overflow-x: hidden;
}
</style>
