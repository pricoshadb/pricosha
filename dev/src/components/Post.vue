<template>
  <v-card>
    <v-img
      :src="item.file_path">
    </v-img>
    <v-card-title class="pt-1 pb-0">
      <div>
        <v-layout row>
          <h3 class="headline mb-0">{{item.item_name}}</h3>
          <EmojiBar></EmojiBar>
        </v-layout>
        <span>{{item.email}}</span>
        <v-layout row  v-if='item.tagged'>
          <!-- <span v-if='item.tagged'> &mdash; </span> -->
          <v-subheader class='px-0'>{{item.tagged.join(", ")}}</v-subheader>
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
      <v-btn flat icon @click='share_state=true'>
        <v-icon>share</v-icon>
        <v-card v-show='share_state' @native.blur='share_state=false' class='groups_picker'>
          <v-select
            :items='group_names'
            label='groups'
            @input='sharePost($event)'>
          </v-select>
        </v-card>
      </v-btn>
      <v-btn flat icon color="primary"
      @click='show_comments=!show_comments'>
        <v-icon>chat</v-icon>
      </v-btn>
    </v-card-actions>
    <v-card-text v-show='show_comments'>
      <div class='commentdrop'>
        <v-card outline flat color='grey lighten-5'
        class='ma-1 textwrap'
        v-for='comment in comments' :key='comment.email'>
          <v-card-text class='pa-1'>
            {{comment.email}}
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

export default {
  name: 'Post',
  components: {
    EmojiBar,
  },
  data() {
    return {
      show_comments: false,
      tag_value: '',
      comment_value: '',
      share_state: false,
      saved: false,
      comments: [
        {
          email: 'example email',
          content: `j`
        }
      ]
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
      pricosha.setTagged(this.item, this.tag_value)
      this.tag_value=''
      this.$emit('dirty')
    },
    toggleSave() {
      this.saved = !this.saved
      if (this.saved)
        pricosha.setSaved(this.item_id)
      else
        pricosha.setUnsaved(this.item_id)
    },
    sharePost(e) {
      pricosha.setShared(this.item_id, e)
    },
    comment() {
      pricosha.setComment(this.item.item_id, this.comment_value).then(response=> {
        this.comments.push({
          content: this.comment_value
        })
        this.comment_value=''
      })
    }
  },
  created() {
    pricosha.getComments(this.item.item_id).then(response => {
      this.comments = response.data
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
  position: absolute
}
.commentdrop {
  height: 30em;
  overflow-y: scroll;
  overflow-x: hidden;
}
</style>
