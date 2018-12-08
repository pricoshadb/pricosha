import './plugins/axios'
axios.defaults.baseURL = 'https://pricoshaapi.drew.hu'//'127.0.0.1:5000'//'http://45.55.50.40'
window.pricosha = {
  getPosts(url='public', page=1,results_per_page=10) {
    return axios.get('/posts/' + url, {
      params: {
        page: page,
        results_per_page: results_per_page,
      }
    }).then(function(response){
      console.log(response)
    })
  },
  setTagged(post_id) {
    return axios.post('/tags/create', {
      data: {
        post_id: post_id
      }
    }).then(function(response){
      console.log(response)
    })
  },
  getProposedTags() {
    return axios.get('/tags/proposed', {
      params: {
        page: page,
        results_per_page: results_per_page,
      }
    }).then(function(response){
      console.log(response)
    })
  },
  modifyProposedTag(item_id, decision) {
    return axios.post('/tags/modify', {
      data: {
        item_id: item_id,
        decision: decision
      }
    }).then(function(response){
      console.log(response)
    })
  },
  getPost(item_id) {
    return axios.get('/item', {
      args: {
        item_id: item_id
      }
    }).then(function(response){
      console.log(response)
    })
  },
  getUser(email) {
    return axios.get('/user', {
      args: {
        email: email
      }
    }).then(function(response){
      console.log(response)
    })
  },
  setFriend(email) {
    return axios.post('/friend', {
      args: {
        email: email
      }
    }).then(function(response){
      console.log(response)
    })
  },
  removeFriend(email) {
    return axios.post('/unfriend', {
      args: {
        email: email
      }
    }).then(function(response){
      console.log(response)
    })
  },
  setPost(formdata) { // Must be form for file upload
    return axios.post('/post/create', formdata)
  },
  getGroups(fg_name) {
    return axios.post('/groups', {
      args: {
        fg_name: fg_name
      }
    }).then(function(response){
      console.log(response)
    })
  },
  setGroup(fg_name) {
    return axios.post('/group/create', {
      args: {
        fg_name: fg_name
      }
    }).then(function(response){
      console.log(response)
    })
  },
  removeGroup(fg_name) {
    return axios.post('/group/remove', {
      args: {
        fg_name: fg_name
      }
    }).then(function(response){
      console.log(response)
    })
  },
  setGroupMember(fg_name, email) {
    return axios.post('/group/members/add', {
      args: {
        fg_name: fg_name,
        email: email
      }
    }).then(function(response){
      console.log(response)
    })
  },
  removeGroupMember(fg_name, email) {
    return axios.post('/group/members/remove', {
      args: {
        fg_name: fg_name,
        email: email
      }
    }).then(function(response){
      console.log(response)
    })
  },
  setShare(item_id, fg_name) {
    return axios.post('/post/share', {
      args: {
        item_id: item_id,
        fg_name: fg_name
      }
    }).then(function(response){
      console.log(response)
    })
  },
  setSaved(post_id) {
    return axios.post('/post/save', {
      data: {
        post_id: post_id
      }
    }).then(function(response){
      console.log(response)
    })
  },
  removeSaved(post_id) {
    return axios.post('/post/unsave', {
      data: {
        post_id: post_id
      }
    }).then(function(response){
      console.log(response)
    })
  },
  register(email, password, first_name, last_name) {
    return axios.post('/register', {
      auth: {
        email: email,
        password: password
      }
    }).then(function(response){
      console.log(response)
    })
  },
  login(email, password) {
    return axios.post('/login', {
      auth: {
        email: email,
        password: password
      }
    }).then(function(response){
      console.log(response)
    })
  },
  logout() {
    return axios.get('/logout')
  },
  resetPassword(email, old_password, new_password) {
    return axios.post('/reset', {
      data: {
        old_password: old_password,
        new_password: new_password
      }
    }).then(function(response){
      console.log(response)
    })
  }
};
