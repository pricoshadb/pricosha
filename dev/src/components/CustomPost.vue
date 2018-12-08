<template>
  <v-card>
    <v-layout row wrap>
      <v-img
        aspect-ratio='1'
        :src="path || 'https://pricosha.drew.hu/img/none.jpg'">
      </v-img>
      <v-layout col>
        <v-card-text class="pt-1 pb-0">
          <v-layout column>
            <v-form ref='form'>
              <v-text-field solo hide-details label="Title" v-model="item_name" class="pt-2"></v-text-field>
              <FileUpload class="pt-2"
              @url='path=$event'
              @file='image_content=$event'>
              </FileUpload>
              <v-layout wrap>
                <v-checkbox
                  hide-details
                  v-model="is_pub"
                  label='public'>
                </v-checkbox>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click='submit'>Submit</v-btn>
              </v-layout>
            </v-form>
          </v-layout>
        </v-card-text>
      </v-layout>

    </v-layout>
  </v-card>
</template>

<script>
import FileUpload from './FileUpload.vue'

export default {
  name: 'CustomPost',
  data() {
    return {
      item_name: '',
      is_pub: false,
      image_content: null,
      path: '',
    }
  },
  components: {
    FileUpload
  },
  props: {

  },
  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        let data = new FormData()
        data.append('item_name', this.item_name)
        data.append('is_pub', this.is_pub)
        data.append('image_content', this.image_content)
        pricosha.setPost(data).then(response => {
          this.$emit('submit')
        })
      }
    }
  }
}
</script>

<style lang="css">
</style>
