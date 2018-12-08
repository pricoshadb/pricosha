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
        <v-btn flat icon>
          <v-icon>share</v-icon>
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
      saved: false,
    }
  },
  props: {
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
    }
  }
}
</script>

<style lang="css">
</style>
