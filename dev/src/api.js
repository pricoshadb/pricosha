import './plugins/axios'
axios.defaults.baseURL = 'https://pricoshaapi.drew.hu'//'127.0.0.1:5000'//'http://45.55.50.40'
window.pricosha = {
  /***
  @return {item_id, email_post, post_time, file_path, item_name}
  ***/
  getPublicPosts() {
    // return axios.get('https://pricoshaapi.drew.hu/public_content');
    return axios.get('/public_content');
  },
  getPosts(url) {
    return axios.get(url);
  },
  getPost(id) {
    // return axios.get('https://pricoshaapi.drew.hu/item/'+id);
    return axios.get('/item/'+id);
  },
  setTagged() {
    // return axios.put('https://pricoshaapi.drew.hu/tagged')
    return axios.put('/tagged')
  },
  login(email, password) {
    // return axios.post('https://pricoshaapi.drew.hu/login', {
    return axios.post('/login', {
      auth: {
        email: email,
        password: password
      }
    });
  },
  logout() {
    // return axios.get('https://pricoshaapi.drew.hu/logout');
    return axios.get('/logout');
  }
};
