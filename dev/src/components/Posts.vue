<template>
  <v-container>
    <Post
    v-for="item, i in content"
    :key="item.item_id"
    :item='item'
    @dirty='updatePosts()'>
    </Post>
  </v-container>
</template>

<script>
import Post from './Post.vue'

export default {
  name: 'Posts',
  props: {
    src: {
      type: String,
      default: '',
    }
  },
  components: {
    Post,
  },
  methods: {
    updatePost(item_id) {
      pricosha.getPost(item_id).then(
        response => {})
    },
    updatePosts() {
      if (this.src)
        pricosha.getPosts(this.src).then(
          response => {
            this.content = response.data;
          });
      else
        pricosha.getPublicPosts().then(
          response => {
            this.content = response.data;
          });
    }
  },
  data() {
    return {
      content: [],
    }
  },
  created() {
    this.updatePosts()
  }
}
</script>

<style lang="css">
</style>
