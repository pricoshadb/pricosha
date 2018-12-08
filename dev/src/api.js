import './plugins/axios'
axios.defaults.baseURL = 'https://pricoshaapi.drew.hu'//'127.0.0.1:5000'//'http://45.55.50.40'
window.pricosha = {
  getPosts(url='public', page=1,results_per_page=10) {
    return axios.get('/posts/' + url, {
      params: {
        page: page,
        results_per_page: results_per_page,
      }
    })
  },
  setTagged(post_id) {
    return axios.post('/tags/create', {
      data: {
        post_id: post_id
      }
    })
  },
  getProposedTags() {
    return axios.get('/tags/proposed', {
      params: {
        page: page,
        results_per_page: results_per_page,
      }
    })
  },
  removeProposedTag(post_id) {
    return axios.post('/tags/deny', {
      data: {
        post_id: post_id
      }
    })
  },
  getPost(item_id) {
    return axios.get('/item', {
      args: {
        item_id: item_id
      }
    })
  },
  getUser(email) {
    return axios.get('/user', {
      args: {
        email: email
      }
    })
  },
  setFriend(email) {
    return axios.post('/friend', {
      args: {
        email: email
      }
    })
  },
  removeFriend(email) {
    return axios.post('/unfriend', {
      args: {
        email: email
      }
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
    })
  },
  setGroup(fg_name) {
    return axios.post('/group/create', {
      args: {
        fg_name: fg_name
      }
    })
  },
  removeGroup(fg_name) {
    return axios.post('/group/remove', {
      args: {
        fg_name: fg_name
      }
    })
  },
  setGroupMember(fg_name, email) {
    return axios.post('/group/members/add', {
      args: {
        fg_name: fg_name,
        email: email
      }
    })
  },
  removeGroupMember(fg_name, email) {
    return axios.post('/group/members/remove', {
      args: {
        fg_name: fg_name,
        email: email
      }
    })
  },
  setShare(item_id, fg_name) {
    return axios.post('/post/share', {
      args: {
        item_id: item_id,
        fg_name: fg_name
      }
    })
  },
  setSaved(post_id) {
    return axios.post('/post/save', {
      data: {
        post_id: post_id
      }
    })
  },
  removeSaved(post_id) {
    return axios.post('/post/unsave', {
      data: {
        post_id: post_id
      }
    })
  },
  register(email, password, first_name, last_name) {
    return axios.post('/register', {
      auth: {
        email: email,
        password: password
      }
    })
  },
  login(email, password) {
    return axios.post('/login', {
      auth: {
        email: email,
        password: password
      }
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
    })
  }
};
