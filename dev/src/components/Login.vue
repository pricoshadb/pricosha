<template>
  <v-card>
    <v-toolbar dark color="primary">
      <v-toolbar-title>Login</v-toolbar-title>

    </v-toolbar>
    <v-card-text>
      <v-form>
        <v-text-field v-model='email' prepend-icon="person" name="login" label="Email" type="text"></v-text-field>
        <v-text-field v-model='password' prepend-icon="lock" name="password" label="Password" type="password" :messages='[error]'></v-text-field>
        <div v-if='show_register'>
          <v-text-field v-model='first_name' prepend-icon=' ' name='first_name' label='First Name' type='text'></v-text-field>
          <v-text-field v-model='last_name' prepend-icon=' ' name='last_name' label='Last Name' type='text'></v-text-field>
        </div>
      </v-form>
      <v-layout column class="text-xs-center" v-if='!show_register'>
        <span class='error--text'>Dont have an account?</span>
        <div>
          <v-btn color="error" small
          @click='show_register=true'>
            Register
          </v-btn>
        </div>
      </v-layout>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="primary"
      v-if='!show_register'
      @click='login()'>
        Login
      </v-btn>
      <v-btn color="error"
      v-else
      @click='register()'>
        Register
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
  export default {
    name: 'Login',
    data() {
      return {
        email: null,
        password: null,
        first_name: '',
        last_name: '',
        show_register: false,
        error: '',
      }
    },
    methods: {
      login() {
        this.pricosha.login(this.email, this.password).then(response => {
          this.pricosha.authed = true
          this.$emit('success')
          this.$emit('end_dialog')
          this.error=''
        }).catch(error => {
          this.error = 'Invalid password'
          console.error(error);
        })
      },
      register() {
        this.pricosha.register(this.email, this.password, this.first_name, this.last_name).then(response => {
          this.show_register = false
          this.login()
        }).catch(error => {
          this.error = 'Registration error'
          console.error(error);
        })
      }
    }
  }
</script>
