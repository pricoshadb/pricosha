<template>
  <v-card>
    <v-layout row>
      <v-img
        aspect-ratio='1'
        :src="item.file_path">
      </v-img>
      <v-layout col>
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
      </v-layout>
      <v-spacer></v-spacer>
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
        <v-btn flat icon color="primary">
          <v-icon>chat</v-icon>
        </v-btn>
      </v-card-actions>
    </v-layout>
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
      tag_value: '',
      share_state: false,
      saved: false,
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
    }
  }
}
</script>

<style lang="css">
.groups_picker  {
  width: 20rem;
  height: 30rem;
  position: absolute
}
</style>
