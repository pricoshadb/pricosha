<template>
  <v-card class='sm-12 md-8 lg-6'>
    <v-toolbar dark color="primary">
      <v-toolbar-title>Groups</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-list>
        <v-list-tile>
          <v-text-field
            name="fg_name"
            label="add group"
            v-model='name_value'
            hide-details
            prefix='+'
            @keyup.enter='addGroup()'>
          </v-text-field>
        </v-list-tile>
        <v-list-group
        v-for="group, index in groups"
        :key="group.fg_name">
          <v-list-tile slot="activator">
            <v-list-tile-content>
              <v-list-tile-title>{{group.fg_name}}</v-list-tile-title>
            </v-list-tile-content>
            <v-btn round outline color="error" dark
            @click='groups.splice(index,1);pricosha.removeGroup(group.fg_name)'>remove</v-btn>
          </v-list-tile>
          <v-list-tile>
            <v-combobox
              v-model="group.members"
              chips
              multiple
              @change=''>
              <template slot="selection" slot-scope="data">
                <v-chip
                  :selected="data.selected"
                  close
                  @input="pricosha.removeGroupMember(group.fg_name, data.item);
                  groups.members.splice(groups.members.indexOf(data.item),1)">
                  <strong>{{ data.item }}</strong>&nbsp;
                </v-chip>
              </template>
            </v-combobox>
          </v-list-tile>
        </v-list-group>
      </v-list>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: 'Groups',
    data() {
      return {
        name_value: '',
        groups: [
          {
            fg_name: 'name',
            members: [
              'example@gmail.com'
              // {
              //   email: 'example@gmail.com',
              //   first_name: 'Lucas',
              //   last_name: 'OhZia'
              // }
            ]
          }
        ]
      }
    },
    methods: {
      addGroup() {
        this.name_value=this.name_value.trim()
        if (!this.name_value) return
        pricosha.setGroup(this.name_value)
        this.groups.push({
          fg_name: this.name_value,
          members:[]
        })
        this.name_value=''
      }
    }
  }
</script>
