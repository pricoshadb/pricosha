<template>
  <v-container fluid fill-height>
    <v-layout column>
      <v-card flat v-if='create_new==false && pricosha.authed'>
        <v-layout row justify-center class="py-2">
          <v-btn large color="primary" @click='create_new=true'>
            <v-icon>add</v-icon>
          </v-btn>
        </v-layout>
      </v-card>
      <CustomPost v-if='create_new==true'
      @submit='create_new=false;updatePosts()'></CustomPost>
      <Post
      v-for="item, index in content"
      :key="item.item_id"
      :item='item'
      :group_names='group_names'
      @dirty='updatePost(item.item_id, index)'>
      </Post>
      <v-spacer></v-spacer>
      <v-layout row justify-center align-center shrink>
        <v-btn fab small depressed
        :disabled='page<=1'
        @click='page--'>
          <v-icon>chevron_left</v-icon>
        </v-btn>
        <v-btn fab depressed style="pointer-events: none;">
          {{page}}
        </v-btn>
        <v-btn fab small depressed
        @click='page++'>
          <v-icon>chevron_right</v-icon>
        </v-btn>
      </v-layout>
    </v-layout>
  </v-container>
</template>

<script>
import Post from './Post.vue'
import CustomPost from './CustomPost.vue'

export default {
  name: 'Posts',
  props: {
    src: {
      type: String,
      default: 'public',
    }
  },
  components: {
    Post,
    CustomPost,
  },
  data() {
    return {
      content: [],
      page: 1,
      group_names: [],
      create_new: false
    }
  },
  methods: {
    updatePost(item_id, index) {
      this.pricosha.getPost(item_id).then(
        response => {
          this.content[index] = response.data
        })
    },
    updatePosts() {
      this.pricosha.getPosts(this.src, this.page).then(
        response => {
          this.content = response.data;
        });
    }
  },
  created() {
    this.updatePosts()
    this.pricosha.getGroups(true).then(response => {
      this.group_names = response.data
    })
  },
  watch: {
    src: {
      handler (val, old) {
        this.updatePosts()
      }
    },
    page: {
      handler() {
        this.updatePosts()
      }
    }
  }
}
</script>

<style lang="css">
</style>
