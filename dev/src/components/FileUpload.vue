<template lang="html">
	<v-flex xs12 class="text-xs-center">
		<!-- <img :src="imageUrl" height="150" v-if="imageUrl"/> -->
		<v-text-field solo label="Select Image"
      @click='pickFile'
      v-model='imageName' 
      append-icon='attach_file'
      hide-details>
    </v-text-field>
		<input
			type="file"
			style="display: none"
			ref="image"
			accept="image/*"
			@change="onFilePicked">
	</v-flex>
</template>

<script>
export default {
  name: 'FileUpload',
  data() {
    return {
  		imageName: '',
  		imageUrl: '',
  		imageFile: '',
    }
  },
  methods: {
    pickFile () {
      this.$refs.image.click ()
    },
  	onFilePicked (e) {
  		const files = e.target.files
  		if(files[0] !== undefined) {
  			this.imageName = files[0].name
  			if(this.imageName.lastIndexOf('.') <= 0) {
  				return
  			}
  			const fr = new FileReader ()
  			fr.readAsDataURL(files[0])
  			fr.addEventListener('load', () => {
  				this.imageUrl = fr.result
  				this.imageFile = files[0] // this is an image file that can be sent to server...
  			})
    		} else {
    			this.imageName = ''
    			this.imageFile = ''
    			this.imageUrl = ''
    		}
	   }
  },
  watch: {
    imageUrl: {
      handler (val, old) {
        this.$emit('url', val)
      }
    },
    imageFile: {
      handler (val, old) {
        this.$emit('file', val)
      }
    }
  }
}
</script>

<style lang="css">
</style>
