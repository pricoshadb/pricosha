<template>
  <v-container>
    <v-card flat v-if='create_new==false'>
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
    @dirty='updatePost(item.item_id, index)'>
    </Post>
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
      content: [{
        tagged: ['email1@gmail.com', 'email2@gmail.com'],
        email: 'author@gmail.com',
        item_name: 'Title1',
        file_path: 'https://i.redd.it/nb6w56a10x221.jpg',

      }],
      create_new: false
    }
  },
  methods: {
    updatePost(item_id, index) {
      pricosha.getPost(item_id).then(
        response => {
          this.content[index] = response.data
        })
    },
    updatePosts() {
      pricosha.getPosts(this.src).then(
        response => {
          this.content = response.data;
        });
    }
  },
  created() {
    this.updatePosts()
  },
  watch: {
    src: {
      immediate: true,
      handler (val, old) {
        this.updatePosts()
      }
    }
  }
}
</script>

<style lang="css">
</style>
