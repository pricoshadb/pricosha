import './plugins/axios'
axios.defaults.baseURL = 'http://127.0.0.1:5000'//'http://45.55.50.40'
window.pricosha = {
  /***
  @return {item_id, email_post, post_time, file_path, item_name}
  ***/
  getPublicPosts() {
    return axios.get('/public_content');
  },
  getPosts(url) {
    return axios.get(url);
  },
  getPost(id) {
    return axios.get('/item/'+id);
  },
  setTagged() {
    return axios.put('/tagged')
  },
  login(username, password) {
    return axios.get('/login', {
      auth: {
        username: username,
        password: password
      }
    });
  }
};
