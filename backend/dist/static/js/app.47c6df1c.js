(function(e){function t(t){for(var i,o,n=t[0],l=t[1],c=t[2],d=0,m=[];d<n.length;d++)o=n[d],r[o]&&m.push(r[o][0]),r[o]=0;for(i in l)Object.prototype.hasOwnProperty.call(l,i)&&(e[i]=l[i]);u&&u(t);while(m.length)m.shift()();return s.push.apply(s,c||[]),a()}function a(){for(var e,t=0;t<s.length;t++){for(var a=s[t],i=!0,n=1;n<a.length;n++){var l=a[n];0!==r[l]&&(i=!1)}i&&(s.splice(t--,1),e=o(o.s=a[0]))}return e}var i={},r={app:0},s=[];function o(t){if(i[t])return i[t].exports;var a=i[t]={i:t,l:!1,exports:{}};return e[t].call(a.exports,a,a.exports,o),a.l=!0,a.exports}o.m=e,o.c=i,o.d=function(e,t,a){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:a})},o.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var a=Object.create(null);if(o.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var i in e)o.d(a,i,function(t){return e[t]}.bind(null,i));return a},o.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="/";var n=window["webpackJsonp"]=window["webpackJsonp"]||[],l=n.push.bind(n);n.push=t,n=n.slice();for(var c=0;c<n.length;c++)t(n[c]);var u=l;s.push([0,"chunk-vendors"]),a()})({0:function(e,t,a){e.exports=a("56d7")},"02b1":function(e,t,a){"use strict";var i=a("574c"),r=a.n(i);r.a},5036:function(e,t,a){},"56d7":function(e,t,a){"use strict";a.r(t);var i=a("2b0e"),r=a("bb71");a("da64");i["a"].use(r["a"],{iconfont:"md"});var s=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-app",{attrs:{id:"inspire"}},[a("v-navigation-drawer",{attrs:{fixed:"",app:""},model:{value:e.drawer,callback:function(t){e.drawer=t},expression:"drawer"}},[a("v-list",{attrs:{dense:""}},[a("v-list-tile",{on:{click:function(t){e.drawer=!1,e.content_source="public"}}},[a("v-list-tile-action",[a("v-icon",[e._v("home")])],1),a("v-list-tile-content",[a("v-list-tile-title",[e._v("Home")])],1)],1),[a("v-list-tile",{on:{click:function(t){e.drawer=!1,e.content_source="shared"}}},[a("v-list-tile-action",[a("v-icon",[e._v("share")])],1),a("v-list-tile-content",[a("v-list-tile-title",[e._v("Shared Content")])],1)],1),a("v-list-tile",{on:{click:function(t){e.drawer=!1,e.content_source="saved"}}},[a("v-list-tile-action",[a("v-icon",[e._v("bookmark")])],1),a("v-list-tile-content",[a("v-list-tile-title",[e._v("Saved Content")])],1)],1),a("v-list-tile",{on:{click:function(t){e.drawer=!1,e.groups_dialog=!0}}},[a("v-list-tile-action",[a("v-icon",[e._v("group")])],1),a("v-list-tile-content",[a("v-list-tile-title",[e._v("Groups")])],1)],1),a("v-dialog",{attrs:{"max-width":"600px"},model:{value:e.groups_dialog,callback:function(t){e.groups_dialog=t},expression:"groups_dialog"}},[a("Groups",{on:{end_dialog:function(t){e.groups_dialog=!1}}})],1),a("v-list-tile",{on:{click:function(t){e.drawer=!1,e.friends_dialog=!0}}},[a("v-list-tile-action",[a("v-icon",[e._v("favorite")])],1),a("v-list-tile-content",[a("v-list-tile-title",[e._v("Friends")])],1)],1),a("v-dialog",{attrs:{"max-width":"600px"},model:{value:e.friends_dialog,callback:function(t){e.friends_dialog=t},expression:"friends_dialog"}},[a("Friends",{on:{end_dialog:function(t){e.friends_dialog=!1}}})],1)],e.$pricosha.authed?a("v-list-tile",{on:{click:function(t){e.drawer=!1,e.logout()}}},[a("v-list-tile-action",[a("v-icon",[e._v("meeting_room")])],1),a("v-list-tile-content",[a("v-list-tile-title",[e._v("Logout")])],1)],1):e._e(),e.$pricosha.authed?e._e():a("v-list-tile",{on:{click:function(t){e.drawer=!1,e.login_dialog=!0}}},[a("v-list-tile-action",[a("v-icon",[e._v("meeting_room")])],1),a("v-list-tile-content",[a("v-list-tile-title",[e._v("Login")])],1)],1),a("v-dialog",{attrs:{"max-width":"600px"},model:{value:e.login_dialog,callback:function(t){e.login_dialog=t},expression:"login_dialog"}},[a("Login",{on:{end_dialog:function(t){e.login_dialog=!1},success:function(t){e.$pricosha.authed=!0}}})],1)],2)],1),a("v-toolbar",{attrs:{color:"indigo",dark:"",fixed:"",app:""}},[a("v-toolbar-side-icon",{on:{click:function(t){t.stopPropagation(),e.drawer=!e.drawer}}}),a("v-toolbar-title",[e._v("PriCoSha")])],1),a("v-content",[a("Posts",{attrs:{src:e.content_source}})],1),a("v-footer",{attrs:{color:"indigo",app:""}},[a("span",{staticClass:"white--text"},[e._v("@ 2018 // Maxwell Colin Reddy // Lucas Pollice // Khoa Nguyen // Andrew Hu")])])],1)},o=[],n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-card",[a("v-toolbar",{attrs:{dark:"",color:"primary"}},[a("v-toolbar-title",[e._v("Login")])],1),a("v-card-text",[a("v-form",[a("v-text-field",{attrs:{"prepend-icon":"person",name:"login",label:"Email",type:"text"},model:{value:e.email,callback:function(t){e.email=t},expression:"email"}}),a("v-text-field",{attrs:{"prepend-icon":"lock",name:"password",label:"Password",type:"password",messages:[e.error]},model:{value:e.password,callback:function(t){e.password=t},expression:"password"}}),e.show_register?a("div",[a("v-text-field",{attrs:{"prepend-icon":" ",name:"first_name",label:"First Name",type:"text"},model:{value:e.first_name,callback:function(t){e.first_name=t},expression:"first_name"}}),a("v-text-field",{attrs:{"prepend-icon":" ",name:"last_name",label:"Last Name",type:"text"},model:{value:e.last_name,callback:function(t){e.last_name=t},expression:"last_name"}})],1):e._e()],1),e.show_register?e._e():a("v-layout",{staticClass:"text-xs-center",attrs:{column:""}},[a("span",{staticClass:"error--text"},[e._v("Dont have an account?")]),a("div",[a("v-btn",{attrs:{color:"error",small:""},on:{click:function(t){e.show_register=!0}}},[e._v("\n          Register\n        ")])],1)])],1),a("v-card-actions",[a("v-spacer"),e.show_register?a("v-btn",{attrs:{color:"error"},on:{click:function(t){e.register()}}},[e._v("\n      Register\n    ")]):a("v-btn",{attrs:{color:"primary"},on:{click:function(t){e.login()}}},[e._v("\n      Login\n    ")])],1)],1)},l=[],c={name:"Login",data(){return{email:null,password:null,first_name:"",last_name:"",show_register:!1,error:""}},methods:{login(){this.$pricosha.login(this.email,this.password).then(e=>{this.$pricosha.authed=!0,this.$emit("success"),this.$emit("end_dialog"),this.error=""}).catch(e=>{this.error="Invalid password",console.error(e)})},register(){this.$pricosha.register(this.email,this.password,this.first_name,this.last_name).then(e=>{this.show_register=!1,this.login()}).catch(e=>{this.error="Registration error",console.error(e)})}}},u=c,d=a("2877"),m=a("6544"),p=a.n(m),v=a("8336"),h=a("b0af"),_=a("99d9"),f=a("4bd4"),g=a("a722"),b=a("9910"),x=a("2677"),y=a("71d9"),V=a("2a7f"),k=Object(d["a"])(u,n,l,!1,null,null,null);k.options.__file="Login.vue";var w=k.exports;p()(k,{VBtn:v["a"],VCard:h["a"],VCardActions:_["a"],VCardText:_["b"],VForm:f["a"],VLayout:g["a"],VSpacer:b["a"],VTextField:x["a"],VToolbar:y["a"],VToolbarTitle:V["a"]});var C=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-container",{attrs:{fluid:"","fill-height":""}},[a("v-layout",{attrs:{column:""}},[0==e.create_new&&e.$pricosha.authed?a("v-card",{attrs:{flat:""}},[a("v-layout",{staticClass:"py-2",attrs:{row:"","justify-center":""}},[a("v-btn",{attrs:{large:"",color:"primary"},on:{click:function(t){e.create_new=!0}}},[a("v-icon",[e._v("add")])],1)],1)],1):e._e(),1==e.create_new?a("CustomPost",{on:{submit:function(t){e.create_new=!1,e.updatePosts()}}}):e._e(),e._l(e.content,function(t,i){return a("Post",{key:t.item_id,attrs:{item:t,group_names:e.group_names},on:{dirty:function(a){e.updatePost(t.item_id,i)}}})}),a("v-spacer"),a("v-layout",{attrs:{row:"","justify-center":"","align-center":"",shrink:""}},[a("v-btn",{attrs:{fab:"",small:"",depressed:"",disabled:e.page<=1},on:{click:function(t){e.page--}}},[a("v-icon",[e._v("chevron_left")])],1),a("v-btn",{staticStyle:{"pointer-events":"none"},attrs:{fab:"",depressed:""}},[e._v("\n        "+e._s(e.page)+"\n      ")]),a("v-btn",{attrs:{fab:"",small:"",depressed:""},on:{click:function(t){e.page++}}},[a("v-icon",[e._v("chevron_right")])],1)],1)],2)],1)},P=[],$=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-card",[a("v-img",{attrs:{src:e.item.file_path}}),a("v-card-title",{staticClass:"pt-1 pb-0"},[a("div",[a("v-layout",{attrs:{row:""}},[a("h3",{staticClass:"headline mb-0"},[e._v(e._s(e.item.item_name))]),a("EmojiBar",{attrs:{emotes:e.ratings},on:{emoji:function(t){e.rate(t)}}})],1),a("UserChip",{attrs:{email:e.item.email,color:"primary","text-color":"white"}}),e.item.tagged?a("v-layout",{attrs:{row:""}},[e._l(e.item.tagged,function(e){return a("v-subheader",{staticClass:"px-0"},[a("UserChip",{attrs:{email:e}})],1)}),a("v-text-field",{attrs:{label:"+","hide-details":"",solo:"",flat:""},on:{keyup:function(t){if(!("button"in t)&&e._k(t.keyCode,"enter",13,t.key,"Enter"))return null;e.addTag(e.item,t)}},model:{value:e.tag_value,callback:function(t){e.tag_value=t},expression:"tag_value"}})],2):e._e()],1)]),a("v-card-actions",[a("v-btn",{attrs:{flat:"",icon:"",color:"yellow"},on:{click:function(t){e.toggleSave()}}},[e.saved?a("v-icon",[e._v("bookmark")]):a("v-icon",[e._v("bookmark_border")])],1),a("v-menu",[a("v-btn",{attrs:{slot:"activator",flat:"",icon:""},on:{click:function(t){e.share_state=!0}},slot:"activator"},[a("v-icon",[e._v("share")])],1),a("v-card",[a("v-select",{attrs:{items:e.group_names,label:"groups"},on:{input:function(t){e.sharePost(t)}}})],1)],1),a("v-btn",{attrs:{flat:"",icon:"",color:"primary"},on:{click:function(t){e.show_comments=!e.show_comments}}},[a("v-icon",[e._v("chat")])],1)],1),a("v-divider"),a("v-card-text",{directives:[{name:"show",rawName:"v-show",value:e.show_comments,expression:"show_comments"}]},[a("div",{staticClass:"commentdrop"},e._l(e.comments,function(t){return a("v-card",{key:t.email,staticClass:"ma-1 textwrap",attrs:{outline:"",flat:"",color:"grey lighten-5"}},[a("v-card-text",{staticClass:"pa-1"},[a("br"),e._v("\n          "+e._s(t.content)+"\n        ")])],1)})),a("v-text-field",{attrs:{"single-line":"",label:"comment"},on:{keyup:function(t){if(!("button"in t)&&e._k(t.keyCode,"enter",13,t.key,"Enter"))return null;e.comment()}},model:{value:e.comment_value,callback:function(t){e.comment_value=t},expression:"comment_value"}})],1)],1)},T=[],j=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-layout",{attrs:{row:""}},[a("v-flex",{staticStyle:{"overflow-x":"hidden"},attrs:{shrink:""}},[a("v-layout",{staticStyle:{"max-width":"20rem"},attrs:{row:""}},e._l(e.emotes,function(t){return a("v-chip",{key:t.emoji,attrs:{small:""}},[e._v("\n        "+e._s(t.emoji)+"\n        "+e._s(t.count)+"\n      ")])}))],1),a("emoji-picker",{attrs:{search:e.search},on:{emoji:e.insert},scopedSlots:e._u([{key:"emoji-invoker",fn:function(t){var i=t.events;return a("div",e._g({},i),[a("v-chip",{staticClass:"px-0",attrs:{small:""}},[e._v(" + ")])],1)}},{key:"emoji-picker",fn:function(t){var i=t.emojis,r=t.insert;t.display;return a("div",{},[a("v-card",{staticClass:"emoji-picker sm-12"},[a("v-text-field",{attrs:{box:"",label:"search"},model:{value:e.search,callback:function(t){e.search=t},expression:"search"}}),a("v-expansion-panel",{attrs:{expand:""}},e._l(i,function(t,i){return a("v-expansion-panel-content",{key:i},[a("div",{attrs:{slot:"header"},slot:"header"},[e._v(e._s(i))]),a("v-card",[a("v-layout",{attrs:{row:"",wrap:""}},e._l(t,function(t,i){return a("v-avatar",{key:i,on:{click:function(e){r(t)}}},[a("span",{staticClass:"headline",attrs:{title:i}},[e._v("\n                     "+e._s(t)+"\n                   ")])])}))],1)],1)}))],1)],1)}}])}),a("v-spacer")],1)},F=[],S=a("669f"),L=a.n(S),G={name:"EmojiBar",components:{EmojiPicker:L.a},props:{emotes:Array},data(){return{search:""}},methods:{insert(e){let t=!1;for(var a=0;a<this.emotes.length;a++)this.emotes[a].emoji===e&&(this.emotes[a].count+=1,t=!0);t||this.emotes.push({emoji:e,count:1}),this.$emit("emoji",e)}}},O=G,E=(a("718c"),a("8212")),U=a("cc20"),A=a("cd55"),N=a("49e2"),B=a("0e8f"),M=Object(d["a"])(O,j,F,!1,null,null,null);M.options.__file="EmojiBar.vue";var R=M.exports;p()(M,{VAvatar:E["a"],VCard:h["a"],VChip:U["a"],VExpansionPanel:A["a"],VExpansionPanelContent:N["a"],VFlex:B["a"],VLayout:g["a"],VSpacer:b["a"],VTextField:x["a"]});var I=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-dialog",{attrs:{"max-width":"500"}},[a("v-chip",{attrs:{slot:"activator",color:e.color,"text-color":e.textColor,close:e.close},slot:"activator"},[e.user.avatar?a("v-avatar",[a("img",{attrs:{src:e.user.avatar}})]):e._e(),e._v("\n    "+e._s(e.user.first_name)+" "+e._s(e.user.last_name)+"\n  ")],1),a("v-card",[a("v-img",{attrs:{"aspect-ratio":1,src:e.user.avatar}}),a("v-card-title",[a("div",[a("div",{staticClass:"headline"},[e._v(e._s(e.user.first_name)+" "+e._s(e.user.last_name))]),a("span",{staticClass:"grey--text"},[e._v(e._s(e.email))])])]),a("v-card-text",[e._v("\n      "+e._s(e.user.bio)+"\n    ")]),a("v-card-actions",[a("v-btn",{attrs:{flat:"",icon:"",color:"red"},on:{click:function(t){e.toggleFriend()}}},[e.user.friend?a("v-icon",[e._v("heart")]):a("v-icon",[e._v("heart_border")])],1)],1)],1)],1)},D=[],q={name:"UserChip",props:{email:{type:String,required:!0},"text-color":String,color:String,close:Boolean},data(){return{user:{bio:"",avatar:"",first_name:"",last_name:"",friend:!1}}},watch:{email:{immediate:!0,handler(e,t){this.$pricosha.getProfile(e).then(e=>{this.user=e.data})}}},methods:{toggleFriend(){this.user.friend=!this.user.friend,this.user.friend?this.$pricosha.setFriend(this.email):this.$pricosha.removeFriend(this.email)}}},J=q,H=(a("99c4"),a("12b2")),K=a("169a"),z=a("132d"),Q=a("adda"),W=Object(d["a"])(J,I,D,!1,null,null,null);W.options.__file="UserChip.vue";var X=W.exports;p()(W,{VAvatar:E["a"],VBtn:v["a"],VCard:h["a"],VCardActions:_["a"],VCardText:_["b"],VCardTitle:H["a"],VChip:U["a"],VDialog:K["a"],VIcon:z["a"],VImg:Q["a"]});var Y={name:"Post",components:{EmojiBar:R,UserChip:X},data(){return{show_comments:!1,tag_value:"",comment_value:"",share_state:!1,saved:!1,comments:[],ratings:[]}},props:{group_names:Array,item:{type:Object,required:!0}},methods:{addTag(){this.$pricosha.setTagged(this.item.item_id,this.tag_value),this.tag_value="",this.$emit("dirty")},toggleSave(){this.saved=!this.saved,this.saved?this.$pricosha.setSaved(this.item.item_id):this.$pricosha.removeSaved(this.item.item_id)},sharePost(e){this.$pricosha.setShare(this.item.item_id,e)},comment(){this.$pricosha.setComment(this.item.item_id,this.comment_value).then(e=>{this.comments.push({content:this.comment_value}),this.comment_value=""})},rate(e){this.$pricosha.setRating(this.item.item_id,e)}},created(){this.$pricosha.getComments(this.item.item_id).then(e=>{this.comments=e.data}),this.$pricosha.getRatings(this.item.item_id).then(e=>{this.ratings=e.data})}},Z=Y,ee=(a("02b1"),a("ce7e")),te=a("e449"),ae=a("b56d"),ie=a("e0c7"),re=Object(d["a"])(Z,$,T,!1,null,null,null);re.options.__file="Post.vue";var se=re.exports;p()(re,{VBtn:v["a"],VCard:h["a"],VCardActions:_["a"],VCardText:_["b"],VCardTitle:H["a"],VDivider:ee["a"],VIcon:z["a"],VImg:Q["a"],VLayout:g["a"],VMenu:te["a"],VSelect:ae["a"],VSubheader:ie["a"],VTextField:x["a"]});var oe=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-card",[a("v-img",{attrs:{src:e.path||""}}),a("v-card-text",{staticClass:"pt-1 pb-0"},[a("v-form",{ref:"form"},[a("v-text-field",{staticClass:"pt-2",attrs:{solo:"","hide-details":"",label:"Title"},model:{value:e.item_name,callback:function(t){e.item_name=t},expression:"item_name"}}),a("FileUpload",{staticClass:"pt-2",on:{url:function(t){e.path=t},file:function(t){e.image_content=t}}}),a("v-layout",{attrs:{wrap:""}},[a("v-checkbox",{attrs:{"hide-details":"",label:"public"},model:{value:e.is_pub,callback:function(t){e.is_pub=t},expression:"is_pub"}}),a("v-spacer"),a("v-btn",{attrs:{color:"primary"},on:{click:e.submit}},[e._v("Submit")])],1)],1)],1)],1)},ne=[],le=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-flex",{staticClass:"text-xs-center",attrs:{xs12:""}},[a("v-text-field",{attrs:{solo:"",label:"Select Image","append-icon":"attach_file","hide-details":""},on:{click:e.pickFile},model:{value:e.imageName,callback:function(t){e.imageName=t},expression:"imageName"}}),a("input",{ref:"image",staticStyle:{display:"none"},attrs:{type:"file",accept:"image/*"},on:{change:e.onFilePicked}})],1)},ce=[],ue={name:"FileUpload",data(){return{imageName:"",imageUrl:"",imageFile:""}},methods:{pickFile(){this.$refs.image.click()},onFilePicked(e){const t=e.target.files;if(void 0!==t[0]){if(this.imageName=t[0].name,this.imageName.lastIndexOf(".")<=0)return;const e=new FileReader;e.readAsDataURL(t[0]),e.addEventListener("load",()=>{this.imageUrl=e.result,this.imageFile=t[0]})}else this.imageName="",this.imageFile="",this.imageUrl=""}},watch:{imageUrl:{handler(e,t){this.$emit("url",e)}},imageFile:{handler(e,t){this.$emit("file",e)}}}},de=ue,me=(a("e359"),Object(d["a"])(de,le,ce,!1,null,null,null));me.options.__file="FileUpload.vue";var pe=me.exports;p()(me,{VFlex:B["a"],VTextField:x["a"]});var ve={name:"CustomPost",data(){return{item_name:"",is_pub:!1,image_content:null,path:""}},components:{FileUpload:pe},props:{},methods:{submit(){if(this.$refs.form.validate()){let e=new FormData,t={is_pub:this.is_pub,item_name:this.item_name};e.append("data",JSON.stringify(t)),e.append("image_content",this.image_content),this.$pricosha.setPost(e).then(e=>{this.$emit("submit")})}}}},he=ve,_e=(a("d0dc"),a("ac7c")),fe=Object(d["a"])(he,oe,ne,!1,null,null,null);fe.options.__file="CustomPost.vue";var ge=fe.exports;p()(fe,{VBtn:v["a"],VCard:h["a"],VCardText:_["b"],VCheckbox:_e["a"],VForm:f["a"],VImg:Q["a"],VLayout:g["a"],VSpacer:b["a"],VTextField:x["a"]});var be={name:"Posts",props:{src:{type:String,default:"public"}},components:{Post:se,CustomPost:ge},data(){return{content:[],page:1,group_names:[],create_new:!1}},methods:{updatePost(e,t){this.$pricosha.getPost(e).then(e=>{this.content[t]=e.data})},updatePosts(){this.$pricosha.getPosts(this.src,this.page).then(e=>{this.content=e.data})}},created(){this.updatePosts(),this.$pricosha.getGroups(!0).then(e=>{this.group_names=e.data})},watch:{src:{handler(e,t){this.updatePosts()}},page:{handler(){this.updatePosts()}}}},xe=be,ye=(a("eebb"),a("a523")),Ve=Object(d["a"])(xe,C,P,!1,null,null,null);Ve.options.__file="Posts.vue";var ke=Ve.exports;p()(Ve,{VBtn:v["a"],VCard:h["a"],VContainer:ye["a"],VIcon:z["a"],VLayout:g["a"],VSpacer:b["a"]});var we=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-card",{staticClass:"sm-12 md-8 lg-6"},[a("v-toolbar",{attrs:{dark:"",color:"primary"}},[a("v-toolbar-title",[e._v("Friends")])],1),a("v-card-text",[a("v-list",[e._l(e.friends,function(t,i){return a("v-list-tile",{key:t.email},[a("v-list-tile-content",[e._v("\n          "+e._s(t.email)+"\n        ")]),a("v-btn",{attrs:{round:"",outline:"",color:"error",dark:""},on:{click:function(t){e.removeFriend(i)}}},[e._v("unfriend")])],1)}),0==e.friends.length?a("v-list-tile",[a("v-layout",{attrs:{"justify-center":""}},[a("span",{staticClass:"headline grey--text"},[e._v(":(")])])],1):e._e()],2)],1)],1)},Ce=[],Pe={name:"Friends",data(){return{friends:[]}},methods:{removeFriend(e){this.$pricosha.removeFriend(friend.email),this.friends.splice(e,1)}},created(){this.$pricosha.getFriends().then(e=>{this.friends=e.data})}},$e=Pe,Te=a("8860"),je=a("ba95"),Fe=a("5d23"),Se=Object(d["a"])($e,we,Ce,!1,null,null,null);Se.options.__file="Friends.vue";var Le=Se.exports;p()(Se,{VBtn:v["a"],VCard:h["a"],VCardText:_["b"],VLayout:g["a"],VList:Te["a"],VListTile:je["a"],VListTileContent:Fe["a"],VToolbar:y["a"],VToolbarTitle:V["a"]});var Ge=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-card",{staticClass:"sm-12 md-8 lg-6"},[a("v-toolbar",{attrs:{dark:"",color:"primary"}},[a("v-toolbar-title",[e._v("Groups")])],1),a("v-card-text",[a("v-text-field",{attrs:{name:"fg_name",label:"add group","hide-details":"",prefix:"+"},on:{keyup:function(t){if(!("button"in t)&&e._k(t.keyCode,"enter",13,t.key,"Enter"))return null;e.addGroup()}},model:{value:e.name_value,callback:function(t){e.name_value=t},expression:"name_value"}}),a("v-expansion-panel",{attrs:{expand:""}},e._l(e.groups,function(t){return a("v-expansion-panel-content",{key:t.fg_name},[a("div",{attrs:{slot:"header"},slot:"header"},[e._v("\n          "+e._s(t.fg_name)+"\n          "),a("v-btn",{attrs:{round:"",outline:"",color:"error",dark:""},on:{click:function(a){e.removeGroup(t)}}},[e._v("remove")])],1),a("v-card",[a("v-combobox",{attrs:{chips:"",multiple:""},on:{input:function(a){e.modifyGroup(t)}},scopedSlots:e._u([{key:"selection",fn:function(i){return[a("v-chip",{attrs:{selected:i.selected,close:""},on:{input:function(a){e.removeGroupMember(t,i.item)}}},[a("strong",[e._v(e._s(i.item))]),e._v(" \n              ")])]}}]),model:{value:t.members,callback:function(a){e.$set(t,"members",a)},expression:"group.members"}})],1)],1)}))],1)],1)},Oe=[],Ee={name:"Groups",data(){return{name_value:"",groups:[]}},methods:{addGroup(){this.name_value=this.name_value.trim(),this.name_value&&(this.$pricosha.setGroup(this.name_value),this.groups.push({fg_name:this.name_value,members:[]}),this.name_value="")},removeGroup(e){this.$pricosha.removeGroup(e.fg_name),this.groups.splice(this.groups.indexOf(e),1)},removeGroupMember(e,t){this.$pricosha.removeGroupMember(e.fg_name,t),e.members.splice(e.members.indexOf(t),1)},modifyGroup(e){this.$pricosha.setGroupMember(e.fg_name,e.members[-1])}},created(){this.$pricosha.getGroups().then(e=>{this.groups=e.data})}},Ue=Ee,Ae=a("2b5d"),Ne=Object(d["a"])(Ue,Ge,Oe,!1,null,null,null);Ne.options.__file="Groups.vue";var Be=Ne.exports;p()(Ne,{VBtn:v["a"],VCard:h["a"],VCardText:_["b"],VChip:U["a"],VCombobox:Ae["a"],VExpansionPanel:A["a"],VExpansionPanelContent:N["a"],VTextField:x["a"],VToolbar:y["a"],VToolbarTitle:V["a"]});var Me=a("bc3a"),Re=a.n(Me);let Ie={};const De=Re.a.create(Ie);De.interceptors.request.use(function(e){return e},function(e){return Promise.reject(e)}),De.interceptors.response.use(function(e){return e},function(e){return Promise.reject(e)}),Plugin.install=function(e,t){e.axios=De,window.axios=De,Object.defineProperties(e.prototype,{axios:{get(){return De}},$axios:{get(){return De}}})},i["a"].use(Plugin);Plugin;axios.defaults.withCredentials=!0,axios.interceptors.request.use(e=>{return console.log("Starting Request: ",e.url,e),e}),axios.interceptors.response.use(e=>{return console.log("Response: ",e.data,e),e});var qe={authed:!1,getPosts(e="public",t=1,a=10){return axios.get("/posts/"+e,{params:{page:t,results_per_page:a}})},getPost(e){return axios.get("/post",{params:{item_id:e}})},setPost(e){return axios.post("/post/create",e)},setRating(e,t){return axios.post("/rate",{item_id:e,emoji:t})},getRatings(e){return axios.get("/ratings",{params:{item_id:e}})},setTagged(e,t){return axios.post("/tags/create",{item_id:e,tagee_email:t})},getProposedTags(){return axios.get("/tags/proposed",{params:{page:page,results_per_page:results_per_page}})},modifyProposedTag(e,t){return axios.post("/tags/modify",{item_id:e,decision:t})},getProfile(e){return axios.get("/profile",{params:{email:e}})},getFriends(){return axios.get("/friends")},setFriend(e){return axios.post("/friend",{email:e})},removeFriend(e){return axios.post("/unfriend",{email:e})},getGroups(e=!1){return axios.get("/groups",{params:{names_only:e}})},setGroup(e){return axios.post("/group/create",{fg_name:e})},removeGroup(e){return axios.post("/group/remove",{fg_name:e})},setGroupMember(e,t){return axios.post("/group/members/add",{fg_name:e,email:t})},removeGroupMember(e,t){return axios.post("/group/members/remove",{fg_name:e,email:t})},setShare(e,t){return axios.post("/post/share",{item_id:e,fg_name:t})},setSaved(e){return axios.post("/post/save",{item_id:e})},removeSaved(e){return axios.post("/post/unsave",{item_id:e})},getComments(e){return axios.get("/comments",{params:{item_id:e}})},setComment(e,t){return axios.post("/comments/post",{item_id:e,comment:t})},register(e,t,a,i){return axios.post("/register",{first_name:a,last_name:i},{auth:{username:e,password:t}})},login(e,t){return axios.post("/login",{},{auth:{username:e,password:t}})},logout(){return axios.get("/logout")},resetPassword(e,t,a){return axios.post("/reset",{old_password:t,new_password:a})}},Je={name:"App",components:{Login:w,Posts:ke,Friends:Le,Groups:Be},data(){return{groups_dialog:null,login_dialog:null,friends_dialog:null,drawer:null,content_source:"public"}},methods:{logout(){this.$pricosha.logout().then(e=>{this.$pricosha.authed=!1})}}},He=Je,Ke=a("7496"),ze=a("549c"),Qe=a("553a"),We=a("40fe"),Xe=a("f774"),Ye=a("706c"),Ze=Object(d["a"])(He,s,o,!1,null,null,null);Ze.options.__file="App.vue";var et=Ze.exports;p()(Ze,{VApp:Ke["a"],VContent:ze["a"],VDialog:K["a"],VFooter:Qe["a"],VIcon:z["a"],VList:Te["a"],VListTile:je["a"],VListTileAction:We["a"],VListTileContent:Fe["a"],VListTileTitle:Fe["b"],VNavigationDrawer:Xe["a"],VToolbar:y["a"],VToolbarSideIcon:Ye["a"],VToolbarTitle:V["a"]}),i["a"].config.productionTip=!1,i["a"].prototype.$pricosha=qe,new i["a"]({render:e=>e(et)}).$mount("#app")},"574c":function(e,t,a){},"718c":function(e,t,a){"use strict";var i=a("b570"),r=a.n(i);r.a},"99c4":function(e,t,a){"use strict";var i=a("bdc2"),r=a.n(i);r.a},b570:function(e,t,a){},b92a:function(e,t,a){},bdc2:function(e,t,a){},d0dc:function(e,t,a){"use strict";var i=a("5036"),r=a.n(i);r.a},e359:function(e,t,a){"use strict";var i=a("b92a"),r=a.n(i);r.a},e5b0:function(e,t,a){},eebb:function(e,t,a){"use strict";var i=a("e5b0"),r=a.n(i);r.a}});
//# sourceMappingURL=app.47c6df1c.js.map