<template lang="html">
  <v-chip close>
    <!-- <v-avatar>
      <img src="user.avatar" alt="A">
    </v-avatar> -->
    {{user.first_name}} {{user.last_name}}
  </v-chip>
</template>

<script>
export default {
  name: 'UserChip',
  props: {
    email: String
  },
  data() {
    user: {}
  },
  watch: {
    email: {
      handler (val, old) {
        pricosha.getUser(val).then(response => {
          this.user = response.data
        })
      }
    }
  }
}
</script>

<style lang="css">
</style>
