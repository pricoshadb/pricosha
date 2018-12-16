<template>
  <v-layout row>
    <v-flex shrink style="overflow-x: hidden">
      <v-layout row style='max-width: 20rem'>
        <v-chip small v-for='emote in emotes' :key='emote.emoji'>
          {{emote.emoji}}
          {{emote.count}}
        </v-chip>
      </v-layout>
    </v-flex>
    <emoji-picker @emoji="insert" :search="search">
       <div slot="emoji-invoker" slot-scope="{ events }" v-on="events">
         <v-chip small class='px-0'> + </v-chip>
       </div>
       <div slot="emoji-picker" slot-scope="{ emojis, insert, display }">
         <v-card class="emoji-picker sm-12">
           <v-text-field box label="search" v-model="search"></v-text-field>
           <v-expansion-panel expand>
             <v-expansion-panel-content
             v-for="(emojiGroup, category) in emojis"
             :key="category">
               <div slot="header">{{ category }}</div>
               <v-card>
                 <v-layout row wrap>
                   <v-avatar v-for="(emoji, emojiName) in emojiGroup"
                   :key="emojiName"
                   @click="insert(emoji)">
                     <span :title="emojiName" class="headline">
                       {{ emoji }}
                     </span>
                   </v-avatar>
                 </v-layout>
               </v-card>
             </v-expansion-panel-content>
           </v-expansion-panel>
         </v-card>
       </div>
    </emoji-picker>
    <v-spacer></v-spacer>
  </v-layout>
</template>

<script>
import EmojiPicker from 'vue-emoji-picker'

export default {
  name: 'EmojiBar',
  components: {
    EmojiPicker
  },
  props: {
    emotes: Array
  },
  data() {
    return {
      search: ''
    }
  },
  methods: {
    insert(emoji) {
      let found = false
      for (var i=0; i < this.emotes.length; i++) {
        if (this.emotes[i].emoji === emoji) {
            this.emotes[i].count += 1
            found = true
        }
      }
      if (!found) {
        this.emotes.push({
          'emoji': emoji,
          'count': 1
        })
      }
      this.$emit('emoji', emoji)
    }
  }
}
</script>

<style lang="css">
.emoji-picker {
  position: absolute;
  z-index: 1;
  width: 20rem;
  height: 30rem;
  overflow-y: scroll;
  overflow-x: hidden;
}
.v-chip__content {
  padding: 0 4px !important;
}
</style>
