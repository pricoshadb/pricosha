import './plugins/axios'

window.pricosha = {
  /***
  @return {item_id, email_post, post_time, file_path, and item_name}
  ***/
  getPublicPosts() {
    return axios.get('/public_content', {
        baseURL: 'http://45.55.50.40'
      });
  },
  login(username, password) {
    return axios.get('/login', {
      baseURL: 'http://45.55.50.40',
      auth: {
        username: username,
        password: password
      }
    });
  }
};
