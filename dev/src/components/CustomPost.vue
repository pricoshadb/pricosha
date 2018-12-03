<template>
  <v-card>
    <v-layout row>
      <v-flex shrink>
      </v-flex>
      <v-layout col>
        <v-card-title class="pt-1 pb-0">
          <div>
            <h3 class="headline mb-0">{{item.item_name}}</h3>
            <span>{{item.email}}</span>
            <v-layout row  v-if='item.tagged'>
              <!-- <span v-if='item.tagged'> &mdash; </span> -->
              <v-subheader class='px-0'>{{item.tagged.join(", ")}}</v-subheader>
              <v-text-field
              v-model='tag_value'
              label='+'
              hide-details
              @keyup.enter='addTag(item, $event)'
              solo flat>
              </v-text-field>
            </v-layout>
          </div>
        </v-card-title>
        <v-spacer></v-spacer>
        <v-card-actions>
          <v-btn color="primary">Submit</v-btn>
        </v-card-actions>
      </v-layout>

    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: 'CustomPost',
  data() {
    return {
      tag_value: '',
    }
  },
  props: {
    item: {
      type: Object,
      required: false
    }
  },
  methods: {
    addTag() {
      pricosha.setTagged(this.item, this.tag_value)
      this.tag_value=''
      this.$emit('dirty')
    }
  }
}
</script>

<style lang="css">
</style>
