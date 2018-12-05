import './plugins/axios'
axios.defaults.baseURL = 'https://pricoshaapi.drew.hu'//'127.0.0.1:5000'//'http://45.55.50.40'
window.pricosha = {
  getPosts(url='public', page=1,results_per_page=10) {
    return axios.get('/posts/' + url, {
      params: {
        page: page,
        results_per_page: results_per_page,
      }
    });
  },
  getPost(id) {
    // return axios.get('https://pricoshaapi.drew.hu/item/'+id);
    return axios.get('/item/%s' % id);
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
