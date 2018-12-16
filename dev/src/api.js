import './plugins/axios'
// axios.defaults.baseURL = 'https://pricoshaapi.drew.hu'
// axios.defaults.baseURL = 'http://localhost:5000'
axios.defaults.withCredentials = true
// console.log(axios.defaults)
axios.interceptors.request.use(request => {
  console.log('Starting Request: ',request.url, request)
  return request
})

axios.interceptors.response.use(response => {
  console.log('Response: ', response.data, response)
  return response
})

export default {
  authed: false,
  getPosts(url = 'public', page = 1, results_per_page = 10) {
    return axios.get('/posts/' + url, {
      params: {
        page: page,
        results_per_page: results_per_page
      }
    })
  },
  getPost(item_id) {
    return axios.get('/post', {
      params: {
        item_id: item_id
      }
    })
  },
  setPost(formdata) { // Must be form for file upload
    return axios.post('/post/create', formdata)
  },
  setRating(item_id, emoji) {
    return axios.post('/rate', {
      item_id: item_id,
      emoji: emoji
    })
  },
  getRatings(item_id) {
    return axios.get('/ratings', {
      params: {
        item_id: item_id
      }
    })
  },
  setTagged(item_id, tagee_email) {
    return axios.post('/tags/create', {
      item_id: item_id,
      tagee_email: tagee_email
    })
  },
  getProposedTags() {
    return axios.get('/tags/proposed', {
      params: {
        page: page,
        results_per_page: results_per_page
      }
    })
  },
  modifyProposedTag(item_id, decision) {
    return axios.post('/tags/modify', {
      item_id: item_id,
      decision: decision
    })
  },
  getProfile(email) {
    return axios.get('/profile', {
      params: {
        email: email
      }
    })
  },
  getFriends() {
    return axios.get('/friends')
  },
  setFriend(email) {
    return axios.post('/friend', {
      email: email
    })
  },
  removeFriend(email) {
    return axios.post('/unfriend', {
      email: email
    })
  },
  getGroups(names_only = false) {
    return axios.get('/groups', {
      params: {
        names_only: names_only
      }
    })
  },
  setGroup(fg_name) {
    return axios.post('/group/create', {
      fg_name: fg_name
    })
  },
  removeGroup(fg_name) {
    return axios.post('/group/remove', {
      fg_name: fg_name
    })
  },
  setGroupMember(fg_name, email) {
    return axios.post('/group/members/add', {
      fg_name: fg_name,
      email: email
    })
  },
  removeGroupMember(fg_name, email) {
    return axios.post('/group/members/remove', {
      fg_name: fg_name,
      email: email
    })
  },
  setShare(item_id, fg_name) {
    return axios.post('/post/share', {
      item_id: item_id,
      fg_name: fg_name
    })
  },
  setSaved(item_id) {
    return axios.post('/post/save', {
      item_id: item_id
    })
  },
  removeSaved(item_id) {
    return axios.post('/post/unsave', {
      item_id: item_id
    })
  },
  getComments(item_id) {
    return axios.get('/comments', {
      params: {
        item_id: item_id
      }
    })
  },
  setComment(item_id, comment) {
    return axios.post('/comments/post', {
      item_id: item_id,
      comment: comment
    })
  },
  register(email, password, first_name, last_name) {
    return axios.post('/register', {
      first_name: first_name,
      last_name: last_name
    }, {
      auth: {
        username: email,
        password: password
      }
    })
  },
  login(email, password) {
    return axios.post('/login', {}, {
      auth: {
        username: email,
        password: password
      }
    })
  },
  logout() {
    return axios.get('/logout')
  },
  resetPassword(email, old_password, new_password) {
    return axios.post('/reset', {
      old_password: old_password,
      new_password: new_password
    })
  }
};
