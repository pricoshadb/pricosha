<template>
  <v-card class='sm-12 md-8 lg-6'>
    <v-toolbar dark color="primary">
      <v-toolbar-title>Groups</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-text-field
        name="fg_name"
        label="add group"
        v-model='name_value'
        hide-details
        prefix='+'
        @keyup.enter='addGroup()'>
      </v-text-field>
      <v-expansion-panel expand>
        <v-expansion-panel-content
        v-for="group in groups"
        :key="group.fg_name">
          <div slot="header">
            {{group.fg_name}}
            <v-btn round outline color="error" dark
            @click='removeGroup(group)'>remove</v-btn>
          </div>
          <v-card>
            <v-combobox
              v-model="group.members"
              chips
              multiple
              @input='modifyGroup(group)'>
              <template slot="selection" slot-scope="data">
                <v-chip
                  :selected="data.selected"
                  close
                  @input="removeGroupMember(group, data.item)">
                  <strong>{{ data.item }}</strong>&nbsp;
                </v-chip>
              </template>
            </v-combobox>
          </v-card>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: 'Groups',
    data() {
      return {
        name_value: '',
        groups: []
      }
    },
    methods: {
      addGroup() {
        this.name_value=this.name_value.trim()
        if (!this.name_value) return
        this.pricosha.setGroup(this.name_value)
        this.groups.push({
          fg_name: this.name_value,
          members:[]
        })
        this.name_value=''
      },
      removeGroup(group) {
        this.pricosha.removeGroup(group.fg_name)
        this.groups.splice(this.groups.indexOf(group),1)
      },
      removeGroupMember(group, member) {
        this.pricosha.removeGroupMember(group.fg_name, member)
        group.members.splice(group.members.indexOf(member),1)
      },
      modifyGroup(group) {
        this.pricosha.setGroupMember(group.fg_name, group.members[-1])
      }
    },
    created() {
      this.pricosha.getGroups().then(response => {
        this.groups = response.data
      })
    }
  }
</script>
