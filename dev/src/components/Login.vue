<template>
  <v-card>
    <v-toolbar dark color="primary">
      <v-toolbar-title>Login form</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-form>
        <v-text-field v-model='email' prepend-icon="person" name="login" label="Email" type="text"></v-text-field>
        <v-text-field v-model='password' id="password" prepend-icon="lock" name="password" label="Password" type="password"></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="primary" @click='login(email, password)'>Login</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
  export default {
    name: 'Login',
    data() {
      return {
        email: null,
        password: null
      }
    },
    methods: {
      login(email, password) {
        pricosha.login(email, password).then(response => {
          this.$emit('success')
        }).catch(error => {
          console.error(error);
        }).then(() => {
          this.$emit('end_dialog')
        });
      }
    }
  }
</script>
