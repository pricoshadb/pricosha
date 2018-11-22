<template>
    <v-card class="elevation-12">
      <v-toolbar dark color="primary">
        <v-toolbar-title>Login form</v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-form>
          <v-text-field v-model='username' prepend-icon="person" name="login" label="Login" type="text"></v-text-field>
          <v-text-field v-model='password' id="password" prepend-icon="lock" name="password" label="Password" type="password"></v-text-field>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" @click='login(username, password)'>Login</v-btn>
      </v-card-actions>
    </v-card>
</template>

<script>
  export default {
    name: 'Login',
    data() {
      return {
        username: null,
        password: null
      }
    },
    methods: {
      login(username, password) {
        pricosha.login(username, password).then(response => {
        }).catch(error => {
          // if (response.status == 400)
          console.error(error);
        }).then(() => {
          this.$emit('end_dialog');
        });
      }
    }
  }
</script>
